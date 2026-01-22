from typing import TypedDict
from httpx import Response
from clients.api_client import APIClient

class CreateRequestDict(TypedDict):
    """
    Description create user request structure
    """
    email: str
    password: str
    lastName: str
    firstName: str
    middleName: str

class PublicUsersClient(APIClient):
    """ Client to work with /api/v1/users"""

    def create_user_api(self, request: CreateRequestDict) -> Response:
        """ Method to create user
        :param request: dictionary with email, password, lastName, firstName, middleName
        :return: response object
        """
        return self.post('/api/v1/users', json=request)

