from fastapi import APIRouter, Response
from starlette import status

from database import Database

router = APIRouter()


@router.get('/api/packages')
async def getAll():
	return Database.instance.getAll()


@router.get('/api/packages/from')
async def getFrom(response: Response, identifier: str = None, name: str = None, author: str = None):
	# do we have parameters?
	if identifier is None and name is None and author is None:
		# nope
		response.status_code = status.HTTP_400_BAD_REQUEST
		return {
			'error': 'no_parameters',
			'message': 'expected at least one parameter',
			'validParameters': [
				'identifier',
				'name',
				'author'
			]
		}
	return Database.instance.getPackageFromIdentifier(identifier)
