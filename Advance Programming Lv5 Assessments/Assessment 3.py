# -*- coding: utf-8 -*-
"""
Created on Sat Nov  9 21:30:53 2024

@author: Jaceb
"""

def load_student_data():
    # I removed the (open file) part because it doesnt work
    students_data = [
        (1000, "Jace", 16, 20, 20, 70),
        (1001, "Gab", 18, 19, 17, 85),
        (1002, "Reiven", 15, 15, 13, 55),
        (1003, "Sunny", 15, 22, 12, 60),
        (1004, "Apollo", 21, 21, 18, 90)
    ]
    
    students = []
    
    for student in students_data:
        student_code = student[0]
        name = student[1]
        course_marks = list(student[2:5])
        exam_mark = student[5]
        total_coursework = sum(course_marks)
        total_marks = total_coursework + exam_mark
        overall_percentage = (total_marks / 160) * 100
        grade = calculate_grade(overall_percentage)
        
        students.append({
            'code': student_code,
            'name': name,
            'course_marks': course_marks,
            'exam_mark': exam_mark,
            'total_coursework': total_coursework,
            'total_marks': total_marks,
            'overall_percentage': overall_percentage,
            'grade': grade
        })
    
    return students

def calculate_grade(percentage):
    if percentage >= 70:
        return 'A'
    elif percentage >= 60:
        return 'B'
    elif percentage >= 50:
        return 'C'
    elif percentage >= 40:
        return 'D'
    else:
        return 'F'

def view_all_students(students):
    print("\nAll Student Records:")
    total_percentage = 0
    for student in students:
        print(f"Name: {student['name']}")
        print(f"Number: {student['code']}")
        print(f"Total Coursework Mark: {student['total_coursework']}")
        print(f"Exam Mark: {student['exam_mark']}")
        print(f"Overall Percentage: {student['overall_percentage']:.2f}%")
        print(f"Grade: {student['grade']}\n")
        total_percentage += student['overall_percentage']
    
    num_students = len(students)
    avg_percentage = total_percentage / num_students if num_students > 0 else 0
    print(f"Total Students: {num_students}, Average Percentage: {avg_percentage:.2f}%")

def view_individual_student(students):
    student_number = input("Enter student number (1000-1004): ")
    for student in students:
        if str(student['code']) == student_number:
            print_student_info(student)
            return
    print("Student not found.")

def print_student_info(student):
    print(f"Name: {student['name']}")
    print(f"Number: {student['code']}")
    print(f"Total Coursework Mark: {student['total_coursework']}")
    print(f"Exam Mark: {student['exam_mark']}")
    print(f"Overall Percentage: {student['overall_percentage']:.2f}%")
    print(f"Grade: {student['grade']}")

def show_highest_student(students):
    highest = max(students, key=lambda s: s['total_marks'])
    print("\nStudent with the Highest Overall Mark:")
    print_student_info(highest)

def show_lowest_student(students):
    lowest = min(students, key=lambda s: s['total_marks'])
    print("\nStudent with the Lowest Overall Mark:")
    print_student_info(lowest)

def sort_students(students):
    order = input("Sort in ascending (a) or descending (d) order? ")
    if order.lower() == 'a':
        sorted_students = sorted(students, key=lambda s: s['total_marks'])
    else:
        sorted_students = sorted(students, key=lambda s: s['total_marks'], reverse=True)

    print("\nSorted Student Records:")
    for student in sorted_students:
        print_student_info(student)

def add_student_record(students):
    student_code = len(students) + 1000
    name = input("Enter student name: ")
    coursework_marks = [int(input(f"Enter mark for coursework {i+1} (0-20): ")) for i in range(3)]
    exam_mark = int(input("Enter exam mark (0-100): "))
    
    total_coursework = sum(coursework_marks)
    total_marks = total_coursework + exam_mark
    overall_percentage = (total_marks / 160) * 100
    grade = calculate_grade(overall_percentage)

    new_student = {
        'code': student_code,
        'name': name,
        'course_marks': coursework_marks,
        'exam_mark': exam_mark,
        'total_coursework': total_coursework,
        'total_marks': total_marks,
        'overall_percentage': overall_percentage,
        'grade': grade
    }
    
    students.append(new_student)
    print("Student record added successfully!")

def delete_student_record(students):
    student_number = input("Enter student number to delete: ")
    for student in students:
        if str(student['code']) == student_number:
            students.remove(student)
            print("Student record deleted successfully!")
            return
    print("Student not found.")

def update_student_record(students):
    student_number = input("Enter student number to update: ")
    for student in students:
        if str(student['code']) == student_number:
            print("Select the item to update:")
            print("1. Name")
            print("2. Coursework Marks")
            print("3. Exam Mark")
            choice = input("Enter choice: ")

            if choice == '1':
                student['name'] = input("Enter new name: ")
            elif choice == '2':
                student['course_marks'] = [int(input(f"Enter new mark for coursework {i+1} (0-20): ")) for i in range(3)]
            elif choice == '3':
                student['exam_mark'] = int(input("Enter new exam mark (0-100): "))
            else:
                print("Invalid choice.")
                return
            
            student['total_coursework'] = sum(student['course_marks'])
            student['total_marks'] = student['total_coursework'] + student['exam_mark']
            student['overall_percentage'] = (student['total_marks'] / 160) * 100
            student['grade'] = calculate_grade(student['overall_percentage'])
            print("Student record updated successfully!")
            return

    print("Student not found.")

def menu():
    students = load_student_data()
    
    while True:
        print("\nMenu:")
        print("1. View all student records")
        print("2. View individual student record")
        print("3. Show student with highest overall mark")
        print("4. Show student with lowest overall mark")
        print("5. Sort student records")
        print("6. Add a student record")
        print("7. Delete a student record")
        print("8. Update a student's record")
        print("9. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            view_all_students(students)
        elif choice == '2':
            view_individual_student(students)
        elif choice == '3':
            show_highest_student(students)
        elif choice == '4':
            show_lowest_student(students)
        elif choice == '5':
            sort_students(students)
        elif choice == '6':
            add_student_record(students)
        elif choice == '7':
            delete_student_record(students)
        elif choice == '8':
            update_student_record(students)
        elif choice == '9':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")

# Corrected this line
if __name__ == "__main__":
    menu()
