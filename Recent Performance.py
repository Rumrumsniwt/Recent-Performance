#!/usr/bin/python3

# Find Choke
# Author: Murmurtwins

import requests, json, time, math

url='http://akatsuki.pw/api/v1/users/scores/best?mode=0&p=1&l=100&rx=1&id=4391'
r=requests.get(url)
result=json.loads(r.text)
scores=result['scores']
ticks=int(time.time())
item=0
information=''
acc=0
pp=0
max_combomap=0
max_comboyou=0
time_span=86400
print('在过去的',time_span,'秒内，你留了在BP100之内的以下成绩：')
while item<100:
	timeset=scores[item]['time']
	timeArray=time.strptime(timeset,"%Y-%m-%dT%H:%M:%SZ")
	timeStamp=int(time.mktime(timeArray))
	if ticks-timeStamp<=time_span+28800:
		information=scores[item]['beatmap']['song_name']
		acc=scores[item]['accuracy']
		pp=scores[item]['pp']
		max_combomap=scores[item]['beatmap']['max_combo']
		max_comboyou=scores[item]['max_combo']
		print('#',item+1,':',information,'|',acc,'%',max_comboyou,'/',max_combomap,pp,'pp')
		item+=1
	else:
		item+=1
