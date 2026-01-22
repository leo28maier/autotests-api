from httpx import Response

from clients.api_client import APIClient
from typing import TypedDict

class GetCoursesQueryDict(TypedDict):
    """
    описание структуры запроса на получения курса
    """
    userId : str

class CreateCourseRequestDict(TypedDict):
    """
    описание структуры запроса на создания курса
    """
    title: str
    maxScore: int | None
    minScore: int | None
    description: str
    estimatedTime: str
    previewFileId: str
    createdByUserId: str

class UpdateCourseRequestDict(TypedDict):
    """
    описание структуры запроса на патч курса
    """
    title: str | None
    maxScore: int | None
    minScore: int | None
    description: str | None
    estimatedTime: str | None


class CoursesClient(APIClient):

    def get_courses(self, query: GetCoursesQueryDict) -> Response:
        return self.get(
            "/api/v1/courses/",
            params = query
        )

    def get_course(self, course_id: str) -> Response:

        return self.get(
            f"/api/v1/courses/{course_id}",
        )


    def create_course(self, request: CreateCourseRequestDict ) -> Response:
        return self.post(
            "/api/v1/courses/",
            json = request
        )

    def update_course(self, course_id: str, request: UpdateCourseRequestDict) -> Response:
        return self.patch(
            f"/api/v1/courses/{course_id}",
            json = request
        )

    def delete_course(self, course_id: str) -> Response:
        return self.delete(f"/api/v1/courses/{course_id}")