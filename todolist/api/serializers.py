from rest_framework import serializers
from board.models import AddNote

class AddNoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = AddNote
        fields = '__all__'
