#!/usr/bin/python3

from models import storage


print(storage.all())
stats_dict = {}
for clsk, clsv in storage.all().items():
    clsname = clsk.split('.')[0]
    print(clsname)
    stats_dict[clsname] = storage.count(clsname)
print(stats_dict)
