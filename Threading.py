
import threading
import time

# Student data
marks = [85, 67, 92, 35, 76]

# Task 1: Calculate percentage
def calculate_percentage():
    for i in range(len(marks)):
        percentage = marks[i]
        print("Percentage:", percentage, "%")
        time.sleep(1)

# Task 2: Calculate grades
def calculate_grades():
    for m in marks:
        if m >= 90:
            grade = "A"
        elif m >= 75:
            grade = "B"
        elif m >= 50:
            grade = "C"
        else:
            grade = "D"

        print("Marks:", m, "Grade:", grade)
        time.sleep(1)

# Task 3: Check pass or fail
def check_result():
    for m in marks:
        if m >= 40:
            print(m, "Pass")
        else:
            print(m, "Fail")
        time.sleep(1)

# Main function
def main():
    t1 = threading.Thread(target=calculate_percentage)
    t2 = threading.Thread(target=calculate_grades)
    t3 = threading.Thread(target=check_result)

    t1.start()
    t2.start()
    t3.start()

    t1.join()
    t2.join()
    t3.join()

    print("All tasks completed.")

main()
