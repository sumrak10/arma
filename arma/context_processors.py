from main.models import Partners, SiteConfiguration
from . import utils

def base_dependencies(reqeust):
    site_config = SiteConfiguration.objects.first()
    partners = Partners.objects.all()
    company_working_now = utils.company_working_now()
    return {"site_config": site_config, "partners": partners, "company_working_now": company_working_now}