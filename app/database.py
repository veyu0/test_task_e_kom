from tinydb import TinyDB, Query

db = TinyDB('./db.json', indent=4)
Forms = Query()


def insert():
    db.insert_multiple(
        [
            {
                "name": "First Form",
                "text": "Hello",
                "email": "faith.veyu0@gmail.com",
                "phone": "+79824076521",
                "date": "06.01.2023"
            },
            {
                "name": "Users Form",
                "user_name": "Alex",
                "user_email": "alex144@mail.ru",
                "user_phone": "+79223300089",
                "creation_date": "01.01.2023"
            },
            {
                "name": "Orders Form",
                "order_name": "IPhone 14",
                "user_email": "info@mail.ru",
                "user_phone": "+79224400089",
                "creation_date": "03.01.2023"
            }
        ]
    )
