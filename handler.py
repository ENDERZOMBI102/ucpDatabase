from servepy import *
from json import dumps
from threading import Thread

class handler(Thread):
    def get(req, res):
        with open('./Database.json', 'r') as file:
            tfile = file.read()
            res.status(200).set('Content-Type', 'application/json').send( tfile )
              
    def createPackage(req, res):
        # setup the response dict with default values
        response = {"status": 200,"validUserAgent": True, "validContentType": True, "secure": True, "message": "", "True?": "True"}
        # check the user agent, if the request isn't done by requests set the validUserAgent flag to false
        # and the status to 406 (invalid request)
        if ("python-requests") not in req.headers['USER-AGENT']:
            response["validUserAgent"] = False
            response["status"] = 406
            response["message"] = response["message"] + "\n Invalid user agent."
        # check the content type, if isn't application/json set the validContentType flag to false
        # and the status to 406 (invalid request)
        if req.headers["CONTENT-TYPE"] != "application/json":
            response["validContentType"] = False
            response["status"] = 406
            response["message"] = response["message"] + "\n The content type in the request isn't json."
        # check if the protocol is https, if it isn't, set the secure flag to false
        # and the status to 406 (invalid request)
        if req.headers["X-FORWARDED-PROTO"] != "https":
            response["secure"] = False
            response["status"] = 406
            response["message"] = response["message"] + "\n The protocol used isn't https."
        # add the package to the database
        try:
            reqData = req.content
        except err:
            response["status"] = 406
            response["validContentType"] = False
            response["message"] = response["message"] + "\n There's no json in the request."
        if response["status"] == 200:
            with open('./Database.json', 'r') as file:
                data = json.dumps(file)
                for



        # send the response to the client
        res.status(response["status"]).set('Content-Type', 'application/json').send( response )

        

class server:
    def listening():
        print("server online\nlistening on 3000")