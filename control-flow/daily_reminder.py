task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").strip().lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()

print("\n--- DAILY REMINDER ---")

match priority:
    case "high":
        print("HIGH PRIORITY TASK")
    case "medium":
        print("MEDIUM PRIORITY TASK")
    case "low":
        print("LOW PRIORITY TASK")
    case _:
        print("UNKNOWN PRIORITY LEVEL")

if time_bound == "yes":
    print(f"Reminder: '{task}' is a {priority} priority task that requires immediate attention today!")
else:
    if priority == "low":
        print(f"Note: '{task}' is a low priority task. Consider completing it when you have free time.")
    else:
        print(f"Reminder: '{task}' is a {priority} priority task. Stay on track!")