from faker import Faker
from uuid import uuid4
fake = Faker()

# first, import a similar Provider or use the default one
from faker.providers import BaseProvider

# create new provider class. Note that the class name _must_ be ``Provider``.
class Quote(BaseProvider):
    def Service_Request_Num(self):
        return str(uuid4())

# then add new provider to faker instance
fake.add_provider(Quote)

# now you can use:
for a in range(4):
    print(fake.Service_Request_Num())

