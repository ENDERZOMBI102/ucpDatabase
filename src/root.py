from fastapi import APIRouter

router = APIRouter()


@router.get('/')
async def get_root():
	return {'message': 'this endpoint will be used for a future frontend'}