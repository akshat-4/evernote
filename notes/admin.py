from django.contrib import admin
from .models import *

class NotesAdmin(admin.ModelAdmin):
    list_display = ('uploadingdate', 'user', 'notesfile', 'subject', 'branch', 'status')
class SignupAdmin(admin.ModelAdmin):
    list_display = ('user', 'branch', 'role', 'contact')
class FeedbackAdmin(admin.ModelAdmin):
    list_display = ('uploadingdate', 'name', 'email', 'contact', 'description')

class PersonalAdmin(admin.ModelAdmin):
    list_display = ('user', 'uploadingdate', 'file', 'description')

class NotepadAdmin(admin.ModelAdmin):
    list_display = ('user', 'uploadingdate', 'content', 'filename')


admin.site.register(Signup, SignupAdmin)
admin.site.register(Notes, NotesAdmin)
admin.site.register(Feedback, FeedbackAdmin)
admin.site.register(Personal, PersonalAdmin)
admin.site.register(Notepad, NotepadAdmin)
