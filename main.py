from typing import Optional
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

@app.get('/blogs')
def filtered_blogs(limit: int = 10, published: bool = True, sort: Optional[str] = ''): 
    if published:
        return { 'page': f'{limit} published blogs from the {sort} list' }
    else:
        return { 'page': f'{limit} blogs from the {sort} list' }
    

@app.get('/blogs/unpublished')
def unpublished(): 
    return {
        'page': 'Unpublished blog',
        'data': {
            'name': 'showing all unpublished blog'
        }
    }


@app.get('/blogs/{id}')
def show_blog(id: int):
    return {
        'page': 'single blog',
        'id': id,
        'data': {
            'title': 'blog 1',
            'details': 'This is the details for blog no: ' + str(id)
        }
    }

@app.get('/blogs/{id}/comments')
def comments(id: int): 
    return {
        'page': 'comments',
        'blog': {
            'id': id,
            'title': 'title for blog' + str(id)
        },
        'comments': {
            'data': [
                { 
                    'id': 1,
                    'comment': 'nice blog'
                }
            ]
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