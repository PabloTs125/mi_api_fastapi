from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from app.database import engine, Base
from app import models
from app.db import get_db

app = FastAPI()

# Crea las tablas al iniciar si no existen
Base.metadata.create_all(bind=engine)

@app.get("/")
def home():
    return {"message": "Bienvenido a la API de nombres"}

@app.get("/nombres")
def get_nombres(db: Session = Depends(get_db)):
    nombres = db.query(models.Nombre).all()
    return [{"id": n.id, "nombre": n.nombre, "apellidos": n.apellido} for n in nombres]