import requests
from bs4 import BeautifulSoup as bs
import time
import urllib.parse

def BusComing(stop : str):
    fime = time.localtime(time.time())
    table = bs(requests.get(f'https://tripplanner.yrt.ca/hiwire?{urllib.parse.urlencode({"Date": "Today", "TimeHour": fime.tm_hour, "TimeMinute": fime.tm_min, "Meridiem": "a", ".a": "iNextBusFind", ".s": "BXuxJEvaCS6XpszEt2kGsQ", "ShowTimes": "1", "NumStopTimes": "5", "GetSchedules": "1", "EndGeo": "", "StopAbbr": str(stop)})}').text, "html.parser").find("table", {"class": "datatable"})
    BusList = []
    for i in range(1,len(table.contents)):
        bus = table.contents[i]
        route = bus.contents[1].contents[0]
        scheduled_arrival = bus.contents[3].contents[0]
        estimated_arrival = bus.contents[5].contents[0]
        BusList.append([route, scheduled_arrival,estimated_arrival])
    return BusList

# Testing
print(BusComing(1194))
