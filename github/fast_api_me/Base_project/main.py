from fastapi import FastAPI

app=FastAPI()

@app.get("/")
def index():
    return "Welcome to Virtual World"

@app.get("/about")
def about():
    return {"data":{"name":"Ravi Ranjan","Address":"DarkWorld"}}


@app.get("/blog/{id}")
# def show(id):
#     return{"data":id}
def show(id:int):
    return {"data":id}
@app.get("/blog/{id}/comments")
def comments(id):
    return {"data":{"1","3"}}
