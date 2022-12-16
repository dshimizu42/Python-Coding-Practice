#use the bokeh Python library to plot a histogram of which months the scientists have birthdays in
# Birthday Data Part 4

import json
from collections import Counter
from bokeh.plotting import figure, show, output_file

def convertToMonth(num):
    allMonths = {'01': 'January', '02':'February', '03':'March', '04':'April', '05':'May', '06':'June',
        '07':'July', '08':'August', '09':'September', '10':'October', '11':'November', '12':'December'
        }
    
    return allMonths.get(num)
    
if __name__=="__main__":
    with open("info.json", "r") as jsonFile:
        birthday = json.load(jsonFile)
    
    bdayMonths = []
    
    for months in birthday.values():
        bdayMonths.append(months.strip().split('/')[0])
    
    for x in range(len(bdayMonths)):
        bdayMonths[x] = convertToMonth(bdayMonths[x])
    
    monthCounter = Counter(bdayMonths).most_common()
    
    monthX = []
    monthY = []
    
    for z in range(len(monthCounter)):
        monthX.append(monthCounter[z][0])
        monthY.append(monthCounter[z][1])

    monthList = ['January', 'February','March','April','May','June',
    'July','August','September','October','November','December'
    ]
    
    output_file("testplot.html")
    p = figure(x_range = monthList)
    
    p.vbar(x=monthX, top=monthY, width=0.5)
    
    show(p)
    
