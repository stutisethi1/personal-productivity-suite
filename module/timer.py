import time


def countdown_timer():

    seconds = int(input("Enter time in seconds: "))

    while seconds:
        mins, secs = divmod(seconds, 60)
        timer = f"{mins:02d}:{secs:02d}"
        print(timer, end="\r")
        time.sleep(1)
        seconds -= 1

    print("Time's up!")


def stopwatch():

    input("Press ENTER to start stopwatch")
    start_time = time.time()

    input("Press ENTER to stop stopwatch")
    end_time = time.time()

    elapsed = end_time - start_time
    print(f"Elapsed time: {elapsed:.2f} seconds")


def timer_menu():

    while True:

        print("\n------ Timer & Stopwatch ------")
        print("1. Countdown Timer")
        print("2. Stopwatch")
        print("3. Back to Main Menu")

        choice = input("Enter choice: ")

        if choice == "1":
            countdown_timer()

        elif choice == "2":
            stopwatch()

        elif choice == "3":
            break

        else:
            print("Invalid choice.")
