from fastapi import FastAPI
from starlette.responses import RedirectResponse
from data import Data

app = FastAPI()

@app.get("/")
def redirect():
    return RedirectResponse('/docs')

@app.get("/resto/{id}")
def get_resto(id):
    data = Data.get_resto(id)
    return {'data': data} 

@app.get("/resto/inspec/{id}")
def get_resto_inspec(id):
    data = Data.get_resto_inspec(id)
    return {'data': data} 

@app.get("/resto_by_type/{type}")
def get_resto_names(type):
    data = Data.get_resto_names(type)
    return {'data': data}

@app.get("/top10/{grade}")
def get_top10(grade):
    data = Data.get_top10(grade)
    return {'data': data}