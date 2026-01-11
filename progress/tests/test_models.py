import pytest
from accounts.models import User
from courses.models import Course
from lessons.models import Module, Lesson
from progress.models import LessonProgress, CourseProgress

@pytest.mark.django_db
def test_lesson_progress():
    learner = User.objects.create_user(username="learner1", password="pass123", role="learner")
    course = Course.objects.create(title="Python Basics", description="Intro", instructor=learner)
    module = Module.objects.create(course=course, title="Module 1")
    lesson = Lesson.objects.create(module=module, title="Lesson 1", content_type="text", content="Content")
    
    lp = LessonProgress.objects.create(user=learner, lesson=lesson, completed=True)
    cp = CourseProgress.objects.create(user=learner, course=course, progress_percentage=100)
    
    assert lp.completed
    assert cp.progress_percentage == 100
