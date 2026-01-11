import pytest
from courses.models import Course, Enrollment
from accounts.models import User

@pytest.mark.django_db
def test_course_creation():
    instructor = User.objects.create_user(username="teacher1", password="pass123", role="instructor")
    course = Course.objects.create(title="Django 101", description="Intro", instructor=instructor)
    assert course.title == "Django 101"
    assert course.instructor.username == "teacher1"

@pytest.mark.django_db
def test_enrollment():
    learner = User.objects.create_user(username="learner1", password="pass123", role="learner")
    instructor = User.objects.create_user(username="teacher1", password="pass123", role="instructor")
    course = Course.objects.create(title="Python Basics", description="Intro", instructor=instructor)
    enrollment = Enrollment.objects.create(user=learner, course=course)
    assert enrollment.user.username == "learner1"
    assert enrollment.course.title == "Python Basics"
