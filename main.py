from fastapi import FastAPI
app = FastAPI()

@app.get('/')
def index():
    return { 
        'page': 'index',
        'data': {
            'name': 'Saiful', 
            'designation': 'SDE'
        },
        'status': 200
    }

@app.get('/about')
def about():
    return {
        'page': 'about',
        'status': 200,
        'data': {
            'name': 'saiful islam',
            'from': 'lakshmipur'
        }
    }