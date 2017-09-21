from django.contrib import admin
from .models import CoinHiveUser, CoinHiveToken

@admin.register(CoinHiveUser)
class CoinHiveUserAdmin(admin.ModelAdmin):
    pass


@admin.register(CoinHiveToken)
class CoinHiveTokenAdmin(admin.ModelAdmin):
    pass
