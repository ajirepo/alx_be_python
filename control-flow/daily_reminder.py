task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ")
time_bound = input("Is it time-bound? (yes/no): ")
match priority:
     case priority if priority == "high":
        match time_bound:
            case time_bound if time_bound== "yes":
                print(f"Reminder: {task} is a high priority task that requires immediate attention today!")
            
            case time_bound if time_bound != "yes":
                print(f"Reminder: {task} is a high priority task that does not requires immediate attention now.")
match priority:
     case priority if priority == "medium":
        match time_bound:
            case time_bound if time_bound == "yes":
                print(f"Reminder: {task} is a medium priority task that requires immediate attention today!")
            
            
            case time_bound if time_bound != "yes":
                print(f"Reminder: {task} is a medium priority task that does not requires immediate attention today!")
            
match priority:
