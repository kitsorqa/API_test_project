import json
import random
from faker import Faker

faker = Faker()


class UserPayloads:
    def create_user(self):
        user_data = {
            "id": random.randint(1, 999999),
            "username": faker.user_name(),
            "firstName": faker.first_name(),
            "lastName": faker.last_name(),
            "email": faker.email(),
            "password": faker.password(length=7),
            "phone": faker.phone_number(),
            "userStatus": random.randint(1, 999999)
        }
        return user_data

    def create_array_of_users(self, count_of_users_object):
        list_of_users = []
        for _ in range(count_of_users_object):
            list_of_users.append(self.create_user())
        return list_of_users

    def change_user(self, id=312312, username='mary73', fisrtName='string', lastName='string', email='string',
                    password='string', phone='string', userStatus=1):
        user_data = {
            "id": id,
            "username": username,
            "firstName": fisrtName,
            "lastName": lastName,
            "email": email,
            "password": password,
            "phone": phone,
            "userStatus": userStatus
        }
        return user_data