import pytest
from courses.models import Course
from lessons.models import Module, Lesson
from accounts.models import User

@pytest.mark.django_db
def test_module_and_lesson_creation():
    instructor = User.objects.create_user(username="teacher1", password="pass123", role="instructor")
    course = Course.objects.create(title="Django 101", description="Intro", instructor=instructor)
    module = Module.objects.create(course=course, title="Getting Started", order=1)
    lesson = Lesson.objects.create(module=module, title="Install Django", content_type="text", content="Step 1: ...", order=1)
    
    assert module.course.title == "Django 101"
    assert lesson.module.title == "Getting Started"
    assert lesson.content_type == "text"
