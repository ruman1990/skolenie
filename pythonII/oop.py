import datetime as d

#now = d.date.today()
now = d.date(2025,12,30)
vianoce = d.date(now.year,12,24)
print(now)
if now > vianoce:
    vianoce = d.date(now.year + 1,12,24)

rozdiel = vianoce - now
print(rozdiel.days)

