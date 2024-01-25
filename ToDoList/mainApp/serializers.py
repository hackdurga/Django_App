# mainApp/serializers.py

from rest_framework import serializers
from .models import ToDo

class ToDoSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')  # Display the owner's username
    class Meta:
        model = ToDo
        fields = ['id', 'title', 'description', 'due_date', 'status', 'owner']
        read_only_fields = ['owner']
