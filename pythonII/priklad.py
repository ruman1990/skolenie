from datetime import datetime
import zoneinfo

# Pôvodný čas v New Yorku
ny_tz = zoneinfo.ZoneInfo("America/New_York")
dt_ny = datetime(2025, 1, 15, 12, 0, tzinfo=ny_tz)

# Prevod do Bratislavy
ba_tz = zoneinfo.ZoneInfo("Europe/Bratislava")
dt_ba = dt_ny.astimezone(ba_tz)

print("New York:", dt_ny)
print("Bratislava:", dt_ba)

print("UTC:", dt_ny.astimezone(zoneinfo.ZoneInfo("UTC")))