from typing import List

from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

from . import crud, models, schemas
from .database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


# Dependency
def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()


@app.get("/")
def main():
    return {"Hello world"}


@app.post("/orders/", response_model=schemas.Order)
def create_user(order: schemas.Order, db: Session = Depends(get_db)):
    return crud.create_order(db=db, order=order)


@app.get("/orders/", response_model=List[schemas.Order])
def read_orders(skip: int = 0, lim: int = 100, db: Session = Depends(get_db)):
    users = crud.get_orders(db, skip=skip, limit=lim)
    return users


@app.get("/orders/{order_id}", response_model=schemas.Order)
def read_order(order_id: int, db: Session = Depends(get_db)):
    db_order = crud.get_order(db, order_id=order_id)
    if db_order is None:
        raise HTTPException(status_code=404, detail="Order not found")
    return db_order
