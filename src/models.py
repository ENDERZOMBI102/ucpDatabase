from pydantic.validators import *
from pydantic import BaseModel
from typing import *


class EBeeTags(Enum):
	DECORATION: 0
	MECHANICS: 1
	STYLES: 3
	EXTENSION: 4


class EManipulatorTags(Enum):
	PLUGIN: 0
	THEME: 1


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
