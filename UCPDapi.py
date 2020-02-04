from requests import *# sending/reciving things from the web
from json import *# manage json
import base64 # for encrypt a text a image or data to text
import PIL# for managing images

class ucpd:
    r"""
    	this is the main class, used for much of the api work
	"""
    def __init__(self):
        try:
            self.database = get("https://github.com/ENDERZOMBI102/ucpDatabase/raw/master/Database.json").content
        except:
            raise ConnectionError("Failed to download the database!")
        try:
            self.database = loads(self.database)
        except:
            raise ValueError("The downloaded database isn't valid!")
        

    def __iter__(self):
        return self
    
    def __next__(self):
        return next(self.database)

if __name__ == "__main__":
    db = ucpd()
    for i in db:
        print(i)