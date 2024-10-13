class User:
    def __init__(self, username, password, user_role):
        self.username = username
        self.password = password
        self.user_role = user_role

    @property
    def username(self):
        return self.__username

    @username.setter
    def username(self, username):
        self.__username = username

    @property
    def password(self):
        return self.__password

    @password.setter
    def password(self, password):
        self.__password = password

    @property
    def user_role(self):
        return self.__user_role

    @user_role.setter
    def user_role(self, user_role):
        self.__user_role = user_role


class Department:
    def __init__(self, name, employee_list):
        self.__name = name
        self.__employee_list = employee_list

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value

    @property
    def employee_list(self):
        return self.__employee_list

    @employee_list.setter
    def employee_list(self, value):
        self.__employee_list = value


class Employee:
    def __init__(self, name, address, email, phone_nr, task_list):
        self.__name = name
        self.__address = address
        self.__email = email
        self.__phone_nr = phone_nr
        self.__task_list = task_list

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value

    @property
    def address(self):
        return self.__address

    @address.setter
    def address(self, value):
        self.__address = value

    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, value):
        self.__email = value

    @property
    def phone_nr(self):
        return self.__phone_nr

    @phone_nr.setter
    def phone_nr(self, value):
        self.__phone_nr = value

    @property
    def task_list(self):
        return self.__task_list

    @task_list.setter
    def task_list(self, value):
        self.__task_list = value


class Task:
    def __init__(self, name, description, priority):
        self.__name = name
        self.__description = description
        self.__priority = priority

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value

    @property
    def description(self):
        return self.__description

    @description.setter
    def description(self, value):
        self.__description = value

    @property
    def priority(self):
        return self.__priority

    @priority.setter
    def priority(self, value):
        self.__priority = value
