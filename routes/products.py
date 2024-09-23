from datetime import timedelta
from typing import List
from fastapi import APIRouter, Depends, HTTPException, Response
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from config.db import conn, SessionLocal, get_db
from passlib.context import CryptContext
from models.db_p import Vehiculos, Users, Model_Auto, Category
from models import db_p
from sqlalchemy.orm import Session
from modelo.m_pro import vh
from modelo.m_user import Token, Users, Login
from modelo.token import create_access_token
import json

VH = APIRouter()


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


@VH.get("/products", response_model=List[vh])
def getproduct(db: Session = Depends(get_db)):
    product = db.query(Vehiculos).all()
    return product


@VH.post("/products")
def getnew(
    vhs: vh,
    db: Session = Depends(get_db),
):
    existe = db.query(Vehiculos).filter(Vehiculos.name == vhs.name).first()
    if existe is None:
        db_item = Vehiculos(**vhs.model_dump())
        db.add(db_item)
        db.commit()
        db.refresh(db_item)
    else:
        raise HTTPException(
            status_code=404, detail="product with this name already exists "
        )

    return {"data": db_item}


@VH.get("/products/{id}")
def index(id: int, db: Session = Depends(get_db)):
    vh = db.query(Vehiculos).filter(Vehiculos.id == id).first()
    if vh is None:
        raise HTTPException(status_code=404, detail="Product not found")
    return vh


@VH.get("/relacion", response_model=List[vh])
def index(db: Session = Depends(get_db)):
    query = (
        db.query(Vehiculos, Category, Model_Auto)
        .join(Category, Vehiculos.category_id == Category.id)
        .join(Model_Auto, Vehiculos.modelo_id == Model_Auto.id)
        .all()
    )

    # Iterar y mostrar los resultados
    resultados = [
        {
            "id": vehiculo.id,
            "name_product": vehiculo.name_product,
            "category": categoria.name,
            "modelo": modelo.modelo,
        }
        for vehiculo, categoria, modelo in query
    ]

    # Serializar la respuesta usando jsonable_encoder y devolver como JSONResponse
    return JSONResponse(content=jsonable_encoder(resultados))


@VH.delete("/products/{id}")
def delete(id: int, db: Session = Depends(get_db)):
    vh = db.query(Vehiculos).filter(Vehiculos.id == id)
    if vh.first() == None:
        raise HTTPException(status_code=404, detail="Product not found")

    vh.delete()
    db.commit()
    raise HTTPException(status_code=200, detail="Product delete")


@VH.put("/products/{id}", response_model=vh)
def index(id: int, update_vhs: vh, db: Session = Depends(get_db)):
    vh_query = db.query(Vehiculos).filter(Vehiculos.id == id)
    post_vh = vh_query.first()
    if not vh_query.first():
        raise HTTPException(status_code=404, detail="Product not found")

    vh_query.update(update_vhs.model_dump(), synchronize_session=False)
    db.commit()
    db.refresh(post_vh)
    return post_vh


@VH.post("/usuario", response_model=Users)
def get_user(users: Users):
    existe = conn.execute(
        user.select().where(user.c.username == users.username)
    ).first()
    if existe:
        return JSONResponse("usuario ya se encuentra en uso")

    new_users = {"username": users.username}
    new_users["password"] = pwd_context.hash(users.password.encode("utf-8"))
    result = conn.execute(user.insert().values(new_users))
    query = conn.execute(user.select().where(user.c.id == result.lastrowid)).first()
    conn.commit()
    return query


@VH.post("/usuario/login", response_model=Login)
def get_user(users: Login):

    user_db = conn.execute(
        user.select().where(user.c.username == users.username)
    ).first()

    if not user_db or not pwd_context.verify(users.password, user_db.password):
        return JSONResponse("Incorrect username or password")
        raise HTTPException(409, "Incorrect username or password")

    access_token = create_access_token(data={"sub": users.username})
    token = {"access_token": access_token, "token_type": "bearer"}
    return JSONResponse(token)


# raise HTTPException(status_code=200, detail="login")
