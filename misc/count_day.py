#!/usr/bin/env python
# coding=utf-8

from datetime import datetime, timedelta, timezone

tz_utc_8 = timezone(timedelta(hours=8))
now = datetime.now(tz=tz_utc_8)
year  = int(now.strftime("%Y"))
month = int(now.strftime("%m"))
day   = int(now.strftime("%d"))

days = 365
months = [0,31,59,90,120,151,181,212,243,273,304]

if 0 < month < 12:
    sum = months[month - 1] + day

flag = 0
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    flag = 1
    days += 1

if flag == 1 and month > 2:
    sum += 1

print(f"今天是：{year}.{month}.{day}，是今年的第{sum}天，今年还剩{surplus_day}天")
