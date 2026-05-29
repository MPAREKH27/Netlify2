# Student Productivity Tracker
# Console Based Python Mini Project

FILE_NAME = "study_data.txt"


# Function to log study hours
def log_study_hours():
    day = input("Enter Day: ")
    hours = input("Enter Study Hours: ")

    file = open(FILE_NAME, "a")
    file.write(day + "," + hours + "\n")
    file.close()

    print("Study hours saved successfully!\n")


# Function to generate weekly report
def weekly_report():
    try:
        file = open(FILE_NAME, "r")
        data = file.readlines()
        file.close()

        if len(data) == 0:
            print("No study data found.\n")
            return

        total_hours = 0

        print("\n----- Weekly Study Report -----")

        for line in data:
            day, hours = line.strip().split(",")
            print(day, ":", hours, "hours")
            total_hours += float(hours)

        average = total_hours / len(data)

        print("-------------------------------")
        print("Total Study Hours:", total_hours)
        print("Average Study Hours:", round(average, 2))
        print()

    except FileNotFoundError:
        print("No data file found.\n")


# Main Menu
while True:
    print("===== Student Productivity Tracker =====")
    print("1. Log Daily Study Hours")
    print("2. Generate Weekly Report")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        log_study_hours()

    elif choice == "2":
        weekly_report()

    elif choice == "3":
        print("Exiting Program...")
        break

    else:
        print("Invalid Choice! Please try again.\n")