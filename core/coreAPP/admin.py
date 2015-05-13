from django.contrib import admin
from .models import UseCat, UseItems


class ItemsInline(admin.TabularInline):
	model = UseItems
	extra = 4

class UseCatAdmin(admin.ModelAdmin):
	fieldset = [
	(None, {'fields': ['catName']}),
	('Date information', {'fields':['lastUpdate']}),
	]
	inlines = [ItemsInline]
	list_display = ('catName', 'lastUpdate')
	
	
	
	
# Register your models here.
admin.site.register(UseCat, UseCatAdmin)


