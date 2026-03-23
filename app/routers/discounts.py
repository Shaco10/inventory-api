from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from .. import crud, schemas
from ..database import get_db

router = APIRouter(prefix="/discounts", tags=["Discounts"])

@router.post("/", response_model=schemas.DiscountResponse)
def create_discount(discount: schemas.DiscountCreate, db: Session = Depends(get_db)):
    return crud.create_discount(db, discount)

@router.get("/", response_model=list[schemas.DiscountResponse])
def get_discounts(db: Session = Depends(get_db)):
    return crud.get_discounts(db)

@router.delete("/{discount_id}")
def delete_discount(discount_id: int, db: Session = Depends(get_db)):
    return crud.delete_discount(db, discount_id)