input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()

print("\n--- DAILY REMINDER ---")

match priority:
    case "high":
        print("⚠️ Urgent Task!")
    case "medium":
        print("� Important Task")
    case "low":
        print("� Low Priority Task")
    case _:
        print("⚠️ Unknown Priority Level")

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
        print("⚠️ Urgent Task!")
    case "medium":
        print("� Important Task")
    case "low":
        print("� Low Priority Task")
    case _:
        print("⚠️ Unknown Priority Level")

if time_bound == "yes":
    print(f"Reminder: '{task}' is a {priority} priority task that requires immediate attention today!")
else:
    if priority == "low":
        print(f"Note: '{task}' is a low priority task. Consider completing it when you have free time.")
    else:
        print(f"Reminder: '{task}' is a {priority} priority task. Stay on track!")

