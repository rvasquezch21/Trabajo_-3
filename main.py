from fastapi import FastAPI

# Crear una instancia de la aplicación FastAPI
app = FastAPI()

# Definir una ruta de prueba
@app.get("/")
def read_root():
    return {"message": "¡Hola, mundo!"}

# Crear una ruta con un parámetro
@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "q": q}

# Ejecutar la aplicación
# Para esto, se utiliza Uvicorn, que servirá la app en el servidor.
# Esto lo ejecutarás desde la terminal, no dentro del código:
# uvicorn main:app --reload
