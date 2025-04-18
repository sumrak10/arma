import requests

from arma import settings


def checkReCAPTHA(request) -> bool:
    if request.method == 'POST':
        recaptcha_response = request.POST.get('g-recaptcha-response', None)
        if recaptcha_response is None:
            return False
        ip = request.META.get('HTTP_X_FORWARDED_FOR', None) or request.META.get('REMOTE_ADDR', None)
        data = {
            'secret': settings.RECAPTCHA_PRIVATE_KEY,
            'response': recaptcha_response,
            # 'remoteip': ip
        }
        verify_url = 'https://www.google.com/recaptcha/api/siteverify'
        response = requests.post(verify_url, data=data)
        result = response.json()
        if result['success']:
            return True
        return False
