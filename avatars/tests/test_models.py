import pytest
from accounts.models import User
from lessons.models import Lesson, Module
from courses.models import Course
from avatars.models import Avatar, AvatarSession

@pytest.mark.django_db
def test_avatar_creation_and_session():
    instructor = User.objects.create_user(username="teacher1", password="pass123", role="instructor")
    course = Course.objects.create(title="AI Course", description="Intro", instructor=instructor)
    module = Module.objects.create(course=course, title="Module 1")
    lesson = Lesson.objects.create(module=module, title="Lesson 1", content_type="avatar")
    
    avatar = Avatar.objects.create(name="TutorBot", voice="en-US", language="en")
    session = AvatarSession.objects.create(avatar=avatar, user=instructor, lesson=lesson)
    
    assert avatar.name == "TutorBot"
    assert session.avatar.name == "TutorBot"
    assert session.lesson.title == "Lesson 1"
