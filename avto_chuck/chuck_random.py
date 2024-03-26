import requests

class Test_new_joke():
    """Создание"""

    def __init__(self):
        pass

    def test_create(self):
        """Отправка имени и возраста"""

        # url = "my_url/object_info_1?name=Victor&age=32&weight=80"
        print(url)
        result = requests.get(url)
        print("Статус код : " + str(result.status_code))
        assert 200 == result.status_code
        if result.status_code == 200:
            print("Успешно!!!")
        else:
            print("Провал!!!")
        result.encoding = 'utf-8'
        print(result.text)

        check = result.json()
        check_info = check.get("name")
        print(check_info)
        # assert check_info == "Victor"
        # print("Верное имя")


random_joke = Test_new_joke()
random_joke.test_create()