from sqlalchemy.orm import Session
from fastapi import HTTPException
from . import models, schemas


# =========================
# PRODUCTOS
# =========================

def create_product(db: Session, product: schemas.ProductCreate):
    db_product = models.Product(**product.model_dump())
    db.add(db_product)
    db.commit()
    db.refresh(db_product)
    return db_product


def get_products(db: Session):
    return db.query(models.Product).all()


def get_product_by_id(db: Session, product_id: int):
    return db.query(models.Product).filter(models.Product.id == product_id).first()


def update_product(db: Session, product_id: int, product: schemas.ProductUpdate):
    db_product = get_product_by_id(db, product_id)
    if not db_product:
        return None

    for key, value in product.model_dump().items():
        setattr(db_product, key, value)

    db.commit()
    db.refresh(db_product)
    return db_product


def delete_product(db: Session, product_id: int):
    db_product = get_product_by_id(db, product_id)
    if not db_product:
        return None

    db.delete(db_product)
    db.commit()
    return True


# =========================
# VENTAS
# =========================

def make_sale(db: Session, sale: schemas.SaleCreate):
    product = db.query(models.Product).filter(models.Product.sku == sale.sku).first()

    if not product:
        raise HTTPException(status_code=404, detail="Producto no encontrado")

    if product.stock < sale.quantity:
        raise HTTPException(status_code=400, detail="Stock insuficiente")

    product.stock -= sale.quantity

    db_sale = models.Sale(product_id=product.id, quantity=sale.quantity)
    db.add(db_sale)
    db.commit()
    db.refresh(db_sale)

    return db_sale


def get_sales(db: Session):
    return db.query(models.Sale).all()


# =========================
# COMPRAS
# =========================

def create_purchase(db: Session, purchase: schemas.PurchaseCreate):
    # Validar que todos los productos existen antes de hacer nada
    for item in purchase.items:
        product = get_product_by_id(db, item.product_id)
        if not product:
            raise HTTPException(
                status_code=404,
                detail=f"Producto con ID {item.product_id} no encontrado. Agregalo primero en 'Agregar producto'."
            )

    # Crear la compra
    db_purchase = models.Purchase(precio_total=purchase.precio_total)
    db.add(db_purchase)
    db.flush()  # Para obtener el ID sin hacer commit todavía

    # Crear los items y sumar stock
    for item in purchase.items:
        product = get_product_by_id(db, item.product_id)
        product.stock += item.quantity

        db_item = models.PurchaseItem(
            purchase_id=db_purchase.id,
            product_id=item.product_id,
            quantity=item.quantity
        )
        db.add(db_item)

    db.commit()
    db.refresh(db_purchase)
    return db_purchase


def get_purchases(db: Session):
    return db.query(models.Purchase).order_by(models.Purchase.fecha.desc()).all()


def get_purchase_total(db: Session):
    result = db.query(models.Purchase).all()
    return sum(p.precio_total for p in result)


def get_sales_total(db: Session):
    """Calcula el total de ingresos por ventas usando precio_venta de cada producto"""
    sales = db.query(models.Sale).all()
    total = 0.0
    for sale in sales:
        product = get_product_by_id(db, sale.product_id)
        if product and product.precio_venta:
            total += product.precio_venta * sale.quantity
    return total


def delete_sale(db: Session, sale_id: int):
    sale = db.query(models.Sale).filter(models.Sale.id == sale_id).first()
    if not sale:
        raise HTTPException(status_code=404, detail="Venta no encontrada")
    product = get_product_by_id(db, sale.product_id)
    if product:
        product.stock += sale.quantity
    db.delete(sale)
    db.commit()
    return {"message": "Venta eliminada y stock restaurado"}


def delete_purchase(db: Session, purchase_id: int):
    purchase = db.query(models.Purchase).filter(models.Purchase.id == purchase_id).first()
    if not purchase:
        raise HTTPException(status_code=404, detail="Compra no encontrada")
    for item in purchase.items:
        product = get_product_by_id(db, item.product_id)
        if product:
            product.stock = max(0, product.stock - item.quantity)
    db.query(models.PurchaseItem).filter(models.PurchaseItem.purchase_id == purchase_id).delete()
    db.delete(purchase)
    db.commit()
    return {"message": "Compra eliminada y stock actualizado"}


# =========================
# DESCUENTOS
# =========================

def create_discount(db: Session, discount: schemas.DiscountCreate):
    for item in discount.items:
        product = get_product_by_id(db, item.product_id)
        if not product:
            raise HTTPException(
                status_code=404,
                detail=f"Producto con ID {item.product_id} no encontrado."
            )

    db_discount = models.Discount(name=discount.name, precio_descuento=discount.precio_descuento)
    db.add(db_discount)
    db.flush()

    for item in discount.items:
        db_item = models.DiscountItem(
            discount_id=db_discount.id,
            product_id=item.product_id,
            quantity=item.quantity
        )
        db.add(db_item)

    db.commit()
    db.refresh(db_discount)
    return db_discount


def get_discounts(db: Session):
    return db.query(models.Discount).order_by(models.Discount.fecha.desc()).all()


def delete_discount(db: Session, discount_id: int):
    discount = db.query(models.Discount).filter(models.Discount.id == discount_id).first()
    if not discount:
        raise HTTPException(status_code=404, detail="Descuento no encontrado")
    db.query(models.DiscountItem).filter(models.DiscountItem.discount_id == discount_id).delete()
    db.delete(discount)
    db.commit()
    return {"message": "Descuento eliminado"}
