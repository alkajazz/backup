from django.contrib import admin
from . import models

class AltigenAdmin(admin.ModelAdmin):
    pass

class EquipmentAdmin(admin.ModelAdmin):
    pass

class EtiSqlAdmin(admin.ModelAdmin):
    pass

class CrystalAdmin(admin.ModelAdmin):
    pass


admin.site.register(models.Altigen, AltigenAdmin)
admin.site.register(models.Equipment, EquipmentAdmin)
admin.site.register(models.EtiSql, EtiSqlAdmin)
admin.site.register(models.Crystal, CrystalAdmin)





# Register your models here.
