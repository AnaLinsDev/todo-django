from django import forms
from django.forms import ModelForm

from .models import *

'''
Criando a classe de Formulário que será usado na tela inicial para
a criação de novos objetos 
'''

class TaskForm(forms.ModelForm):
	title= forms.CharField(widget= forms.TextInput(attrs={'placeholder':'Add new task...'}))

	class Meta:
		model = Task
		fields = '__all__'