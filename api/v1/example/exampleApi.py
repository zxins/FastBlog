from fastapi import APIRouter

router = APIRouter()

@router.get('/example')
async def example():
    return {'hello': 'example'}

@router.post('/example')
async def create_example(name: str):
    pass