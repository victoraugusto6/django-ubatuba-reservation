import pytest
from django.urls import reverse


@pytest.fixture
def resp_create(client, db):
    resp = client.get(reverse('hospede:create_hospedes'))
    return resp

# def test_create_hospede(resp_create, hospede):
#     pass
