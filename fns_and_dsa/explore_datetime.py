from datetime import datetime, timedelta

def display_current_datetime():
    current_date = datetime.now()
    print(current_date.strftime("%Y-%m-%d %H:%M:%S"))

def calculate_future_date():
    try:
        days = int(input("Enter number of days to add: "))
        future_date = datetime.now() + timedelta(days=days)
        print(future_date.strftime("%Y-%m-%d"))
    except ValueError:
        print("Please enter a valid integer.")

display_current_datetime()
calculate_future_date()
