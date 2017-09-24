from django.contrib import admin
from .models import CoinHiveUser, CoinHiveToken, CoinHiveSite

@admin.register(CoinHiveUser)
class CoinHiveUserAdmin(admin.ModelAdmin):
    pass


@admin.register(CoinHiveSite)
class CoinHiveSiteAdmin(admin.ModelAdmin):
    pass


@admin.register(CoinHiveToken)
class CoinHiveTokenAdmin(admin.ModelAdmin):
    pass
