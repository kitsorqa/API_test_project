import random
from random import randint

class StorePayloads:
    statuses = ["placed", "approved", "delivered"]
    create_order = {
      "id": randint(0, 999999),
      "petId": randint(0, 999999),
      "quantity": randint(0, 999999),
      "shipDate": "2025-04-23T19:29:45.907Z",
      "status": random.choice(statuses),
      "complete": randint(0, 2)
}