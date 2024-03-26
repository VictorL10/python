import requests

# url = "http:my_url/get_method?name=Andrei&age=32"
print(url)
result = requests.get(url)
print("Статус код : "+ str(result.status_code))
assert 200 == result.status_code
if result.status_code == 200:
    print("Успешно!!!")
else:
    print("Провал!!!")
result.encoding = 'utf-8'
print(result.text)