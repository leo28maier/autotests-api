import httpx

from tools.fakers import get_random_email

payload_create_user = {

  "email": get_random_email(),
  "password": "string",
  "lastName": "string",
  "firstName": "string2",
  "middleName": "string3"
}
create_new_user = httpx.post("http://localhost:8000/api/v1/users", json=payload_create_user)
create_new_user_data = create_new_user.json()
create_user_id = create_new_user_data['user']['id']
print(f"Created user id:{create_user_id}")

payload_login = {
    "email": payload_create_user["email"],
    "password": payload_create_user["password"]
}

login_user_response = httpx.post("http://localhost:8000/api/v1/authentication/login", json=payload_login)
login_user_response_data = login_user_response.json()
login_user_token = login_user_response_data['token']['accessToken']
print(f"Login user token:{login_user_token}")


create_file_header = {
    "Authorization": f"Bearer {login_user_token}"
}

create_file_response = httpx.post(
    "http://localhost:8000/api/v1/files",
    data = {"filename": "fototest.PNG", "directory": "courses"},
    files = {"upload_file": open('./testdata/files/fototest.png', 'rb')},
    headers=create_file_header
)

create_file_response_data = create_file_response.json()
print(create_file_response_data)




