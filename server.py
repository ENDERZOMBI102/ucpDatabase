from servepy import *
from handler import *


app = App()

router = Router()
router.get("/Database/get/", db.get)
router.post("/Database/create/", db.createPackage)
app.use(router)
app.listen(port=3000, callback=server.listening)