from pydantic.validators import *
from pydantic import BaseModel
from typing import *
from starlette.datastructures import URL

class MBasePackage(BaseModel):
    
    identifier: str
    name: str
    authors: List[str]
    description: str
    icon_url: str
    repo: str


class MBeePackage(MBasePackage):
    
    tags: EBeeTags

class MManipulatorPackage(MBasePackage):
    
    tags: EManipulatorTags


class EBeeTags(Enum):
    
    DECORATION: 0


class EManipulatorTags(Enum):
    PLUGIN: 0
