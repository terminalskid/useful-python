import os
import time
import webbrowser
import sys


logo = """ ___                                ___           
(   )                              (   )          
 | |_       .--.                 .-.| |    .--.   
(   __)    /    \               /   \ |   /    \  
 | |      |  .-. ;   .------.  |  .-. |  |  .-. ; 
 | | ___  | |  | |  (________) | |  | |  | |  | | 
 | |(   ) | |  | |             | |  | |  | |  | | 
 | | | |  | |  | |             | |  | |  | |  | | 
 | ' | |  | '  | |             | '  | |  | '  | | 
 ' `-' ;  '  `-' /             ' `-'  /  '  `-' / 
  `.__.    `.__.'               `.__,'    `.__.'  
                                                  
                                                  """

print(logo)
page = "Start"

if page == "Start":
print()
print("0 - Create task n\ 1 - Tasks n\ 2 - All tasks n\ 3 - Settings n\ 4 - About developers")
answer = input($ - )
if answer == 1:
    page = "Tasks"
elif answer == 2: 
    page = "All Tasks"
elif answer == 3:
    page = "Settings"
elif answer == 4:
    page = "About Developers"
elif answer == 0:
    page == "Create Task"
else:
    print("Invalid page.")
    break

if page == "Tasks":
    print(logo)

elif page == "All Tasks":
    print(logo)
elif page == "Settings":
    print(logo)
    print("We have no settings lil bro")

elif page == "About Developers":
    print(logo)
elif page == "Create Task":
    print(logo)
    new_task = input("Create new task: ")
    task_list += new_task
    all_tasks = task_list + new_task
else: 
    print("error 404")
    break
