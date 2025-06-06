class EmployeeManager:
    def check_id(self, employee_id):
        with open("employees.txt") as f:
            data = f.readlines()
        found = False
        for i in data:
            if i.startswith(employee_id):
                found = True
        return found

    def add_new_employee(self, employee_id, name, position, salary):
        if employee_id.isdigit():
            if name and position:
                if salary.isdigit():
                    if not self.check_id(employee_id):
                        with open("employees.txt", "a") as f:
                            f.write(f"{employee_id}, {name}, {position}, {salary}\n")
                        print("Employee added successfully!")
                    else:
                        print("Employee with such ID already exists, please enter another ID.")
                else:
                    print("Please enter salary in numbers.")
            else:
                print("Please enter something in the field name and position.")
        else:
            print("Please enter employee id in numbers.")

    def view_all_employees(self):
        print("Employee records:")
        with open("employees.txt") as f:
            data = f.readlines()
        for i in data:
            print(i, end="")

    def search_employee_by_id(self, employee_id):
        if employee_id.isdigit():
            with open("employees.txt") as file:
                data = file.readlines()
            found = False
            for i in data:
                if i.startswith(employee_id):
                    found = True
                    break
            text = "Employee not found"
            if found:
                employee = i.split(", ")
                text = f"Employee Found:\n" \
                       f"ID: {employee[0]}\n" \
                       f"name: {employee[1]}\n" \
                       f"position: {employee[2]}\n" \
                       f"salary: {employee[3]}"
            print(text)
        else:
            print("Please enter only numbers!")

    def update_employee_by_id(self, employee_id):
        if employee_id.isdigit():
            with open("employees.txt") as file:
                data = file.readlines()
            found = False
            for i in data:
                if i.startswith(employee_id):
                    found = True
                    break
            if found:
                index = data.index(i)
                employee = i.split(", ")
                text = f"ID: {employee[0]}\n" \
                       f"name: {employee[1]}\n" \
                       f"position: {employee[2]}\n" \
                       f"salary: {employee[3]}"
                print(text)
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
                else:
                    print("Error: Please enter something.")
            else:
                print("Employee not found")
        else:
            print("Please enter only numbers!")

    def delete_employee_by_id(self, employee_id):
        if employee_id.isdigit():
            with open("employees.txt") as file:
                data = file.readlines()
            found = False
            employee = ""
            for employee in data:
                if employee.startswith(employee_id):
                    found = True
                    break
            if found:
                data.remove(employee)
                text = ""
                for i in data:
                    text += i
                with open("employees.txt", "w") as file:
                    file.write(text)
                print("Success, employee deleted.")
            else:
                print("Employee not found")
        else:
            print("Please enter employee id only in numbers")


employee_manager = EmployeeManager()

print("""Welcome to the Employee Records Manager!\n1. Add new employee record
2. View all employee records
3. Search for an employee by Employee ID
4. Update an employee's information
5. Delete an employee record
6. Exit""")

run = True
while run:
    option = input("\nEnter your choice: ")
    if option == "1":
        employee_id = input("Enter Employee ID: ")
        name = input("Enter Name: ")
        position = input("Enter Position: ")
        salary = input("Enter Salary: ")
        employee_manager.add_new_employee(employee_id, name, position, salary)
    elif option == "2":
        employee_manager.view_all_employees()
    elif option == "3":
        employee_id = input("Enter Employee ID to search: ")
        employee_manager.search_employee_by_id(employee_id)
    elif option == "4":
        employee_id = input("Enter Employee ID to update: ")
        employee_manager.update_employee_by_id(employee_id)
    elif option == "5":
        employee_id = input("Enter Employee ID to delete: ")
        employee_manager.delete_employee_by_id(employee_id)
    elif option == "6":
        run = False
    else:
        print("Please choose one of the options above!\n")