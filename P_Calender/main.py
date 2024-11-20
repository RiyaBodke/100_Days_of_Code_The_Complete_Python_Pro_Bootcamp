import calendar

art ='''

+-+-+-+-+-+-+-+-+
|C|a|l|e|n|d|a|r|
+-+-+-+-+-+-+-+-+ 

'''

print(art,"\n")

usr_inp = int(input("Enter a year: "))
print("\n")
cal = calendar.TextCalendar(calendar.SUNDAY)
i=1
while i<=12 :
  cal.prmonth(usr_inp,i)
  print("\n")
  i += 1
                            