import ipaddress

from arma.settings import BASE_DIR
from .database import IP2Location as IP2LocationService


class IP2Location:
    v3ip_info = IP2LocationService(BASE_DIR / "utils/IP2Location/files/IP2LOCATION-LITE-DB1.BIN")
    v4ip_info = IP2LocationService(BASE_DIR / "utils/IP2Location/files/IP2LOCATION-LITE-DB1.IPV6.BIN")

    @classmethod
    def get_country_short(cls, ip) -> str:
        try:
            ip_obj = ipaddress.ip_address(ip)
        except ValueError as err:
            raise err
        else:
            if ip_obj.version == 4:
                return cls.v3ip_info.get_country_short(ip)
            elif ip_obj.version == 6:
                return cls.v4ip_info.get_country_short(ip)