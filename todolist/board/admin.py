from django.contrib import admin
from .models import AddNote, Tags


# Register your models here.
@admin.register(Tags)
class TagsAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name',)
@admin.register(AddNote)
class AddNoteAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'completed', 'duedate', 'created_at')
    list_filter = ('completed', 'duedate')
    search_fields = ('title', 'content')