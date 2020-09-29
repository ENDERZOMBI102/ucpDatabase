import sqlite3 as sql
from pprint import pprint
from pathlib import Path
import re
from typing import List, Union, Dict

from models import MBasePackage


sanitized: Dict[str, str] = {
	'\'': '%27',
	'%': '%25',
	'&': '%26',
	'\\': '%5C',
	'=': '%3D',
	'$': '%24'
}


class Database:

	instance = None

	db = sql.connect('../db')
	cursor = db.cursor()

	def __init__(self):
		Database.instance = self
		# check if the packages table exists, and, if not, create it
		self.cursor.execute("SELECT name FROM sqlite_master WHERE type='table' ORDER BY name;")
		if len( self.cursor.fetchall() ) == 0:
			self.createTable()

	# create table packages
	def createTable(self):
		self.cursor.execute('''CREATE TABLE packages (
			identifier TEXT not null,
            name TEXT not null,
            authors TEXT not null,
            description TEXT,
            icon_url TEXT,
            repo TEXT not null,
            PRIMARY KEY(identifier),
            UNIQUE(identifier, name)
        );''')
		self.db.commit()

	def rollback(self):
		self.db.rollback()

	# add a package
	def addPackage( self, package: MBasePackage ):
		serializedPackage: List[str] = [
			sanitize( package['identifier'] ),
			sanitize( package['name'] ),
			sanitize( ','.join( package['authors'] ) ),
			sanitize( package['description'] ),
			sanitize( package['icon_url'] ),
			sanitize( package['repo'] )
		]
		self.cursor.execute(
			"INSERT INTO packages (identifier, name, authors, description, icon_url, repo) VALUES (?, ?, ?, ?, ?, ?)",
			serializedPackage
		)

	def commit(self):
		self.db.commit()

	# read all packages
	def getAll(self):
		self.cursor.execute( 'SELECT * FROM packages' )
		return prettify( self.cursor.fetchall() )

	# read all packages with the name starting with NAME
	def getPackageFromName(self, name: str):
		self.cursor.execute( 'SELECT * FROM packages WHERE name LIKE ?', [ '%'+sanitize(name)+'%' ] )
		return prettify( self.cursor.fetchall() )

	# read all packages with the same author
	def getPackageFromAuthor(self, author: str):
		self.cursor.execute( 'SELECT * FROM packages WHERE authors LIKE ?', [ '%'+sanitize(author)+'%' ] )
		return prettify( self.cursor.fetchall() )

	# read all packages with the id starting with IDENTIFIER
	def getPackageFromIdentifier(self, identifier: str):
		self.cursor.execute( "SELECT * FROM packages WHERE identifier LIKE ?", [ '%'+sanitize(identifier)+'%' ] )
		return prettify( self.cursor.fetchall() )

	def deletePackage(self, identifier: str):
		identifier = sanitize(identifier)
		self.cursor.execute( 'SELECT COUNT(*) FROM packages WHERE identifier = ?', [ identifier ] )
		if len( self.cursor.fetchall() ) == 0:
			return False
		self.cursor.execute( 'DELETE FROM packages WHERE identifier = ?', [ identifier ] )


def prettify(data: List[ List[str] ]) -> List[MBasePackage]:
	# prepare data
	done: List[MBasePackage] = []
	i: List[ str ]
	# cycle in the lists
	for i in data:
		done.append(
			MBasePackage(
				identifier=i[0],
				name=i[1],
				authors=i[2].split(','),  # as sql doesn't store list or arrays, we use a ','-unified list
				description=i[3],
				icon_url=i[4],
				repo=i[5]
			)
		)
	return done


def sanitize(sanitizeme: str) -> str:
	for i in sanitized.keys():
		sanitizeme = sanitizeme.replace( i, sanitized[i] )
	return sanitizeme
