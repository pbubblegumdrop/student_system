FILE_NAME = "student.txt"

def calculate_fee(sub1, sub2, sub3):
    fee1 = get_subject_fee(sub1)
    fee2 = get_subject_fee(sub2)
    fee3 = get_subject_fee(sub3)
    return fee1 + fee2 + fee3

def get_subject_name(number):
    if number == 1:
        return "chem"
    elif number == 2:
        return "bio"
    elif number == 3:
        return "math"
    elif number == 4:
        return "phy"
    elif number == 5:
        return "eng"
    else:
        return ""

def get_subject_fee(subject):
    if subject == "chem":
        return 250
    elif subject == "bio":
        return 230
    elif subject == "math":
        return 200
    elif subject == "phy":
        return 220
    elif subject == "eng":
        return 180
    else:
        return 0

def ensure_file():
    try:
        with open(FILE_NAME, "r") as f:
            pass
    except:
        with open(FILE_NAME, "w") as f:
            f.write("ID,Name,Subject1,Subject2,Subject3,TotalFee,Status\n")

def choose_subjects():
    print("Subjects available:")
    print("1. chem (RM250)")
    print("2. bio  (RM230)")
    print("3. math (RM200)")
    print("4. phy  (RM220)")
    print("5. eng  (RM180)")
    
    subjects = []
    while len(subjects) < 3:
        try:
            num = int(input(f"Choose subject #{len(subjects)+1} (1-5): "))
            name = get_subject_name(num)
            if name == "":
                print(" Invalid subject.")
            elif name in subjects:
                print(" Already chosen.")
            else:
                subjects.append(name)
        except:
            print(" Please enter a number.")
    return subjects

def add_student():
    ensure_file()
    sid = input("Enter student ID: ")
    name = input("Enter student name: ")
    subjects = choose_subjects()
    total = calculate_fee(subjects[0], subjects[1], subjects[2])

    with open(FILE_NAME, "a") as f:
        f.write(f"{sid},{name},{subjects[0]},{subjects[1]},{subjects[2]},{total},not\n")
    print(" Student added.\n")

def view_students():
    ensure_file()
    with open(FILE_NAME, "r") as f:
        lines = f.readlines()

    if len(lines) <= 1:
        print("No student data.\n")
        return

    print("\n--- All Students ---")
    for line in lines:
        print(line.strip())
    print()

def search_student():
    sid = input("Enter student ID to search: ")
    found = False
    with open(FILE_NAME, "r") as f:
        for line in f:
            if line.startswith(sid + ","):
                print("\n Student Found:")
                print(line.strip())
                found = True
                break
    if not found:
        print(" Student not found.\n")

def delete_student():
    sid = input("Enter student ID to delete: ")
    found = False
    with open(FILE_NAME, "r") as f:
        lines = f.readlines()

    with open(FILE_NAME, "w") as f:
        for line in lines:
            if line.startswith(sid + ","):
                found = True
                continue
            f.write(line)

    if found:
        print(" Student deleted.\n")
    else:
        print(" Student not found.\n")

def edit_status():
    sid = input("Enter student ID to edit status: ")
    found = False
    new_lines = []
    with open(FILE_NAME, "r") as f:
        lines = f.readlines()

    for line in lines:
        if line.startswith(sid + ","):
            parts = line.strip().split(",")
            current = parts[-1]
            new_status = input(f"Current status is '{current}'. Enter new status (not/complete): ").lower()
            if new_status in ["not", "complete"]:
                parts[-1] = new_status
                new_lines.append(",".join(parts) + "\n")
                found = True
            else:
                print(" Invalid status.")
                return
        else:
            new_lines.append(line)

    with open(FILE_NAME, "w") as f:
        f.writelines(new_lines)

    if found:
        print(" Status updated.\n")
    else:
        print(" Student not found.\n")

def edit_subjects():
    sid = input("Enter student ID to edit subjects: ")
    found = False
    new_lines = []

    with open(FILE_NAME, "r") as f:
        lines = f.readlines()

    for line in lines:
        if line.startswith(sid + ","):
            parts = line.strip().split(",")
            print(f"\nEditing subjects for {parts[1]} (ID: {parts[0]})")
            print(f"Current subjects: {parts[2]}, {parts[3]}, {parts[4]}")

            new_subjects = choose_subjects()
            parts[2], parts[3], parts[4] = new_subjects
            parts[5] = str(calculate_fee(new_subjects[0], new_subjects[1], new_subjects[2]))
            new_lines.append(",".join(parts) + "\n")
            found = True
        else:
            new_lines.append(line)

    with open(FILE_NAME, "w") as f:
        f.writelines(new_lines)

    if found:
        print(" Subjects updated.\n")
    else:
        print(" Student not found.\n")

def main():
    ensure_file()
    while True:
        print("=== Student System ===")
        print("1. Add Student")
        print("2. View All Students")
        print("3. Search Student by ID")
        print("4. Edit Student Subjects")
        print("5. Edit Fee Status")
        print("6. Delete Student")
        print("7. Exit")

        try:
            choice = int(input("Choose option (1-7): "))
        except:
            print(" Invalid input. Enter a number.\n")
            continue

        if choice == 1:
            add_student()
        elif choice == 2:
            view_students()
        elif choice == 3:
            search_student()
        elif choice == 4:
            edit_subjects()
        elif choice == 5:
            edit_status()
        elif choice == 6:
            delete_student()
        elif choice == 7:
            print("Goodbye.")
            break
        else:
            print(" Invalid choice.\n")

if __name__ == "__main__":
    main()



