from django.contrib import admin

from .models import Member, Partners, Slide, AboutUsSlide, Manufactory, SiteConfiguration

@admin.register(SiteConfiguration)
class SiteConfigurationAdmin(admin.ModelAdmin):
    list_display = ["phone", "email", "inn", "ogrn"]

@admin.register(Manufactory)
class ManufactoryAdmin(admin.ModelAdmin):
    list_display = ["id", "city", "address"]

@admin.register(AboutUsSlide)
class AboutUsSlideAdmin(admin.ModelAdmin):
    list_display = ["id"]
    
@admin.register(Member)
class MemberAdmin(admin.ModelAdmin):
    list_display = ["name", "job"]

@admin.register(Slide)
class SlideAdmin(admin.ModelAdmin):
    list_display = ["id"]

@admin.register(Partners)
class PartnersAdmin(admin.ModelAdmin):
    list_display = ["id", "img"]