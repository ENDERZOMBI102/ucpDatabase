import sqlite3 as sql
from pprint import pprint
from pathlib import Path

class Database:

    db = sql.connect('db')
    cursor = db.cursor()

    def __init__(self):
        #check if the packages table exists, and, if not, create it 
        self.cursor.execute("SELECT name FROM sqlite_master WHERE type = 'table' AND name = 'packages';")
        if self.cursor.fetchone() == 0:
            self.createTable()
    
    #create table packages
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

    #add a package
    def addPackage(self, package: List[str]):
        self.cursor.execute("INSERT INTO packages (identifier, name, authors, description, icon_url, repo) VALUES \
            (?, ?, ?, ?, ?, ?)", package)
    
    def commit(self):
        self.db.commit()

    #read all packages
    def getAll(self):
        self.cursor.execute('SELECT * FROM packages')
        return self.cursor.fetchall()

    #read all packages with the name starting wity NAME
    def getPackageFromName(self, name: str):
        self.cursor.execute('SELECT * FROM packages WHERE name LIKE ?', [name])
        return self.cursor.fetchall()
    
    # read all packages with the same author
    def getPackageFromAuthor(self, author: str):
        self.cursor.execute('SELECT * FROM packages WHERE authors LIKE ?', [author])
        return self.cursor.fetchall()

    # read all packages with the id starting with IDENTIFIER
    def getPackageFromIdentifier(self, identifier: str):
        self.cursor.execute('SELECT * FROM packages WHERE identifier LIKE ?', [identifier])
        return self.cursor.fetchall()

    def deletePackage(self, identifier: str):
        self.cursor.execute('DELETE FROM packages WHERE identifier = ?', [identifier])




