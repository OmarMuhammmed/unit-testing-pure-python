from user_manager import UserManager
import pytest

@pytest.fixture
def user_manager():
    return UserManager()

def test_add_user(user_manager):
    user_manager.add_user("Omar")
    assert user_manager.list_users() == ["Omar"]

def test_remove_user(user_manager):
    user_manager.add_user("Omar")
    user_manager.remove_user("Omar")
    assert user_manager.list_users() == []

def test_add_existing_user(user_manager):
    user_manager.add_user("Omar")
    with pytest.raises(ValueError):
        user_manager.add_user("Omar")
