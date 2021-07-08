from rest_framework import serializers

from .models import Task

class TaskSerializer(serializers.HyperlinkedModelSerializer):
    """Es es mi conmentario de la func Task que serializa """
    class Meta:
        model = Task
        fields = ('id', 'description', 'status')




