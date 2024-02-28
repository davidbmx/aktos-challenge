from django.contrib import admin
from accounts.models import Account

@admin.register(Account)
class AccountAdmin(admin.ModelAdmin):
    list_display = ['client_reference_no', 'consumer', 'balance', 'status',]
    list_filter = ['status',]
    search_fields = ['consumer__name',]

