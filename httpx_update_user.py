import email

import httpx
from tools.fakers import get_random_email


create_user_upload = {
  "email": get_random_email(),
  "password": "string",
  "lastName": "string",
  "firstName": "string",
  "middleName": "string"
}

create_new_user = httpx.post("http://localhost:8000/api/v1/users",json=create_user_upload)
create_new_user_data = create_new_user.json()
user_id = create_new_user_data['user']['id']

print(f"New user id:{user_id}")
print(create_new_user.status_code)



login_payload = {
    "email": create_user_upload['email'],
    "password": create_user_upload['password']
}

login_new_user_response = httpx.post("http://localhost:8000/api/v1/authentication/login", json=login_payload)
login_new_user_response_data = login_new_user_response.json()
print(login_new_user_response_data)
login_user_access_token = login_new_user_response_data['token']['accessToken']

print(login_new_user_response.status_code)
print(f"New access token:{login_user_access_token}")


patch_headers = {"Authorization": f"Bearer {login_user_access_token}"}
patch_new_upload = {
    "email": get_random_email(),
    "lastName": "stringGGG",
    "firstName": "GGGstring",
    "middleName": "stringGGG"
}
patch_user_response = httpx.patch(f"http://localhost:8000/api/v1/users/{user_id}", headers=patch_headers, json=patch_new_upload)
patch_user_response_data = patch_user_response.json()

print(patch_user_response.status_code)
print(patch_user_response.json())













