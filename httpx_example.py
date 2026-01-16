import httpx

# response = httpx.get("https://jsonplaceholder.typicode.com/todos/1")
#
# print(response.status_code)
# print(response.json())
#
#
# data = {
#     "title": "New task",
#     "completed": False,
#     "UserId": 1
# }
#
# response = httpx.post("https://jsonplaceholder.typicode.com/todos", json=data)
# print(response.status_code)
# print(response.request.headers)
# print(response.json())
#
#
# data = {
#     "username": "admin",
#     "password": "123456"
# }
# response = httpx.post("https://httpbin.org/post", data=data)
# print(response.status_code)
# print(response.json())
#
#
# headers = {"Authorization": "Bearer my_token"}
# response = httpx.get("https://httpbin.org/get", headers=headers)
#
# print(response.status_code)
# print(response.request.headers)
# print(response.json())

# используем query param

# params = {
#     "userId": 1,
#     "complete": False
# }
# response = httpx.get("https://jsonplaceholder.typicode.com/todos", params=params)
#
#
# print(response.status_code)
# print(response.url)
# print(response.json())
#
#
# files = {
#     "file": ("example.txt", open("example.txt", "rb"))
# }
# response = httpx.post("https://httpbin.org/post", files=files)
# print(response.status_code)
# print(response.url)
# print(response.json())

# with httpx.Client() as client:
#     response1 = client.get("http://httpbin.org/get")
#     response2 = client.get("http://httpbin.org/get")
#
# print(response1.json())
# print(response2.text)
#
# client = httpx.Client(headers={"User-Agent": "Mozilla/3.0", "Authorization": "my token"})
# response = client.get("http://httpbin.org/get")
#
# print(response.text)

# try:
#     response = httpx.get("http://httpbin.org/get/invalid-url")
#     response.raise_for_status()
# except httpx.HTTPStatusError as e:
#     print(f"неуспешный ответ: {e}")

try:
    response = httpx.get("http://httpbin.org/delay/5", timeout=2)
    response.raise_for_status()
except httpx.ReadTimeout as e:
    print(f"Задержка больше 2 сек: {e}")