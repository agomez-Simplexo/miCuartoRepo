import os
from typing import Union
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

@app.get("/familia")
def get_familia():
    rows = ["Amin", "Marce", "Miranda"]
    return rows

@app.get("/superheroesDC")
def get_superheroes():
    rows = ["Superman", "Batman", "Flash", "Linterna Verde", "Mujer maravilla", "Aquaman", "Shazam", "Cyborg"]
    return rows

@app.get("/superheroesMarvel")
def get_superheroes():
    rows = ["Spiderman", "Ironman", "Thor", "Blackwido", "Solder America"]
    return rows

@app.get("/cursos")
def get_cursos():
    rows = ["Docker", "Bash", "Linux", "Ingles", "Javascripts"]
    return rows

@app.get("/nombres")
def get_nombres():
    rows = ["Angel", "lili", "Ingrid", "Dolores", "Jose"]
    return rows