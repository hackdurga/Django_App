from django.test import TestCase
from django.contrib.auth.models import User
from .models import ToDo
from rest_framework.test import APIClient
from rest_framework import status
from django.urls import reverse
from datetime import date

class ToDoTestCase(TestCase):
    def setUp(self):
        # Create a user
        self.user = User.objects.create_user(username='testuser', password='password')
        self.client = APIClient()
        self.client.force_authenticate(user=self.user)

        # Create a ToDo item
        self.todo_data = {'title': 'Test ToDo', 'description': 'Test Description', 'due_date': date.today()}
        self.response = self.client.post(
            reverse('create_todo'),
            self.todo_data,
            format="json")

    def test_create_todo(self):
        """ Test module for inserting a new todo """
        self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(ToDo.objects.count(), 1)
        self.assertEqual(ToDo.objects.get().title, 'Test ToDo')

    def test_get_all_todos(self):
        """ Test module for getting all todos """
        response = self.client.get(
            reverse('list_todo'),
            format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreaterEqual(len(response.data), 1)

    def test_get_valid_single_todo(self):
        """ Test module for getting a valid single todo """
        response = self.client.get(
            reverse('detail_todo', kwargs={'pk': self.response.data['id']}))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_invalid_single_todo(self):
        """ Test module for getting a invalid single todo """
        response = self.client.get(
            reverse('detail_todo', kwargs={'pk': 999}))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_update_todo(self):
        """ Test module for updating an existing todo record """
        change_todo = {'title': 'Updated ToDo', 'description': 'Updated Description', 'due_date': date.today()}
        res = self.client.put(
            reverse('detail_todo', kwargs={'pk': self.response.data['id']}),
            change_todo, format='json'
        )
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(ToDo.objects.get().title, 'Updated ToDo')

    def test_delete_todo(self):
        """ Test module for deleting an existing todo record """
        response = self.client.delete(
            reverse('delete_todo', kwargs={'pk': self.response.data['id']}))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(ToDo.objects.count(), 0)

    
