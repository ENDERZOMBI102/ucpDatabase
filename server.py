from servepy import *
from handler import *


app = App()
router = Router()

router.get("/API/get/", db.get) # send the client the database
router.post("/API/create/", db.createPackage) # submit a package to the database



app.use(router)
app.listen(port=3000, callback=server.listening)