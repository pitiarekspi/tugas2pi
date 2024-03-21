def calculate_average_and_print_grades():
    grades = []
    grade = int(input("Masukkan Angka: \n"))

    while grade != -1:
        grades.append(grade)
        grade = int(input())

    if grades:
        average = sum(grades) // len(grades)
        print(average)
        for grade in grades:
            print(grade)

calculate_average_and_print_grades()