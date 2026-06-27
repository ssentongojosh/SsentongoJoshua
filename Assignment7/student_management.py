import csv
import json
import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[logging.FileHandler("student_system.log"), logging.StreamHandler()],
)

logger = logging.getLogger(__name__)


# student class to ease creation of student objects
class Student:
    students_list = []

    def __init__(
        self, registration_no, student_no, name, address, contact, program
    ) -> None:
        self.name = name
        self.registration_no = registration_no
        self.student_no = student_no
        # additional student details
        self.address = address
        self.contact = contact
        self.program = program

        # appending the newly created student in the student students_list
        Student.students_list.append(self)
        logger.info(
            f"New student added , Name: {self.name}, RegNo: {self.registration_no}"
        )

    @classmethod
    def get_all_students(cls):
        return cls.students_list

    # overrode the __str__ magic method of the Student class to print teh studetn objects directly in a human readable format
    def __str__(self) -> str:
        return f"Name : {self.name} \nReg No: {self.registration_no} \nStudent No: {self.student_no} \nAddress: {self.address} \nContact: {self.contact} \nProgram: {self.program}\n"

    # helper class method for prompting user for student details to update
    @classmethod
    def prompt_user(cls, attribute: dict[str, str], student):

        attr, prop = list(attribute.items())[0]
        while True:
            choice = input(f"Would you like to update the Student {attr} (y/n): ")
            if choice.lower() not in ["y", "n"]:
                logger.warning('Invalid choice enteered, try "y" or "n"')
                continue
            if choice.lower() == "y":
                value = input(f"Enter new Student {attr}: ")
                setattr(student, prop, value)
                logger.info(
                    f"Student {attr} of student {registration_no} updated to {value} "
                )
                break
            else:
                break

    # searching a student by registration number
    @classmethod
    def search_student(cls, registration_no):
        if len(Student.students_list) == 0:
            return None
        else:
            for student in Student.students_list:
                if student.registration_no == registration_no:
                    return student
                else:
                    return None

    @classmethod
    def update_student(cls, registration_no):
        student = Student.search_student(registration_no)
        if student is None:
            logger.warning(
                f"Update failed: No Student with registration number {registration_no} exists"
            )
            return
        else:
            print("current Student Details")
            print(student)

        Student.prompt_user({"Name": "name"}, student)
        Student.prompt_user({"Reg No": "registration_no"}, student)
        Student.prompt_user({"Student No": "student_no"}, student)
        Student.prompt_user({"Address": "address"}, student)
        Student.prompt_user({"Contact": "contact"}, student)
        Student.prompt_user({"Program": "program"}, student)
        print("")
        logger.info(
            f"Update Successful: Updated details of student with registration number {registration_no}"
        )
        print(student)

    @classmethod
    def delete_student(cls, registration_no):
        student = Student.search_student(registration_no)
        if student is None:
            logger.warning(
                f"Delete failed: No Student with entered registration number {registration_no} exists"
            )
        else:
            if student in Student.students_list:
                Student.students_list.remove(student)
                logger.info(
                    f"Student with registration number {registration_no} deleted"
                )

    # class method to store student details in csv file and json file
    @classmethod
    def store_student_details(cls):
        # store first three attributes in a csv and the rest in json file
        json_file_keys = {"address", "contact", "program"}

        with open("students.csv", "w") as file:
            fields = [
                "name",
                "registration_no",
                "student_no",
            ]
            writer = csv.DictWriter(file, fieldnames=fields)
            writer.writeheader()
            for student in Student.students_list:
                csv_dict = {
                    k: v for k, v in vars(student).items() if k not in json_file_keys
                }
                # writing to csv
                writer.writerow(csv_dict)

        with open("students.json", "w") as file:
            for student in Student.students_list:
                json_dict = {
                    k: v for k, v in vars(student).items() if k in json_file_keys
                }
                # writing to json file
                json.dump(json_dict, file, indent=4)
        logger.info(
            "student details stored in csv with extra details stored in jason file"
        )


class InvalidInputError(Exception):
    def __init__(self, value):
        super().__init__(
            f"{value} is not a valid option, Enter a number between 1 and 7"
        )
        self.value = value


if __name__ == "__main__":
    print("=========== Welcome to the student management system ========")
    while True:
        print("""
        =================================================================
        Choose an action to take.
        1. Add New Student
        2. View all Students 
        3. Search Student
        4. Update Student Details 
        5. Delete Student
        6. Store student details
        7. Quit

        =================================================================
        """)
        choice = input("")
        try:
            choice = int(choice)
            if choice not in [x for x in range(1, 8)]:
                raise InvalidInputError(choice)
        except ValueError:
            logger.error("Non-numeric input entered, enter a number (1-7)")
            continue
        except InvalidInputError as e:
            logger.warning(e)
            continue
        finally:
            logger.debug(f"User selected option {choice}")

        match str(choice):
            case "1":
                name = input("Enter student name: ")
                registration_no = input("Enter student registration number: ")
                student_no = input("Enter student number: ")
                address = input("Enter student address: ")
                contact = input("Enter student contact: ")
                program = input("Enter student program: ")

                Student(registration_no, student_no, name, address, contact, program)
            case "2":
                if len(Student.students_list) == 0:
                    logger.warning("No students added yet, try adding students first")
                print("All Students Details")
                for student in Student.students_list:
                    print(student)
            case "3":
                registration_no = input("Enter student registration number to search: ")
                student = Student.search_student(registration_no)
                if student is None:
                    logger.warning(
                        "Search Failed: No student with entered registration number exists"
                    )
                else:
                    print("Search results")
                    print(student)
            case "4":
                registration_no = input(
                    "Enter registration number of student whose details to update: "
                )
                Student.update_student(registration_no)
            case "5":
                registration_no = input(
                    "Enter registration number of student to delete: "
                )
                Student.delete_student(registration_no)
            case "6":
                Student.store_student_details()
            case "7":
                logger.info("User Quit system")
                print("thank you for using our services")
                print("bye")
                break
