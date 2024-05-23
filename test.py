import timeit
from arma.settings import BASE_DIR
from utils.IP2Location import IP2Location

time = timeit.timeit("""
v3ip_info = IP2Location(BASE_DIR/"utils/IP2Location/files/IP2LOCATION-LITE-DB1.BIN")
rec = v3ip_info.get_all("146.158.69.150")
""", number=1000, globals=globals())
print("Average time: ", time)
# v3ip_info = IP2Location(BASE_DIR/"utils/IP2Location/files/IP2LOCATION-LITE-DB1.IPV6.BIN")
