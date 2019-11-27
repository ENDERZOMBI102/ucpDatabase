from servepy import *
class db:
    def get(req, res):
        with open('./Database.json', 'r') as file:
            tfile = file.read()
            res.status(200).set('Content-Type', 'application/json').send( tfile )
              
    def createPackage(req, res):
        print(req)

class server:
    def listening():
        print("server online\nlistening on 3000")