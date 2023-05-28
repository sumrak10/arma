from django.contrib import admin

from .models import Member, Partners, Slide


@admin.register(Member)
class MemberAdmin(admin.ModelAdmin):
    list_display = ["name", "job"]

@admin.register(Slide)
class SlideAdmin(admin.ModelAdmin):
    list_display = ["id"]

@admin.register(Partners)
class PartnersAdmin(admin.ModelAdmin):
    list_display = ["id", "img"]