#education timetable
name = input("Enter teacher_name")

#language options
languages = ["English","French","Japan"]
print("languages available: 0 = English, 1 = French, 2 = Japan")

language_choice = int(input("Select your language(0,1,2): "))

if language_choice in [0,1,2]:
    print(f"Select Language: {languages[language_choice]}")

schedule = int(input("Enter your lecture time(0,1,2): "))
if schedule == 0:
   print(" Schedule: 1:00pm ")
elif schedule == 1:
   print(" Schedule: 2:00pm ")
elif schedule == 2:
   print(" Schedule: 3:00pm ")
else:
   print("The class is close :")


timelines = ["English","French","Japan"]
print("timelines available: 1:00pm = English, 2:00pm = French, 3:00pm = Japan")

      