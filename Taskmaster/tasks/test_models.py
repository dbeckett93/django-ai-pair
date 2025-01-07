from django.test import TestCase
from tasks.models import Task, Category

class TaskModelTest(TestCase):

    def setUp(self):
        # Set up non-modified objects used by all test methods
        self.category = Category.objects.create(name="Work")
        self.task = Task.objects.create(
            title="Test task",
            due_date="2025-01-15",
            completed=False,
            category=self.category
        )

    def test_task_creation(self):
        # Test task creation
        self.assertEqual(self.task.title, "Test task")
        self.assertEqual(self.task.due_date, "2025-01-15")
        self.assertEqual(self.task.completed, False)
        self.assertEqual(self.task.category, self.category)
        pass

    def test_task_str(self):
        # Test the __str__ method of the Task model
        self.assertEqual(str(self.task), "Test task")
        pass

    def test_task_due_date(self):
        # Test the due_date field of the Task model
        self.assertEqual(self.task.due_date, "2025-01-15")
        pass

    def test_task_completed(self):
        # Test the completed field of the Task model
        self.assertEqual(self.task.completed, False)
        pass

    def test_task_category(self):
        # Test the category field of the Task model
        self.assertEqual(self.task.category, self.category)
        pass

