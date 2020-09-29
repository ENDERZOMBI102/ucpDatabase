from fastapi import APIRouter, Response
from starlette import status

from database import Database

router = APIRouter()


@router.get('/api/packages')
async def getAll():
	return Database.instance.getAll()


@router.get('/api/packages/from')
async def getFrom(response: Response, identifier: str = None, name: str = None, author: str = None):
	if identifier is not None:
		return Database.instance.getPackageFromIdentifier(identifier)
	elif name is not None:
		return Database.instance.getPackageFromName(name)
	elif author is not None:
		return Database.instance.getPackageFromAuthor(author)
	else:
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




@router.delete('/api/packages/{package_id}')
async def deletePackage(package_id: str):
	Database.instance.deletePackage(package_id)