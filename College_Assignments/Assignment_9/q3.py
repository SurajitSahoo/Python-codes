import threading
import time

# Function to print numbers with a delay
def print_number(num):
    try:
        if num > 30:
            raise Exception("Number exceeds 30")
        print(num)
    except Exception as e:
        print(f"Error: {e}")

# Timer function to trigger the print_number function every interval
def timer_function():
    for i in range(1, 31):
        threading.Timer(i, print_number, [i]).start()
        time.sleep(1)  # Short delay of 1 second between each number

# Start the timer function
try:
    timer_function()
except KeyboardInterrupt:
    print("\nProcess interrupted by user.")
