import pytest
from rest_framework.test import APIClient


@pytest.fixture
def api_client(request):
    client = APIClient()
    return client
