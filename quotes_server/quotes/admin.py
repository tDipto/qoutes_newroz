from django.contrib import admin
from .models import Quote

# class show_company(admin.ModelAdmin):
#     list_display = ["name","address","phone_number"]

admin.site.register(Quote)
