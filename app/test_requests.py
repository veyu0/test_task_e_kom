import requests


def test_requests():
    test1 = requests.post('http://127.0.0.1:8000/get_form/text=Hello&phone=+79824076521')
    print(test1.json())
    test2 = requests.post('http://127.0.0.1:8000/get_form/user_name=Alex&creation_date=01.01.2023')
    print(test2.json())
    test3 = requests.post('http://127.0.0.1:8000/get_form/order_name=IPhone 14&user_email=info@mail.ru')
    print(test3.json())
    test4 = requests.post('http://127.0.0.1:8000/get_form/text=Hello&phone=+7000000000')
    print(test4.json())


test_requests()