import logging

logging.basicConfig(filename='example.log', encoding='utf-8', level=logging.INFO)


class User:
    def __init__(self, user_name, user_age, user_email, user_password):
        self.name = user_name
        self.email = user_email
        self.age = user_age
        self.password = user_password

        logging.info('Created User: {} - {} - {}'.format(self.name, self.age, self.email))

    def change_user_name(self, updated_name):
        assert not updated_name.isdigit()
        self.name = updated_name

    def change_user_email(self, updated_email):
        assert '@' in updated_email
        self.email = updated_email

    def change_user_age(self, updated_age):
        assert 0 < updated_age < 150
        self.age = updated_age

    def change_user_password(self, updated_password):
        self.password = updated_password
        assert len(self.password) >= 8


user1 = User('Aidar', 18, 'test123@gmail.com', 'spotify1234')
# user1.change_user_password('we345')
# user1.change_user_age(345)
