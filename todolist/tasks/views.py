from django.shortcuts import render, redirect
from django.http import HttpResponse

from .models import *
from .forms import *

'''
Quando a url estiver igual a '', a função index irá ser chamada, e 
nela será retornada o conteúdo que está no aquivo list.html dentro
do diretório templates

Irá mostrar todos os objetos tasks  guardados no sqlite e
adicionar novos objetos 
'''

def index(request):
	tasks = Task.objects.all()

	form = TaskForm()

	if request.method =='POST':
		form = TaskForm(request.POST)
		if form.is_valid():
			form.save()
		return redirect('/')


	context = {'tasks':tasks, 'form':form}
	return render(request, 'tasks/list.html', context)

'''
Quando a url estiver igual a 'update_task/3/', a função updateTask 
irá ser chamada, e nela será retornada o conteúdo que está no 
aquivo update_task.html dentro do diretório templates para o especifico
index 3 (nesse caso)

Se o usuário apertar em Enviar, entrará no if e o Task de index 3 
será atualizado e voltará para a tela inicial
'''

def updateTask(request, pk):
	task = Task.objects.get(id=pk)

	# form pegará o objeto com id igual a pk
	form = TaskForm(instance=task)

	if request.method == 'POST':
		# form pegará o objeto com id igual a pk, mas atualizado
		form = TaskForm(request.POST, instance=task)
		# O a classe Meta irá ver se está válido de 
		# acordo com o model e entra no if
		if form.is_valid():
			form.save()
			return redirect('/')

	context = {'form':form}

	return render(request, 'tasks/update_task.html', context)

'''
Quando a url estiver igual a 'delete/3/', a função deleteTask 
irá ser chamada, e nela será retornada o conteúdo que está no 
aquivo delete.html dentro do diretório templates para o especifico
index 3 (nesse caso).

Se o usuário apertar em Enviar, entrará no if e o Task de index 3 
será deletado e voltará para a tela inicial
'''

def deleteTask(request, pk):
	item = Task.objects.get(id=pk)

	if request.method == 'POST':
		item.delete()
		return redirect('/')

	context = {'item':item}
	return render(request, 'tasks/delete.html', context)
