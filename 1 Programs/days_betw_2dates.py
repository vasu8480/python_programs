date1="25/10/2022"
date2="25/12/2022"
d1=date1.split("/")
d2=date2.split("/")
diff=(int(d2[0]) + int(d2[1])*30 +int(d2[0])*365)-(int(d1[0]) + int(d1[1])*30 +int(d1[0])*365)
print(diff)
#--------------------------------------- Method-2 --------------------------------------------------------
import calendar
from datetime import datetime
d1=date1.split("/")
d2=date2.split("/")
dat1=calendar.datetime.date(int(d1[2]),int(d1[1]),int(d1[0]))
dat2=calendar.datetime.date(int(d2[2]),int(d2[1]),int(d2[0]))
print((dat2-dat1).days)