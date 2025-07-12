try:
    num = float(input("Enter a number: "))
    print(f"The square of {num} is {num ** 2}")
except KeyboardInterrupt:
    print("\nKeyboardInterrupt: No input entered.")
