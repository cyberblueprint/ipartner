from django.db import models
from django.contrib.auth.models import User

from datetime import *

# Create your models here.
class Personal(models.Model):
	username = models.ForeignKey(User)
	created_at = models.DateTimeField(auto_now_add=True)
	name = models.CharField(max_length=30)
	surname = models.CharField(max_length=30)
	updated_at = models.DateTimeField(auto_now=True)


	def __str__(self):
		return self.username

class Empresa(models.Model):
	username = models.ForeignKey(User, default="ipartner")
	name = models.CharField(max_length=30)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.name


PRODUCTOS = (
	('infraestructura', 'infraestructura'),
	('software', 'software'),
	('kpi', 'kpi'),
	('contratos', 'contratos'), 
)


class Producto(models.Model):
	products_set = models.CharField(max_length=300, choices=PRODUCTOS)


class Productos(models.Model):
	username = models.ForeignKey(User)
	empresa = models.ForeignKey(Empresa)
	products_set = models.ManyToManyField(Producto, related_name="products_all")
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
