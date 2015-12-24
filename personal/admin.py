from django.contrib import admin


from .models import Personal, Empresa, Productos, Producto


# Register your models here.
class PersonalAdmin(admin.ModelAdmin):
	date_hierarchy = 'created_at'
	search_fields = ['username', 'name']
	list_display = ['pk', 'username', 'created_at', 'name', 'surname', 'updated_at']
	#list_filter = ['language', 'category']
	list_editable = ['username', 'name', 'surname']


class EmpresaAdmin(admin.ModelAdmin):
	date_hierarchy = 'created_at'
	search_fields = ['username', 'name']
	list_display = ['pk', 'username', 'name', 'created_at', 'updated_at']
	#list_filter = ['language', 'category']
	list_editable = ['username', 'name']


class ProductosAdmin(admin.ModelAdmin):
	date_hierarchy = 'created_at'
	search_fields = ['username', 'name']
	list_display = ['pk', 'username', 'empresa', 'show_products', 'updated_at']
	#list_filter = ['language', 'category']
	list_editable = ['username']

	def show_products(self, obj):
		return "\n".join([a.products_set for a in obj.products_set.all()])


class ProductoAdmin(admin.ModelAdmin):
	list_display = ['pk','products_set']
	#list_filter = ['language', 'category']
	list_editable = ['products_set']

admin.site.register(Personal, PersonalAdmin)
admin.site.register(Empresa, EmpresaAdmin)
admin.site.register(Productos, ProductosAdmin)
admin.site.register(Producto, ProductoAdmin)
