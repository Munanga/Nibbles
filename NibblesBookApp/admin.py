from django.contrib import admin
from NibblesBookApp import models

admin.site.register(models.Author)
admin.site.register(models.Publisher)
admin.site.register(models.Store)
admin.site.register(models.Book)
admin.site.register(models.Review)
admin.site.register(models.Format)
