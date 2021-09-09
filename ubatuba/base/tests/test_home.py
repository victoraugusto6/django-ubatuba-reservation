import pytest
from django.urls import reverse

from django_assertions import assert_contains


@pytest.fixture
def resp(client, db):
    resp = client.get(reverse('base:home'))
    return resp


def test_status_code(resp):
    assert resp.status_code == 200


def test_contains_home_link(resp):
    assert_contains(resp, reverse('base:home'))


def test_contains_dropdown(resp):
    assert_contains(resp, '<li class="nav-item dropdown">')


def test_contains_button_photos(resp):
    assert_contains(resp, 'type="button">Fotos')


def test_contains_button_map(resp):
    assert_contains(resp, 'type="button">Mapa')
