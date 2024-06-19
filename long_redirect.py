import requests

response = requests.get("https://playground.learnqa.ru/api/long_redirect", allow_redirects=True)
first_response = response.history[0]
first_response_1 = response.history[1]
second_response = response

print(first_response.url)
print(first_response_1.url)
print(second_response.url)