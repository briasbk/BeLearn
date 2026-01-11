import pytest
from accounts.models import User, Profile

@pytest.mark.django_db
def test_user_creation():
    user = User.objects.create_user(username="learner1", password="pass123", role="learner")
    assert user.username == "learner1"
    assert user.role == "learner"

@pytest.mark.django_db
def test_profile_creation():
    user = User.objects.create_user(username="teacher1", password="pass123", role="instructor")
    profile = Profile.objects.create(user=user, language="en")
    assert profile.user.username == "teacher1"
    assert profile.language == "en"
