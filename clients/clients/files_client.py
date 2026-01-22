from clients.api_client import APIClient
from httpx import Response, QueryParams, Request

from typing import Any, TypedDict


class CreateFileRequestDict(TypedDict):
    """
    Описание структуры запроса на создание файла
    """
    filename: str
    directory: str
    upload_file: str

class FilesClient(APIClient):
    """
    метод создания файла
    """
    def get_file(self, file_id: str) -> Response:
        """
        Метод получения файла.

        :param file_id: Идентификатор файла.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.get(f"/api/v1/files/{file_id}")

    def create_file(self, request: CreateFileRequestDict) -> Response:
        """
        Метод создания файла.

        :param request: Словарь с filename, directory, upload_file.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.post(
            "/api/v1/files",
            data = request,
            files = {"upload_file": open(request['upload_file'], 'rb')}
        )
    def delete_file(self) -> Response:
        """
        Метод удаления файла.
        :param file_id: Идентификатор файла.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.delete("/api/v1/files/{file_id}")