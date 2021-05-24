import os
import sys
import re
from datetime import datetime

def main():
    filepath = sys.argv[1]

    if not os.path.isfile(filepath):
        print("File path {} does not exist. Exiting...".format(filepath))
        sys.exit()
    
    guardingLogs = {}
    with open(filepath) as fp:
        for line in fp:
            datesearch = re.search(r'\[(.+)\] (.+)', line)
            if datesearch:
                datestr = datesearch.group(1)
                content = datesearch.group(2)
                date = datetime.strptime(datestr, '%Y-%m-%d %H:%M')
                guardingLogs[date] = content
            else:
                next

    
    guardstatistics = {}
    guardtotalsleep = {}
    for date in sorted(guardingLogs.keys()):
        print("Date: {}, Content: {}".format(date, guardingLogs[date]))
        if 'Guard' in guardingLogs[date]:
            guardnumber = guardingLogs[date].split(' ')[1][1:]
            next
        if 'falls asleep' in guardingLogs[date]:
            fellasleeptime = date.minute
            next
        if 'wakes up' in guardingLogs[date]:
            wokeuptime = date.minute
            if not guardnumber in guardstatistics:
                guardstatistics[guardnumber] = {i:0 for i in range(60)}
                guardtotalsleep[guardnumber] = 0
            for i in range(fellasleeptime, wokeuptime):
                guardstatistics[guardnumber][i] += 1
                guardtotalsleep[guardnumber] += 1

    guardwithmaxtotalsleep = max(guardtotalsleep.keys(), key=(lambda key: guardtotalsleep[key]))
    mostfrequentminute = max(guardstatistics[guardwithmaxtotalsleep].keys(), key=(lambda key: guardstatistics[guardwithmaxtotalsleep][key]))
        
    valueofinterest = int(guardwithmaxtotalsleep)*mostfrequentminute
    print("Guard {} most frequent minute is {} which results in {}".format(guardwithmaxtotalsleep, mostfrequentminute, valueofinterest))

    minuteguardcountmap = {}
    minutelaziestguardcountmap = {}
    for m in range(0,60):
        minuteguardcountmap[m] = {k:guardstatistics[k][m] for k in guardstatistics.keys()}
        minutelaziestguardcountmap[m] = max(minuteguardcountmap[m].items(), key=lambda x: x[1])
    optitem = max(minutelaziestguardcountmap.items(), key = lambda x: x[1][1])
    
    optguard = optitem[1][0]
    optminute = optitem[0]
    alternativevalue = int(optguard)*optminute
    print("Minute is {} opt guard is {} which results in {}".format(optminute, optguard, alternativevalue))


if __name__ == '__main__':
    main()
