from .models import Uzduotis
from django.contrib import admin

class UzduotisAdmin(admin.ModelAdmin):
    list_display = ('uzduoties_tekstas', 'vartotojas', 'data')
    # list_editable = ('uzduoties_tekstas', 'data')

  # fieldsets = (
  #       (None, {
  #           'fields': ('uzduotis', 'id')
  #       }),
  # )

admin.site.register(Uzduotis, UzduotisAdmin)
