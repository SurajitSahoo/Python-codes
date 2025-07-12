def count():
    positive_count = 0
    negative_count = 0
    zero_count = 0

    while True:
        n = int(input("Enter number (enter -1 to stop): "))
        if n == -1:
            break
        elif n > 0:
            positive_count += 1
        elif n < 0:
            negative_count += 1
        else:
            zero_count += 1

    print(f"The positive count is: {positive_count}")
    print(f"The negative count is: {negative_count}")
    print(f"The zero count is: {zero_count}")

count()
