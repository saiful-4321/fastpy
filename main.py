from fastapi import FastAPI
app = FastAPI()

@app.get('/')
def index():
    return { 
        'data': {
            'name': 'Saiful', 
            'designation': 'SDE'
        },
        'status': 200
    }