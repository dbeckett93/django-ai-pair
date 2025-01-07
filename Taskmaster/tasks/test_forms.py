from django.test import TestCase
from tasks.forms import TaskForm
from tasks.models import Category

class TaskFormTest(TestCase):

    def setUp(self):
        self.category = Category.objects.create(name="Work")

    def test_task_form_valid(self):
        form_data = {
            'title': 'Test task',
            'due_date': '2025-01-15',
            'category': self.category.id
        }
        form = TaskForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_task_form_invalid(self):
        form_data = {
            'title': '',
            'due_date': '2025-01-15',
            'category': self.category.id
        }
        form = TaskForm(data=form_data)
        self.assertFalse(form.is_valid())