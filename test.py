from fastapi import FastAPI

inst = FastAPI()

#to start the server
#here command will be uvicorn filename:fastApiInstanceName --realod
@inst.get('/')
def index():
    return "index here"