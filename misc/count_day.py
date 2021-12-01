#!/usr/bin/env python
# coding=utf-8

from datetime import datetime, timedelta, timezone, date

tz_utc_8 = timezone(timedelta(hours=8))
now = datetime.now(tz=tz_utc_8)
year  = int(now.strftime("%Y"))
month = int(now.strftime("%m"))
day   = int(now.strftime("%d"))

now=now.date()

next_year=date(int(year)+1,1,1)
now_year =date(int(year),1,1)

sum = (now - now_year).days

surplus_day = (next_year - now).days

print(f"今天是：{year}.{month}.{day}，是今年的第{sum}天，今年还剩{surplus_day}天")
