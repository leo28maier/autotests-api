import httpx

from tools.fakers import get_random_email

new_user_payload = {
  "email": get_random_email(),
  "password": "Qazwsx123!",
  "lastName": "Kos",
  "firstName": "Poz",
  "middleName": "Vich"
}
create_user_response = httpx.post("http://localhost:8000/api/v1/users", json=new_user_payload)
create_user_response_data = create_user_response.json()
print(create_user_response.status_code)
print(f"created_user:{create_user_response_data}")


auth_payload = {
  "email": new_user_payload["email"],
  "password": new_user_payload["password"]
}

auth_response = httpx.post("http://localhost:8000/api/v1/authentication/login", json= auth_payload)
auth_response_data = auth_response.json()

print(f"Auth_user:{auth_response_data}")

get_user_headers = {"Authorization": f"Bearer {auth_response_data['token']['accessToken']}"
}
response = httpx.get(f"http://localhost:8000/api/v1/users/{create_user_response_data['user']['id']}",headers=get_user_headers)
get_user_data = response.json()

print(f"get_user_data:{get_user_data}")
 