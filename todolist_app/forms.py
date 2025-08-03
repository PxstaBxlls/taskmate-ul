from django import forms 
from todolist_app.models import TaskList

#this class will talk about which model i am connecting to and which field i am editing
class Taskform(forms.ModelForm):
    class Meta:
        model = TaskList
        fields = ['tasks','done']