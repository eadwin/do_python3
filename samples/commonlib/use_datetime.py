#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import re
from datetime import datetime, timedelta, timezone


# 获取当前datetime:
now = datetime.now()
print('now =', now)
print('type(now) =', type(now))
print('datetime -> timestamp:', now.timestamp())

# 用指定日期时间创建datetime:
dt = datetime(2015, 4, 19, 12, 20)
print('dt =', dt)

# 把datetime转换为timestamp:
print('datetime -> timestamp:', dt.timestamp())

# 把timestamp转换为datetime:
t = dt.timestamp()
print('timestamp -> datetime:', datetime.fromtimestamp(t))
print('timestamp -> datetime as UTC+0:', datetime.utcfromtimestamp(t))

# 从str读取datetime:
cday = datetime.strptime('2015-6-1 18:19:59', '%Y-%m-%d %H:%M:%S')
print('strptime:', cday)

# 把datetime格式化输出:
print('strftime:', cday.strftime('%a, %b %d %H:%M'))

# 对日期进行加减:
print('current datetime =', cday)
print('current + 10 hours =', cday + timedelta(hours=10))
print('current - 1 day =', cday - timedelta(days=1))
print('current + 2.5 days =', cday + timedelta(days=2, hours=12))

# 把时间从UTC+0时区转换为UTC+8:
utc_dt = datetime.utcnow().replace(tzinfo=timezone.utc)
utc8_dt = utc_dt.astimezone(timezone(timedelta(hours=8)))
print('UTC+0:00 now =', utc_dt)
print('UTC+8:00 now =', utc8_dt)


#homework
def to_timestamp(dt_str, tz_str):
    dt_time = datetime.strptime(dt_str, '%Y-%m-%d %H:%M:%S')
    tz_utc_str = re.match(r'^UTC([+|-]\d{1,2}):00', tz_str).group(1)
    tz_utc = timezone(timedelta(hours=int(tz_utc_str)))
    dt = dt_time.replace(tzinfo=tz_utc)
    return datetime.timestamp(dt)


# 测试:

t1 = to_timestamp('2015-6-1 08:10:30', 'UTC+7:00')
assert t1 == 1433121030.0, t1

t2 = to_timestamp('2015-5-31 16:10:30', 'UTC-09:00')
assert t2 == 1433121030.0, t2

print('Pass')