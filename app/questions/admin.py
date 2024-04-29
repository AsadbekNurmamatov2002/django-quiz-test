from django.contrib import admin
from .models import Varyant, Savol

# Register your models here.
class VaryantItem(admin.TabularInline):
    model = Varyant
    raw_id_fields = ['savol']

@admin.register(Savol)
class OSavolAdmin(admin.ModelAdmin):
    list_display = ['id', "text", "savol_turi", "updated","created"]
    list_filter = ['id', 'created', 'updated']
    inlines = [VaryantItem]