from fastapi.testclient import TestClient
from main import app
from tests.setUp import TestSetUp

config = TestSetUp()
client = TestClient(app)

#def test01_ifTheAuthorizerCanScanTheTicketThenTheStatusCodeIs200
#def test02_ifTheAuthorizerCantScanTheTicketBecauseEventDoesntExistTheStatusCodeIs403
#def test03_ifTheAuthorizerCantScanTheTicketBecauseHeDoesntHasPermissionThenTheStatusCodeIs403