from django.contrib import admin
from .models import *

# Register your models here.

class PaintingModel(admin.ModelAdmin):
	exclude = ('thumbnail',)


admin.site.register(Painting, PaintingModel)
admin.site.register(Category)