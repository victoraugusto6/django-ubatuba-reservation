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


def test_contains_button_reservation(resp):
    assert_contains(resp, 'Ver reservas</a>')


def test_contains_button_add(resp):
    assert_contains(resp, 'Cadastrar reserva</a>')
