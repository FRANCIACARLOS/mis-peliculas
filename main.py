from fastapi import FastAPI #importa FastAPI
#Crear una explicación web
app =FastAPI() #Crea una instancia de la clase FastAPI
app.title="Comida saludable " #cambiar el titulo al FastAPI
@app.get('/', tags=["Home"]) #Definimos una ruta
#creamos una funcion que nos permita disparar un mensaje y retorne "hola mundo"
def message(): #definimos una función de la ruta
    return "Hello world" #Devolvemos un string en la respuesta de la ruta
# Ejecutar la terminal 

# peliculas
from fastapi import FastAPI 
from fastapi.responses import HTMLResponse

app = FastAPI() #Crea una instancia de la clase FastAPI 
app.title = "Mi aplicación de películas favoritas con FastAPI"
app.version = "0.0.1"

movies_list = [
    {
        "id": 1,
        "title": "Deadpool y Wolverne",
        "overview": "Deadpool y Wolverine se unen en una aventura peligrosa",
        "year": 2024,
        "rating": 8.5
    },
        {
        "id": 2,
        "title": "Los vengadores",
        "overview": "Los vengadores se unen en una aventura peligrosa",
        "year": 2024,
        "rating": 8.5
    }
]

@app.get('/', tags=["Home"])#Definimos una ruta
def message(): # Definimos una función de la ruta
    return HTMLResponse ('<h1>Hello world</h1>') # Devolvemos un string en la respuesta de la ruta

@app.get('/movies', tags=["Movies"])#Definimos una ruta de la clase FastAPI
def get_movies(): 
    return movies_list

@app.get('/movies/{id}', tags=["Movies"])#Definimos una ruta de la clase FastAPI
def get_movie(id: int):
    for item in movies_list:
        if item['id'] == id:
            return item
    return[]
