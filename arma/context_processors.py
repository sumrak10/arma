from main.models import Partners, SiteConfiguration
import config
from . import utils


def base_dependencies(request):
    site_config = SiteConfiguration.objects.first()
    partners = Partners.objects.all()
    company_working_now = utils.company_working_now()
    return {
        "RECAPTCHA_PUBLIC_KEY": config.RECAPTCHA_PUBLIC_KEY,
        "site_config": site_config,
        "partners": partners,
        "company_working_now": company_working_now
    }
