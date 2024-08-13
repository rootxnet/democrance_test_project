from django.contrib import admin

from customer.models import Customer


class CustomerAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'dob', 'date_added']
    search_fields = ['first_name', 'last_name', ]


admin.site.register(Customer, CustomerAdmin)
