from django.contrib import admin
from django.contrib.auth.models import User
from .models import Note


# Register the Note model
@admin.register(Note)
class NoteAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'content', 'created_at', 'author_full_name')
    search_fields = ('title', 'content', 'author_full_name')
    list_filter = ('created_at', 'author')  # Add filters by date and author
    ordering = ('created_at',)

    # def author_full_name(self, obj):
    #     return obj.author_full_name
    #
    # author_full_name.short_description = 'Author'




