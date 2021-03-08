import datetime
import winsound
alarmHour= int(input("What hour do you want: ")) #asks user to give hour input
alarmMinute= int(input("What minute do you want: ")) #asks user to give minute input
amPm=str(input("pm or am:")) #asks the user to give am or pm input
print("Waiting for alarm",alarmHour,alarmMinute,amPm)
if(amPm=="pm"): #is statement if the user choses pm and increments the time
    alarmHour +=12
    

while(True):#infinte loop
       if(alarmHour == datetime.datetime.now().hour and
        alarmMinute == datetime.datetime.now().minute): #if statement to check if the user entered time matches the current time
           print("Time to wake up")#prints the statement once the condition is satisfied
           winsound.PlaySound("sound.wav",winsound.SND_ASYNC) #sound
           break

print("Done")
