from django.contrib import admin

from .models import Member, News, Partners


@admin.register(Member)
class MemberAdmin(admin.ModelAdmin):
    list_display = ["name", "job", "des"]

@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ["id", "img"]

@admin.register(Partners)
class PartnersAdmin(admin.ModelAdmin):
    list_display = ["id", "img"]