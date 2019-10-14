from requests import *# sending/reciving things from the web
import json # manage json
import base64 # for encrypt a text a image or data to text
import PIL# for managing images

class status:
	data=''
	'''
		this class is all about checking the status of a service.
		with this is possible to check: webhook, website, bot, api and  server status, just call
		the right function and get the response (maintenance, online or offline)
		info() is used to obtain server infos
	'''
	def server():
		data=get('https://ucpdatabase.glitch.me/status/server')
		return data.content
	
	def api():
		data=get('https://ucpdatabase.glitch.me/status/api')
		return data.content
	
	def webhook():
		data=get('https://ucpdatabase.glitch.me/status/webhook')
		return data.content
	
	def info():
		data=get('https://ucpdatabase.glitch.me/status/status')
		return data.content

class ucpd:
	'''
		this is the main class, used for much of the api work
	'''
	def getfile(whatfile):
		data=get('https://ucpdatabase.glitch.me/db/files/'+whatfile)
		return data.content
	def getimage(name):
		data=get('https://ucpdatabase.glitch.me/db/images/'+name+'.b64')
		base64
		return image
	def getdata(whatdata):
		data='f'
		
class bmpackage:
	'''
	this class rappresents a bee manipulator package
	use a dict cause is faster to convert to json, and for faster accessibility of curse
	'''
	def __init__(self, info):
		print('r')

class package:
	'''
	this class rappresents a BEE2.4 package
	using a dict for reasons
	this is how a package look to bee manipulator
	'''
	def __init__(self,info):
		info.json()
		self.name = info['name']
		self.repo_url = info['repo_url']
		self.author = info['author']
		self.co_author = info['co_author']
		self.version = info['version']
		self.file_name = info['file_name']
		self.direct_download = False
		api_latest_url = info['api_latest_url']
	'''
	with this function we check if the package info are correct
	'''
	def check(self):
		 if(self.repo_url=="gdrive" or self.repo_url=="drive" or self.repo_url=="dropbox" or self.repo_url==""):
		 	self.direct_download=True
		 else:
		 	self.direct_download=False