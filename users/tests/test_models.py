import pytest

from ..models import User

pytestmark = pytest.mark.django_db

def test_create_user():
    user = User.objects.create_user(
			username="cleber_test",
			email="cleber.nandi.test@gmail.com",
			password="passw0rd"
		)
    
    assert user.username == "cleber_test"
    assert user.email == "cleber.nandi.test@gmail.com"
    assert user.is_active
    assert not user.is_staff
    assert not user.is_superuser


def test_create_superuser():
    user = User.objects.create_superuser(
			username="cleber_admin",
			email="cleber.nandi.admin@gmail.com",
			password="passw0rd"
		)
    
    assert user.username == "cleber_admin"
    assert user.email == "cleber.nandi.admin@gmail.com"
    assert user.is_active
    assert user.is_staff
    assert user.is_superuser