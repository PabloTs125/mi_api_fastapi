from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from app.db import get_db
from app import models
from app.database import engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Bienvenido a la API de nombres"}

@app.get("/nombres")
def get_nombres(db: Session = Depends(get_db)):
    nombres = db.query(models.Nombre).all()
    return [{"id": n.id, "nombre": n.nombre, "apellidos": n.apellido} for n in nombres]