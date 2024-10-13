from model import Department, Employee, Task, User
from enums import Priority, UserRole


class UserDataProvider():
    def __init__(self):
        self.__user_list = []
        self._create_user_list()  # Siguro që lista e përdoruesve të krijohet automatikisht

    def _create_user_list(self):
        user1 = User("1", "1", UserRole.ADMIN)
        user2 = User("2", "2", UserRole.EMPLOYEE)
        user3 = User("3", "3", UserRole.EMPLOYEE)
        user4 = User("4", "4", UserRole.INTERN)
        self.__user_list.append(user1)
        self.__user_list.append(user2)
        self.__user_list.append(user3)
        self.__user_list.append(user4)

    @property
    def user_list(self):
        return self.__user_list


class DataProvider:
    def __init__(self):
        self.__departments = []
        self._create_department_list()

    def _create_department_list(self):
        department1_employee_list = self._create_department1_employees()
        department1 = Department("Sales", department1_employee_list)

        department2_employee_list = self._create_department2_employees()
        department2 = Department("Menagment", department2_employee_list)

        department3_employee_list = self._create_department3_employees()
        department3 = Department("Development", department3_employee_list)

        self.__departments.append(department1)
        self.__departments.append(department2)
        self.__departments.append(department3)

    def _create_department1_employees(self):
        employee1 = Employee("Dep1 Emp1", "XYZ Street 1",
                             "dep1.emp1@email.com", "+383123123", self.task_for_employee1())
        employee2 = Employee("Dep1 Emp2", "XYZ Street 2",
                             "dep1.emp2@email.com", "+383123123", self.task_for_employee2())
        employee3 = Employee("Dep1 Emp3", "XYZ Street 3",
                             "dep1.emp3@email.com", "+383123123", self.task_for_employee3())

        employee_list = [employee1, employee2, employee3]
        return employee_list

    def _create_department2_employees(self):
        employee1 = Employee("Dep2 Emp1", "XYZ Street 1",
                             "dep2.emp1@email.com", "+383123123", self.task_for_employee1())
        employee2 = Employee("Dep2 Emp2", "XYZ Street 2",
                             "dep2.emp2@email.com", "+383123123", self.task_for_employee2())
        employee3 = Employee("Dep2 Emp3", "XYZ Street 3",
                             "dep2.emp3@email.com", "+383123123", self.task_for_employee3())

        employee_list = [employee1, employee2, employee3]
        return employee_list

    def _create_department3_employees(self):
        employee1 = Employee("Dep3 Emp1", "XYZ Street 1",
                             "dep3.emp1@email.com", "+383123123", self.task_for_employee1())
        employee2 = Employee("Dep3 Emp2", "XYZ Street 2",
                             "dep3.emp2@email.com", "+383123123", self.task_for_employee2())
        employee3 = Employee("Dep3 Emp3", "XYZ Street 3",
                             "dep3.emp3@email.com", "+383123123", self.task_for_employee3())

        employee_list = [employee1, employee2, employee3]
        return employee_list

    def task_for_employee1(self):
        tasks = [
            Task("Task 1", "description 1", Priority.LOW),
            Task("Task 2", "description 2", Priority.HIGH),
            Task("Task 3", "description 3", Priority.MEDIUM)
        ]
        return tasks

    def task_for_employee2(self):
        tasks = [
            Task("Task 4", "description 4", Priority.LOW),
            Task("Task 5", "description 5", Priority.HIGH),
            Task("Task 6", "description 6", Priority.MEDIUM)
        ]
        return tasks

    def task_for_employee3(self):
        tasks = [
            Task("Task 7", "description 7", Priority.LOW),
            Task("Task 8", "description 8", Priority.HIGH),
            Task("Task 9", "description 9", Priority.MEDIUM)
        ]
        return tasks

    @property
    def department_list(self):
        return self.__departments
