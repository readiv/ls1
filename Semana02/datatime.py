from datetime import datetime, timedelta

print(f"вчера: {(datetime.now()-timedelta(days=1)):%Y-%m-%d}")
print(f"сегодня: {(datetime.now()):%Y-%m-%d}")
print(f"завтра: {(datetime.now()+timedelta(days=1)):%Y-%m-%d}")

s = "01/01/17 12:10:03.234567"
print(datetime.strptime(s, "%d/%m/%y %H:%M:%S.%f"))

