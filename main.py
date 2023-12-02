from fastapi import FastAPI
app = FastAPI()

@app.get('/')
def index():
    return { 
        'page': 'index',
        'title': 'blog list',
        'data': {
            'name': 'Saiful', 
            'designation': 'SDE'
        },
        'status': 200
    }

@app.get('/blogs/{id}')
def show_blog(id):
    return {
        'page': 'single blog',
        'id': id,
        'data': {
            'title': 'blog 1',
            'details': 'This is the details for blog no: ' + id
        }
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