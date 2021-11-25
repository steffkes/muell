from datetime import datetime, timedelta
from dateutil import parser
import requests
import icalendar
import os

cal = icalendar.Calendar()
cal.add('prodid', '-//Schwendi Muell//')
cal.add('version', '2.0')

r = requests.get("https://mymuell.jumomind.com/mmapp/api.php?r=dates/0&city_id=56744&area_id=56744")

for entry in r.json():
    day = parser.parse(entry["day"])

    event = icalendar.Event()
    event['uid'] = '%s@my-muell' % entry["id"]
    event["summary"] = entry["title"]
    if entry["description"]:
      event["description"] = entry["description"]
    event["dtstamp"] = day.strftime("%Y%m%dT000000Z")
    event.add("dtstart", day.date(), parameters={"value": "DATE"})
    event.add("dtend", day.date() + timedelta(days=1), parameters={"value": "DATE"})

    cal.add_component(event)

with open("./data/56744-schwendi.json", "wb") as fh:
    fh.write(r.content)

with open("./data/56744-schwendi.ics", "wb") as fh:
    fh.write(cal.to_ical())
