from tests.models.store import Store
from tests.models.user import User
from tests.service.serviceuser import ServiceUser


service = ServiceUser()
resultado = service.add_user("Emerson", "Santiago")
print(resultado)
print(service.store.bd[0].name)
