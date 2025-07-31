from rest_framework import viewsets, permissions
from board.models import AddNote
from .serializers import AddNoteSerializer
from .filters import AddNoteFilter
from django_filters.rest_framework import DjangoFilterBackend

class AddNoteViewSet(viewsets.ModelViewSet):
    queryset = AddNote.objects.all()
    serializer_class = AddNoteSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = AddNoteFilter
    permission_classes = [permissions.AllowAny]  # 👈 Require login

    def perform_create(self, serializer):
        serializer.save()  # 👈 Tie note to logged-in user

    def get_queryset(self):
        # Return only notes created by the logged-in user
        return AddNote.objects.all()P
    
    