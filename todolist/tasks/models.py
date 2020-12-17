from django.db import models

'''
Aqui estão sendo criadas as tabelas e dados que irão ficar guardados
no banco de dados. O banco padrão do django é o sqlite e é o usado 
nesse projeto; porém podem ser usados qualquer outro. 
'''

class Task(models.Model):
	title = models.CharField(max_length=200)
	complete = models.BooleanField(default=False)
	created = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.title