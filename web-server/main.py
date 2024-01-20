import store
#Libreria de fastapi
from fastapi import FastAPI
#Libreria para tener response de html
from fastapi.responses import HTMLResponse

#Nombre de la aplicacion para ejecutar
app = FastAPI()

#Funcion para obtener un listado en servidor
@app.get('/')
def get_list():
    return [1,2,3,4,5]

@app.get('/contact', response_class=HTMLResponse)
def get_contact():
    return """
        <h1>Hola soy una pagina en blanco</h1>
        <p>Este es el primer paso en usar una libreria backend</p>
    """
    


def run():
    store.get_categories()

if __name__ == '__main__':
    run()