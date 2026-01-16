import httpx

payload = {
     "email": "user777@example.com",
     "password": "string"
}
response = httpx.post("http://localhost:8000/api/v1/authentication/login", json=payload)
response_data = response.json()
login_access_token = response_data['token']['accessToken']
print(login_access_token)

get_user_headers = {"Authorization": f"Bearer {login_access_token}"}
response = httpx.get("http://localhost:8000/api/v1/users/me", headers=get_user_headers)

print(response.json())
print(response.status_code)