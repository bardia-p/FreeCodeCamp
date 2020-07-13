def add_time(start, duration, day=""):
    start_time=start.split()
    duration_time=list(map(lambda x:int(x),duration.split(":")))
    weekdays=[", Monday ",", Tuesday ",", Wednesday ",", Thursday ",", Friday ",", Saturday ", ", Sunday "]

    weekdays2=["MONDAY","TUESDAY","WEDNESDAY","THURSDAY","FRIDAY","SATURDAY", "SUNDAY"]

    next_days=0
    period="AM"

    start_time[0]=list(map(lambda x:int(x),start_time[0].split(":")))

    if start_time[1]=="PM":
      start_time[0][0]+=12

    start_time[0][1]+=duration_time[1]
    if start_time[0][1]>=60:
      start_time[0][1]=start_time[0][1]%60
      start_time[0][0]+=1
  
    start_time[0][0]+=duration_time[0]

    if start_time[0][0]>=24:
      next_days = start_time[0][0]//24
      start_time[0][0]=start_time[0][0]%24

    if start_time[0][0]>12:
      start_time[0][0]-=12
      period="PM"
    elif start_time[0][0]==0:
      period="AM"
      start_time[0][0]=12
    elif start_time[0][0]==12:
      period="PM"

    if day!="":
      day= weekdays[(weekdays2.index(day.upper())+next_days)%7]
    else:
      day=" "
    rest=""

    if next_days==1:
      rest="(next day)"
    elif next_days>1:
      rest="("+str(next_days)+" days later)"

    new_time=(str(start_time[0][0])+":"+"0"*(2-len(str(start_time[0][1])))+str(start_time[0][1])+" "+period+day+rest).strip()
    
    return new_time
