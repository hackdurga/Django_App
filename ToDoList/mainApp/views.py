# mainApp/views.py

from rest_framework import generics, permissions
from .serializers import ToDoSerializer
from .models import ToDo

# Read
class ListTodo(generics.ListAPIView):
    queryset = ToDo.objects.all()
    serializer_class = ToDoSerializer
    permission_classes = [permissions.IsAuthenticated]

# Retrieve or Update
class DetailTodo(generics.RetrieveUpdateAPIView):
    queryset = ToDo.objects.all()
    serializer_class = ToDoSerializer
    permission_classes = [permissions.IsAuthenticated]

# Create
class CreateTodo(generics.CreateAPIView):
    serializer_class = ToDoSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

# Delete
class DeleteTodo(generics.DestroyAPIView):
    queryset = ToDo.objects.all()
    serializer_class = ToDoSerializer
    permission_classes = [permissions.IsAuthenticated]
