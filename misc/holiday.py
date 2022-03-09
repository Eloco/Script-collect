#!/usr/bin/env python
# coding=utf-8
import httpx
from bs4 import BeautifulSoup
from datetime import datetime

r = httpx.get(f'https://www.officeholidays.com/upcoming/week')
if r.status_code==200:
    soup = BeautifulSoup(r.text, "html.parser")
    tr=soup.find_all("tr")
    all=[]
    for t in tr:
        all_t=[]
        td_lst=t.find_all("td")
        if len(td_lst)==4:
            date=(td_lst[0].time.get('datetime'))
            if datetime.today().strftime('%Y-%m-%d')==date:
                all_t.append(datetime.strptime(date, '%Y-%m-%d').strftime("%A"))
                all_t.append(td_lst[1].get_text())
                all_t.append(td_lst[2].get_text())
                all_t.append(td_lst[3].get_text())
                all.append(tuple(all_t))

    all=sorted(all, key=lambda student: student[3])
    all=sorted(all, key=lambda student: student[2])
    print(f"Today: {datetime.today().strftime('%Y-%m-%d')}, {datetime.today().strftime('%A')}")
    day=""
    day_type=""
    msg=""
    for a in all:
        if a[2] != day_type:
            if msg!="":msg+="\n"
            day_type=a[2]
            msg+="\n"
            msg+=a[2]
        if a[3] !=day:
            if msg!="":msg+="\n"
            day=a[3]
            msg+=f"【{a[3]}】"
        msg+=f"{a[1]}, "
    print(msg)
