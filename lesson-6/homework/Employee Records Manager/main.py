program = True
def add_employee():
    with open("employees.txt") as file:
        data = file.readlines()
    if data:
        employee_id = int(data[-1].split(",")[0]) + 1
    else:
        employee_id = 1
    print(data)
    name = input("Enter name: ")
    position = input("Enter position: ")
    salary = input("Enter salary: ")
    if name and position:
        if salary.isdigit():
            with open("employees.txt", "a") as file:
                file.write(f"\n{employee_id}, {name}, {position}, {salary}")
            print("Success, new employee added.")
        else:
            print("Error: Please enter salary in numbers.")
            add_employee()
    else:
        print("Error: Please enter something.")
        add_employee()
def view_all_employees():
    with open("employees.txt") as file:
        data = file.readlines()
    text = ""
    for i in data:
        employee = i.split(",")
        text += f"ID: {employee[0]}\n" \
                f"name: {employee[1]}\n" \
                f"position: {employee[2]}\n" \
                f"salary: {employee[3]}"
    print(text)
def search_employee_by_id():
    employee_id = input("Enter an employee id: ")
    if employee_id.isdigit():
        with open("employees.txt") as file:
            data = file.readlines()
        found = False
        for employee in data:
            if employee.startswith(employee_id):
                found = True
                break
        text = "Employee not found"
        if found:
            employee = employee.split(",")
            text = f"ID: {employee[0]}\n" \
                   f"name: {employee[1]}\n" \
                   f"position: {employee[2]}\n" \
                   f"salary: {employee[3]}"
        print(text)
    else:
        print("Please enter only numbers!")
        search_employee_by_id()
def update_employee_by_id():
    employee_id = input("Enter an employee id: ")
    if employee_id.isdigit():
        with open("employees.txt") as file:
            data = file.readlines()
        found = False
        for employee in data:
            if employee.startswith(employee_id):
                found = True
                break
        text = "Employee not found"
        if found:
            index = data.index(employee)
            employee = employee.split(",")
            text = f"ID: {employee[0]}\n" \
                   f"name: {employee[1]}\n" \
                   f"position: {employee[2]}\n" \
                   f"salary: {employee[3]}"
            name = input("Enter new name: ")
            position = input("Enter new position: ")
            salary = input("Enter new salary: ")
            if name and position:
                if salary.isdigit():
                    data[index] = f"{employee_id}, {name}, {position}, {salary}\n"
                    text = ""
                    for i in data:
                        text += i
                    with open("employees.txt", "w") as file:
                        file.write(text)
                    print("Success, employee updated.")
                else:
                    print("Error: Please enter salary in numbers.")
                    update_employee_by_id()
            else:
                print("Error: Please enter something.")
                update_employee_by_id()
                print(text)
    else:
        print("Please enter only numbers!")
        update_employee_by_id()
def delete_employee_by_id():
    employee_id = input("Enter an employee id: ")
    if employee_id.isdigit():
        with open("employees.txt") as file:
            data = file.readlines()
        found = False
        for employee in data:
            if employee.startswith(employee_id):
                found = True
                break
        text = "Employee not found"
        if found:
            data.remove(employee)
            text = ""
            for i in data:
                text += i
            with open("employees.txt", "w") as file:
                file.write(text)
            text = "Success, employee deleted."
        print(text)
    else:
        print("Please enter employee id only in numbers")
def exit():
    global program
    program = False

actions = {"1": add_employee, "2": view_all_employees, "3": search_employee_by_id, "4": update_employee_by_id,
           "5": delete_employee_by_id, "6": exit}

while program:
    action = input("1. Add new employee record\n"
                   "2. View all employee records\n"
                   "3. Search for an employee by Employee ID\n"
                   "4. Update an employee's information\n"
                   "5. Delete an employee record\n"
                   "6. Exit\n"
                   "Choose one of the options above: ")
    if action in actions.keys():
        actions[action]()
    else:
        print("Please enter only numbers above!")