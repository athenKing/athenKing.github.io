
import os

def check_ping(hostname):
    # hostname = "taylor"
    response = os.system("ping -c 1 " + hostname)
    # and then check the response...
    if response == 0:
        pingstatus = "Network Active"
    else:
        pingstatus = "Network Error"

    return pingstatus




check_ping("45.142.164.197")