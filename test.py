import requests
from bs4 import BeautifulSoup as bs
import time

def bus_coming(stop):
    stop = str(stop)
    fime = time.localtime(time.time())
    time_hour = str(fime.tm_hour)
    time_minute = str(fime.tm_min)

    url = "https://tripplanner.yrt.ca/hiwire?Date=Today&TimeHour="+time_hour+"&TimeMinute="+time_minute+"&Meridiem=a&.a=iNextBusFind&.s=BXuxJEvaCS6XpszEt2kGsQ&ShowTimes=1&NumStopTimes=5&GetSchedules=1&EndGeo=&StopAbbr="+stop+"&.a=iNextBusFind"
    html = requests.get(url)
    soup = bs(html.text,'html.parser')

    table = soup.find_all("table",{"class":"datatable"})[0]
    our_list = []
    for i in range(1,len(table.contents)):
        bus = table.contents[i]
        route = bus.contents[1].contents[0]
        scheduled_arrival = bus.contents[3].contents[0]
        estimated_arrival = bus.contents[5].contents[0]
        our_list.append([route, scheduled_arrival,estimated_arrival])
    return our_list
