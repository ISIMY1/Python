#Project from CHATGPT

#This part is where the user will input their name 
username = input("What is your name?")
department = "IT"
#What their device is 
device = input("What is your device model number?")
#The issue with the device 
issue = input("What is your issue with the device?")
priority = "High"
#How long the issue had been occuring for in hours
duration = input("How long has this issue been occurring?")
#This is where we will convert the duration from hours to minutes by using minutes as the str but then we will have to use int to convert the duration into an integer. 
minutes = int(duration) * 60
print("""========================================
            IT SUPPORT TICKET
======================================== 
""")
print("User: " + username)
print("Department: " + department)
print("Device: " + device)
print("Issue: " + issue)
print("Priority: " + priority)
print("Duration: " + duration)
#Where the duration is converted into minutes and then printed out. We also have to convert the minutes into a string so that it can be printed out.
print("Duration in minutes: " + str(minutes))
print("""========================================
          
======================================== 
""")