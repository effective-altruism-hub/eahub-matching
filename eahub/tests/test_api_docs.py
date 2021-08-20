from django.test import TestCase
from rest_framework.test import APIClient


class ApiDocsTest(TestCase):
    client_class = APIClient

    def test_docs_response(self):
        response = self.client.get("/api/docs/")
        self.assertEquals(response.status_code, 200)
