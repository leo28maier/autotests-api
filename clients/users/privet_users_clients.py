from clients.api_client import APIClient
from httpx import Response
from typing import TypedDict

class UpdateUserRequest(TypedDict):
    """
    description request structure for update user request
    """
    email: str | None
    password: str | None
    lastName: str | None
    firstName: str | None
    middleName: str | None

class PrivetUsersClients(APIClient):
    """
    клиент работы с API
    """
    def get_user_me_api (self) -> Response:
        """
        метод получения текущего пользователя
        :return: response object текущего пользователя
        """
        return self.get('/api/v1/users/me')

    def get_user_api (self, user_id: str) -> Response:
        """
        Метод получения пользователя по идентификатору
        :param user_id: user id
        :return: response object в вииде httpx.response
        """
        return self.get('/api/v1/users/{user_id}')

    def update_user_api (self, user_id: str, request: UpdateUserRequest) -> Response:
        """
        Метод patch пользователя по идентификатору
        :param user_id: user id
        :param request: dict email, password, lastName, firstName, middleName
        :return: response object в вииде httpx.response
        """
        return self.patch('/api/v1/users/{user_id}', json=request)

    def delete_user_api (self, user_id: str) -> Response:
        """
        Метод удаления пользователя по идентификатору
        :param user_id: user id
        :return: response object в вииде httpx.response
        """
        return self.delete('/api/v1/users/{user_id}')