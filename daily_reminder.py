input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()

print("\n--- DAILY REMINDER ---")

match priority:
    case "high":
        print("‚ö†Ô∏è Urgent Task!")
    case "medium":
        print("Ì¥î Important Task")
    case "low":
        print("Ì≥ù Low Priority Task")
    case _:
        print("‚ö†Ô∏è Unknown Priority Level")

if time_bound == "yes":
    print(f"Reminder: '{task}' is a {priority} priority task that requires immediate attention today!")
else:
    if priority == "low":
        print(f"Note: '{task}' is a low priority task. Consider completing it when you have free time.")
    else:
        print(f"Reminder: '{task}' is a {priority} priority task. Stay on track!")input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()

print("\n--- DAILY REMINDER ---")

match priority:
    case "high":
        print("‚ö†Ô∏è Urgent Task!")
    case "medium":
        print("Ì¥î Important Task")
    case "low":
        print("Ì≥ù Low Priority Task")
    case _:
        print("‚ö†Ô∏è Unknown Priority Level")

if time_bound == "yes":
    print(f"Reminder: '{task}' is a {priority} priority task that requires immediate attention today!")
else:
    if priority == "low":
        print(f"Note: '{task}' is a low priority task. Consider completing it when you have free time.")
    else:
        print(f"Reminder: '{task}' is a {priority} priority task. Stay on track!")

