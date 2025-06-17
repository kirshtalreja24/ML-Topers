name = input("Enter your name: ")
age = int(input("Enter your age: "))

marks = {}
marks["English"] = float(input("Enter marks in English: "))
marks["Math"] = float(input("Enter marks in Math: "))
marks["Urdu"] = float(input("Enter marks in Urdu: "))

add_bonus = input("Add 5 bonus marks to all subjects? (yes/no): ").strip().lower()

if add_bonus == "yes":
    marks = {subject: (lambda x: x + 5)(score) for subject, score in marks.items()}



def calculate_average(marks_dict):
    total = sum(marks_dict.values())
    average = total / len(marks_dict)
    return average



def cal_grade(average):
    if average >= 80:
        return "A"
    elif average >= 60:
        return "B"
    elif average >= 40:
        return "C"
    else:
        return "F"

average = calculate_average(marks)
grade = cal_grade(average)



filename = "reportcard.txt"
with open(filename, "w") as file:
    file.write(f"Name: {name}\n")
    file.write(f"Age: {age}\n")
    for subject, score in marks.items():
        file.write(f"{subject}: {score}\n")
    file.write(f"Average: {average:.2f}\n")
    file.write(f"Grade: {grade}\n")


print("\n------ Student Report Card ------")
with open(filename, "r") as file:
    report = file.read()
    print(report)
