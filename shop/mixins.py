from django.contrib import admin

class IncDecPrioMixin:
    @staticmethod
    @admin.action(description='Понизить приоритет')
    def decrease_product_prio(modeladmin, request, queryset):
        for item in queryset:
            item.decrease_prio()
    @staticmethod
    @admin.action(description='Повысить приоритет')
    def increase_product_prio(modeladmin, request, queryset):
        for item in queryset:
            item.increase_prio()
    
    def decrease_prio(self):
        if self.prio > 0:
            self.prio = self.prio - 1
            self.save()
    def increase_prio(self):
        self.prio = self.prio + 1
        self.save()