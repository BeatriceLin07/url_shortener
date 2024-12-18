import pytest
from django.urls import reverse
from shortener.models import URL

@pytest.fixture
def create_url():
    """Fixture to create a URL entry."""
    return URL.objects.create(long_url='https://www.google.com', short_code='abc123', clicks=0)

@pytest.mark.django_db
def test_shorten_url_create(client):
    response = client.post(reverse('shorten_url'), {'long_url': 'https://www.google.com'})
    assert response.status_code == 200
    assert 'short_code' in response.context


@pytest.mark.django_db
def test_shorten_url_existing(client, create_url):
    response = client.post(reverse('shorten_url'), {'long_url': 'https://www.google.com'})
    assert response.status_code == 200
    assert response.context['short_code'] == 'abc123'

@pytest.mark.django_db
def test_redirect_url(client, create_url):
    response = client.get(reverse('redirect_to_url', args=['abc123']))
    assert response.status_code == 302
    assert response.url == 'https://www.google.com'
    create_url.refresh_from_db()
    assert create_url.clicks == 1
