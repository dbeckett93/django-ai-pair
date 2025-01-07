from django.test import TestCase, Client
from django.urls import reverse
from tasks.models import Task, Category
from tasks.forms import TaskForm

class TaskViewTest(TestCase):

    def setUp(self):
        self.client = Client()
        self.category = Category.objects.create(name="Work")
        self.task = Task.objects.create(
            title="Test task",
            due_date="2025-01-15",
            completed=False,
            category=self.category
        )

    def test_index_view_get(self):
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'tasks/index.html')
        self.assertContains(response, 'Taskmaster')
        self.assertIsInstance(response.context['form'], TaskForm)

    def test_index_view_post(self):
        response = self.client.post(reverse('index'), {
            'title': 'New task',
            'due_date': '2025-01-20',
            'category': self.category.id
        })
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('index'))
        self.assertTrue(Task.objects.filter(title='New task').exists())