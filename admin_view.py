import sys
from kivymd.uix.pickers import MDDatePicker
from kivy.uix.textinput import TextInput
from kivy.uix.actionbar import CheckBox
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from dataprovider import DataProvider
from kivymd.uix.textfield import MDTextField
from kivy.uix.button import Button
from kivymd.uix.datatables import MDDataTable
from kivy.metrics import dp
from kivymd.uix.menu import MDDropdownMenu
from kivy.uix.popup import Popup


class EmployeeManagerContentPanel:
    department_list = DataProvider().department_list

    def create_content_panel(self):
        split_layout_panel = GridLayout(cols=2)
        split_layout_panel.add_widget(self._create_employee_input_data_panel())
        split_layout_panel.add_widget(self._create_employee_management_panel())
        return split_layout_panel

    def _create_employee_input_data_panel(self):
        input_data_component_panel = GridLayout(cols=1, padding=30, spacing=20)
        input_data_component_panel.size_hint_x = None
        input_data_component_panel.width = 400

        self.name_input = MDTextField(
            multiline=True, font_size='18sp', hint_text='Name')
        input_data_component_panel.add_widget(self.name_input)

        self.address_input = MDTextField(
            multiline=False, font_size='18sp', hint_text='Address')
        input_data_component_panel.add_widget(self.address_input)

        self.email_input = MDTextField(
            multiline=False, font_size='18sp', hint_text='Email')
        input_data_component_panel.add_widget(self.email_input)

        self.phone_nr_input = MDTextField(
            multiline=False, font_size='18sp', hint_text='Phone number')
        input_data_component_panel.add_widget(self.phone_nr_input)

        input_data_component_panel.add_widget(
            self._create_buttons_component_panel())
        return input_data_component_panel

    def _create_employee_management_panel(self):
        content_panel = GridLayout(cols=1, spacing=10)
        content_panel.add_widget(self._create_department_selector())
        content_panel.add_widget(self._create_employee_selector())
        content_panel.size_hint_x = None
        content_panel.width = 1200
        content_panel.add_widget(self._create_table_panel())
        return content_panel

    def _create_buttons_component_panel(self):
        buttons_components_panel = GridLayout(cols=3, padding=0, spacing=10)
        add_button = Button(text='Add', size_hint=(None, None), size=(
            100, 40), background_color=(0, 1, 1, 1))
        update_button = Button(text='Update', size_hint=(
            None, None), size=(100, 40), background_color=(0, 1, 1, 1))
        delete_button = Button(text='Delete', size_hint=(
            None, None), size=(100, 40), background_color=(0, 1, 1, 1))
        buttons_components_panel.add_widget(add_button)
        buttons_components_panel.add_widget(update_button)
        buttons_components_panel.add_widget(delete_button)
        return buttons_components_panel

    def _create_table_panel(self):
        table_panel = GridLayout(cols=1, padding=10, spacing=0)
        self.employee_table = self.create_table()
        table_panel.add_widget(self.employee_table)
        return table_panel

    def _create_department_selector(self):
        button = Button(text='Select a department', size_hint=(
            1, 0.1), background_color=(0, 1, 1, 1))

        button.bind(on_release=self.show_department_menu)
        return button

    def _create_employee_selector(self):
        button = Button(text='Select an employee', size_hint=(
            1, 0.1), background_color=(0, 1, 1, 1))

        button.bind(on_release=self.show_employee_menu)
        return button

    def create_table(self):
        table_row_data = []
        self.department = self.department_list[0]
        employees = self.department.employee_list

        for employee in employees:
            table_row_data.append(
                (employee.name, employee.address, employee.email, employee.phone_nr))

        self.employee_table = MDDataTable(
            pos_hint={'center_x': 0.5, 'center_y': 0.5},
            check=True,
            use_pagination=True,
            rows_num=10,
            column_data=[
                ("Name", dp(40)),
                ("Address", dp(30)),
                ("Email", dp(40)),
                ("Phone number", dp(25))
            ],
            row_data=table_row_data
        )
        return self.employee_table

    def show_department_menu(self, button):
        menu_items = []
        department_list = self.department_list

        for department in department_list:
            menu_items.append(
                {'viewclass': 'OneLineListItem', 'text': department.name})

        self.dropdown = MDDropdownMenu(
            caller=button,
            items=menu_items,
            width_mult=5,
            max_height=dp(150),
        )
        self.dropdown.open()

    def show_employee_menu(self, button):
        menu_items = []
        employee_list = self.department.employee_list

        for employee in employee_list:
            menu_items.append(
                {'viewclass': 'OneLineListItem', 'text': employee.name})

        self.dropdown = MDDropdownMenu(
            caller=button,
            items=menu_items,
            width_mult=5,
            max_height=dp(150),
        )
        self.dropdown.open()


class TaskManagerContentPanel:
    department_list = DataProvider().department_list

    def create_content_panel(self):
        split_layout_panel = GridLayout(cols=2)
        split_layout_panel.add_widget(self._create_task_input_data_panel())
        split_layout_panel.add_widget(self._create_management_panel())
        return split_layout_panel

    def _create_task_input_data_panel(self):
        input_data_component_panel = GridLayout(cols=1, padding=30, spacing=20)
        input_data_component_panel.size_hint_x = None
        input_data_component_panel.width = 400
        self.name_input = MDTextField(
            multiline=True, font_size='18sp', hint_text='Name')
        input_data_component_panel.add_widget(self.name_input)
        self.description_input = MDTextField(
            multiline=True, font_size='18sp', hint_text='Description')
        input_data_component_panel.add_widget(self.description_input)
        input_data_component_panel.add_widget(
            self._create_priority_input_data_panel())
        input_data_component_panel.add_widget(
            self._create_button_component_panel())
        return input_data_component_panel

    def _create_priority_input_data_panel(self):
        priority_input_panel = GridLayout(cols=2, spacing=20)
        priority_input_panel.size_hint = (None, None)
        # Assuming there are three priority levels: Low, Medium, High
        priority_options = ['Low', 'Medium', 'High']

        for priority in priority_options:
            checkbox = CheckBox(
                group='priority', active=False, color=(0, 0, 0, 1))
            checkbox_label = Label(text=priority, color=(0, 0, 0, 1))
            priority_input_panel.add_widget(checkbox)
            priority_input_panel.add_widget(checkbox_label)

        return priority_input_panel

    def _create_management_panel(self):
        content_panel = GridLayout(cols=1, spacing=10)
        content_panel.size_hint_x = None
        content_panel.width = 800
        content_panel.add_widget(self._create_department_selector_panel())
        content_panel.add_widget(self._create_employee_selector_panel())
        content_panel.add_widget(self._create_table())
        return content_panel

    def _create_button_component_panel(self):
        buttons_component_panel = GridLayout(cols=3, padding=0, spacing=10)
        add_button = Button(text='Add', size_hint=(None, None), size=(
            100, 40), background_color=(0, 1, 1, 1))
        update_button = Button(text='Update', size_hint=(
            None, None), size=(100, 40), background_color=(0, 1, 1, 1))
        delete_button = Button(text='Delete', size_hint=(
            None, None), size=(100, 40), background_color=(0, 1, 1, 1))
        buttons_component_panel.add_widget(add_button)
        buttons_component_panel.add_widget(update_button)
        buttons_component_panel.add_widget(delete_button)
        return buttons_component_panel

    def _create_department_selector_panel(self):
        button = Button(text='Select a department', size_hint=(
            1, 0.1), background_color=(0, 1, 1, 1))
        button.bind(on_release=self._show_department_list)
        return button

    def _create_employee_selector_panel(self):
        button = Button(text='Select an employee', size_hint=(
            1, 0.1), background_color=(0, 1, 1, 1))
        button.bind(on_release=self._show_employee_list)
        return button

    def _show_department_list(self, button):
        menu_items = []
        department_list = self.department_list

        for department in department_list:
            menu_items.append(
                {'viewclass': 'OneLineListItem', 'text': department.name})

        self.dropdown = MDDropdownMenu(
            caller=button,
            items=menu_items,
            width_mult=5,
            max_height=dp(150),
        )
        self.dropdown.open()

    def _show_employee_list(self, button):
        menu_items = []
        employee_list = self.department_list[0].employee_list

        for employee in employee_list:
            menu_items.append(
                {'viewclass': 'OneLineListItem', 'text': employee.name})

        self.dropdown = MDDropdownMenu(
            caller=button,
            items=menu_items,
            width_mult=5,
            max_height=dp(150),
        )
        self.dropdown.open()

    def _create_table(self):
        table_row_data = []
        department = self.department_list[0]
        employees = department.employee_list
        task_list = employees[0].task_list

        for task in task_list:
            table_row_data.append(
                (task.name, task.description, task.priority.value))

        self.task_table = MDDataTable(
            pos_hint={'center_x': 0.5, 'center_y': 0.5},
            check=True,
            use_pagination=True,
            rows_num=10,
            column_data=[
                ("Name", dp(40)),
                ("Description", dp(50)),
                ("Priority", dp(40))
            ],
            row_data=table_row_data
        )
        return self.task_table


class DepartmentManagerContentPanel:
    department_list = DataProvider().department_list

    def create_content_panel(self):
        split_layout_panel = GridLayout(cols=2)
        split_layout_panel.add_widget(
            self._create_department_input_data_panel())
        split_layout_panel.add_widget(self._create_management_panel())
        return split_layout_panel

    def _create_department_input_data_panel(self):
        input_data_component_panel = GridLayout(cols=1, padding=30, spacing=20)
        input_data_component_panel.size_hint_x = None
        input_data_component_panel.width = 400

        self.name_input = MDTextField(
            multiline=False, font_size='18sp', hint_text='Department Name'
        )
        input_data_component_panel.add_widget(self.name_input)

        self.manager_input = MDTextField(
            multiline=False, font_size='18sp', hint_text='Manager Name'
        )
        input_data_component_panel.add_widget(self.manager_input)

        input_data_component_panel.add_widget(
            self._create_button_component_panel())

        return input_data_component_panel

    def _create_button_component_panel(self):
        buttons_component_panel = GridLayout(cols=3, padding=0, spacing=10)
        add_button = Button(
            text='Add', size_hint=(None, None), size=(100, 40), background_color=(0, 1, 1, 1)
        )
        update_button = Button(
            text='Update', size_hint=(None, None), size=(100, 40), background_color=(0, 1, 1, 1)
        )
        delete_button = Button(
            text='Delete', size_hint=(None, None), size=(100, 40), background_color=(0, 1, 1, 1)
        )

        add_button.bind(on_press=self.add_department)
        update_button.bind(on_press=self.update_department)
        delete_button.bind(on_press=self.delete_department)

        buttons_component_panel.add_widget(add_button)
        buttons_component_panel.add_widget(update_button)
        buttons_component_panel.add_widget(delete_button)
        return buttons_component_panel

    def _create_management_panel(self):
        content_panel = GridLayout(cols=1, spacing=10)
        content_panel.size_hint_x = None
        content_panel.width = 800
        content_panel.add_widget(self._create_department_selector_panel())
        content_panel.add_widget(self._create_table())
        return content_panel

    def _create_department_selector_panel(self):
        button = Button(
            text='Select a department', size_hint=(1, 0.1), background_color=(0, 1, 1, 1)
        )
        button.bind(on_release=self._show_department_list)
        return button

    def _show_department_list(self, button):
        menu_items = []
        department_list = self.department_list

        for department in department_list:
            menu_items.append(
                {'viewclass': 'OneLineListItem', 'text': department.name}
            )

        self.dropdown = MDDropdownMenu(
            caller=button,
            items=menu_items,
            width_mult=5,
            max_height=dp(150),
        )
        self.dropdown.open()

    def _create_table(self):
        table_row_data = []
        for department in self.department_list:
            manager_name = department.manager.name if hasattr(
                department, 'manager') and department.manager else "No Manager"
            table_row_data.append((department.name, manager_name))

        self.department_table = MDDataTable(
            pos_hint={'center_x': 0.5, 'center_y': 0.5},
            check=True,
            use_pagination=True,
            rows_num=10,
            column_data=[
                ("Name", dp(40)),
                ("Manager", dp(50)),
            ],
            row_data=table_row_data,
        )
        return self.department_table

    def add_department(self, instance):
        department_name = self.name_input.text.strip()
        manager_name = self.manager_input.text.strip()

        if department_name and manager_name:
            popup = Popup(
                title="Department Added",
                content=Label(
                    text=f"Department '{department_name}' with manager '{manager_name}' added."),
                size_hint=(None, None),
                size=(400, 200),
            )
            popup.open()
            self.name_input.text = ""
            self.manager_input.text = ""
        else:
            popup = Popup(
                title="Input Error",
                content=Label(
                    text="Please provide valid department and manager names."),
                size_hint=(None, None),
                size=(400, 200),
            )
            popup.open()

    def update_department(self, instance):
        popup = Popup(
            title="Update Department",
            content=Label(text="Department updated successfully."),
            size_hint=(None, None),
            size=(400, 200),
        )
        popup.open()

    def delete_department(self, instance):
        popup = Popup(
            title="Delete Department",
            content=Label(text="Department deleted successfully."),
            size_hint=(None, None),
            size=(400, 200),
        )
        popup.open()


class PayrollManagerContentPanel:
    def __init__(self):
        self.payroll_list = []

    def create_content_panel(self):
        split_layout_panel = GridLayout(cols=2)
        split_layout_panel.add_widget(self._create_payroll_input_data_panel())
        split_layout_panel.add_widget(self._create_management_panel())
        return split_layout_panel

    def _create_payroll_input_data_panel(self):
        input_data_component_panel = GridLayout(cols=1, padding=30, spacing=20)
        input_data_component_panel.size_hint_x = None
        input_data_component_panel.width = 400

        self.employee_name_input = MDTextField(
            multiline=False, font_size='18sp', hint_text='Employee Name'
        )
        input_data_component_panel.add_widget(self.employee_name_input)

        self.salary_input = MDTextField(
            multiline=False, font_size='18sp', hint_text='Salary'
        )
        input_data_component_panel.add_widget(self.salary_input)

        payment_date_button = Button(
            text="Select Payment Date", size_hint=(None, None), size=(200, 50), background_color=(0, 1, 0.7, 1)
        )
        payment_date_button.bind(on_press=self.show_date_picker)
        input_data_component_panel.add_widget(payment_date_button)

        input_data_component_panel.add_widget(
            self._create_button_component_panel())

        return input_data_component_panel

    def _create_button_component_panel(self):
        buttons_component_panel = GridLayout(cols=3, padding=0, spacing=10)
        add_button = Button(
            text='Add', size_hint=(None, None), size=(100, 40), background_color=(0, 1, 1, 1)
        )
        update_button = Button(
            text='Update', size_hint=(None, None), size=(100, 40), background_color=(0, 1, 1, 1)
        )
        delete_button = Button(
            text='Delete', size_hint=(None, None), size=(100, 40), background_color=(0, 1, 1, 1)
        )

        add_button.bind(on_press=self.add_payroll)
        update_button.bind(on_press=self.update_payroll)
        delete_button.bind(on_press=self.delete_payroll)

        buttons_component_panel.add_widget(add_button)
        buttons_component_panel.add_widget(update_button)
        buttons_component_panel.add_widget(delete_button)
        return buttons_component_panel

    def show_date_picker(self, instance):
        date_dialog = MDDatePicker()
        date_dialog.bind(on_save=self.on_date_selected)
        date_dialog.open()

    def on_date_selected(self, instance, value, date_range):
        self.selected_date = value.strftime('%Y-%m-%d')

    def _create_management_panel(self):
        content_panel = GridLayout(cols=1, spacing=10)
        content_panel.size_hint_x = None
        content_panel.width = 800
        content_panel.add_widget(self._create_table())
        return content_panel

    def _create_table(self):
        table_row_data = []
        for payroll in self.payroll_list:
            table_row_data.append(
                (payroll["employee"], payroll["salary"], payroll["date"]))

        self.payroll_table = MDDataTable(
            pos_hint={'center_x': 0.5, 'center_y': 0.5},
            check=True,
            use_pagination=True,
            rows_num=10,
            column_data=[
                ("Employee", dp(40)),
                ("Salary", dp(30)),
                ("Date", dp(30)),
            ],
            row_data=table_row_data,
        )
        return self.payroll_table

    def add_payroll(self, instance):
        employee_name = self.employee_name_input.text.strip()
        salary = self.salary_input.text.strip()
        payment_date = getattr(self, 'selected_date', None)

        if employee_name and salary and payment_date:
            self.payroll_list.append(
                {"employee": employee_name, "salary": salary, "date": payment_date})
            self.refresh_table()
            popup = Popup(
                title="Payroll Added",
                content=Label(
                    text=f"Payroll entry for '{employee_name}' with salary '{salary}' on {payment_date} added."),
                size_hint=(None, None),
                size=(400, 200),
            )
            popup.open()
            self.employee_name_input.text = ""
            self.salary_input.text = ""
            self.selected_date = None
        else:
            popup = Popup(
                title="Input Error",
                content=Label(
                    text="Please provide valid employee name, salary, and payment date."),
                size_hint=(None, None),
                size=(400, 200),
            )
            popup.open()

    def update_payroll(self, instance):
        popup = Popup(
            title="Update Payroll",
            content=Label(text="Payroll updated successfully."),
            size_hint=(None, None),
            size=(400, 200),
        )
        popup.open()

    def delete_payroll(self, instance):
        popup = Popup(
            title="Delete Payroll",
            content=Label(text="Payroll deleted successfully."),
            size_hint=(None, None),
            size=(400, 200),
        )
        popup.open()

    def refresh_table(self):
        table_row_data = [(payroll["employee"], payroll["salary"],
                           payroll["date"]) for payroll in self.payroll_list]
        self.payroll_table.row_data = table_row_data


class AccountManagementPanel:
    def __init__(self):
        self.account_list = []

    def create_content_panel(self):
        panel = GridLayout(cols=2, padding=30, spacing=20)
        panel.add_widget(self._create_input_data_panel())
        panel.add_widget(self._create_management_panel())
        return panel

    def _create_input_data_panel(self):
        input_panel = GridLayout(cols=1, padding=30, spacing=20)
        input_panel.size_hint_x = None
        input_panel.width = 400
        self.username_input = MDTextField(
            multiline=False, font_size='18sp', hint_text='Username'
        )
        input_panel.add_widget(self.username_input)
        self.email_input = MDTextField(
            multiline=False, font_size='18sp', hint_text='Email'
        )
        input_panel.add_widget(self.email_input)
        self.role_input = MDTextField(
            multiline=False, font_size='18sp', hint_text='Role'
        )
        input_panel.add_widget(self.role_input)
        input_panel.add_widget(self._create_button_panel())
        return input_panel

    def _create_button_panel(self):
        button_panel = GridLayout(cols=3, padding=0, spacing=10)
        add_button = Button(
            text=' Add Account ', size_hint=(None, None), size=(100, 40), background_color=(0, 1, 1, 1)
        )
        update_button = Button(
            text=' Update Account ', size_hint=(None, None), size=(100, 40), background_color=(0.9, 0.7, 0, 1)
        )
        delete_button = Button(
            text=' Delete Account ', size_hint=(None, None), size=(100, 40), background_color=(1, 0, 0, 1)
        )
        add_button.bind(on_press=self.add_account)
        update_button.bind(on_press=self.update_account)
        delete_button.bind(on_press=self.delete_account)
        button_panel.add_widget(add_button)
        button_panel.add_widget(update_button)
        button_panel.add_widget(delete_button)
        return button_panel

    def _create_management_panel(self):
        management_panel = GridLayout(cols=1, spacing=10)
        management_panel.size_hint_x = None
        management_panel.width = 800
        management_panel.add_widget(self.create_account_table())
        return management_panel

    def create_account_table(self):
        table_row_data = [(account["username"], account["email"],
                           account["role"]) for account in self.account_list]
        self.account_table = MDDataTable(
            pos_hint={"center_x": 0.5, "center_y": 0.5},
            check=True,
            use_pagination=True,
            rows_num=10,
            column_data=[
                ("Username", dp(40)),
                ("Email", dp(50)),
                ("Role", dp(30)),
            ],
            row_data=table_row_data
        )
        return self.account_table

    def refresh_table(self):
        table_row_data = [(account["username"], account["email"],
                           account["role"]) for account in self.account_list]
        self.account_table.row_data = table_row_data

    def add_account(self, instance):
        username = self.username_input.text.strip()
        email = self.email_input.text.strip()
        role = self.role_input.text.strip()

        if username and email and role:
            self.account_list.append(
                {"username": username, "email": email, "role": role})
            self.refresh_table()
            popup = Popup(
                title="Account Added",
                content=Label(
                    text=f"Account '{username}' added successfully."),
                size_hint=(None, None),
                size=(400, 200),
            )
            popup.open()
            self.username_input.text = ""
            self.email_input.text = ""
            self.role_input.text = ""
        else:
            popup = Popup(
                title="Input Error",
                content=Label(
                    text="Please provide username, email, and role."),
                size_hint=(None, None),
                size=(400, 200),
            )
            popup.open()

    def update_account(self, instance):
        selected_row = self.account_table.get_row_checks()
        if selected_row:
            index = selected_row[0][0]
            account = self.account_list[index]
            account["username"] = self.username_input.text.strip(
            ) or account["username"]
            account["email"] = self.email_input.text.strip() or account["email"]
            account["role"] = self.role_input.text.strip() or account["role"]
            self.refresh_table()
            popup = Popup(
                title="Account Updated",
                content=Label(
                    text=f"Account '{account['username']}' updated successfully."),
                size_hint=(None, None),
                size=(400, 200),
            )
            popup.open()
        else:
            popup = Popup(
                title="Selection Error",
                content=Label(text="Please select an account to update."),
                size_hint=(None, None),
                size=(400, 200),
            )
            popup.open()

    def delete_account(self, instance):
        selected_row = self.account_table.get_row_checks()
        if selected_row:
            index = selected_row[0][0]
            del self.account_list[index]
            self.refresh_table()
            popup = Popup(
                title="Account Deleted",
                content=Label(text="Account deleted successfully."),
                size_hint=(None, None),
                size=(400, 200),
            )
            popup.open()
        else:
            popup = Popup(
                title="Selection Error",
                content=Label(text="Please select an account to delete."),
                size_hint=(None, None),
                size=(400, 200),
            )
            popup.open()


class HolidayManagerContentPanel:
    def __init__(self):
        self.holiday_list = []

    def create_content_panel(self):
        split_layout_panel = GridLayout(cols=2)
        split_layout_panel.add_widget(self._create_holiday_input_data_panel())
        split_layout_panel.add_widget(self._create_management_panel())
        return split_layout_panel

    def _create_holiday_input_data_panel(self):
        input_data_component_panel = GridLayout(cols=1, padding=30, spacing=20)
        input_data_component_panel.size_hint_x = None
        input_data_component_panel.width = 400

        self.holiday_name_input = MDTextField(
            multiline=False, font_size='18sp', hint_text='Holiday Name'
        )
        input_data_component_panel.add_widget(self.holiday_name_input)

        date_picker_button = Button(
            text="Select Date", size_hint=(None, None), size=(200, 50), background_color=(0, 1, 0.7, 1)
        )
        date_picker_button.bind(on_press=self.show_date_picker)
        input_data_component_panel.add_widget(date_picker_button)

        input_data_component_panel.add_widget(
            self._create_button_component_panel())

        return input_data_component_panel

    def _create_button_component_panel(self):
        buttons_component_panel = GridLayout(cols=3, padding=0, spacing=10)
        add_button = Button(
            text='Add', size_hint=(None, None), size=(100, 40), background_color=(0, 1, 1, 1)
        )
        update_button = Button(
            text='Update', size_hint=(None, None), size=(100, 40), background_color=(0, 1, 1, 1)
        )
        delete_button = Button(
            text='Delete', size_hint=(None, None), size=(100, 40), background_color=(0, 1, 1, 1)
        )
        add_button.bind(on_press=self.add_holiday)
        update_button.bind(on_press=self.update_holiday)
        delete_button.bind(on_press=self.delete_holiday)
        buttons_component_panel.add_widget(add_button)
        buttons_component_panel.add_widget(update_button)
        buttons_component_panel.add_widget(delete_button)
        return buttons_component_panel

    def show_date_picker(self, instance):
        date_dialog = MDDatePicker()
        date_dialog.bind(on_save=self.on_date_selected)
        date_dialog.open()

    def on_date_selected(self, instance, value, date_range):
        self.selected_date = value.strftime('%Y-%m-%d')

    def _create_management_panel(self):
        content_panel = GridLayout(cols=1, spacing=10)
        content_panel.size_hint_x = None
        content_panel.width = 800
        content_panel.add_widget(self._create_table())
        return content_panel

    def _create_table(self):
        table_row_data = []
        for holiday in self.holiday_list:
            table_row_data.append((holiday["name"], holiday["date"]))

        self.holiday_table = MDDataTable(
            pos_hint={'center_x': 0.5, 'center_y': 0.5},
            check=True,
            use_pagination=True,
            rows_num=10,
            column_data=[
                ("Name", dp(40)),
                ("Date", dp(50)),
            ],
            row_data=table_row_data,
        )
        return self.holiday_table

    def add_holiday(self, instance):
        holiday_name = self.holiday_name_input.text.strip()
        holiday_date = getattr(self, 'selected_date', None)

        if holiday_name and holiday_date:
            self.holiday_list.append(
                {"name": holiday_name, "date": holiday_date})
            self.refresh_table()
            popup = Popup(
                title="Holiday Added",
                content=Label(
                    text=f"Holiday '{holiday_name}' on {holiday_date} added."),
                size_hint=(None, None),
                size=(400, 200),
            )
            popup.open()
            self.holiday_name_input.text = ""
            self.selected_date = None
        else:
            popup = Popup(
                title="Input Error",
                content=Label(
                    text="Please provide valid holiday name and date."),
                size_hint=(None, None),
                size=(400, 200),
            )
            popup.open()

    def update_holiday(self, instance):
        popup = Popup(
            title="Update Holiday",
            content=Label(text="Holiday updated successfully."),
            size_hint=(None, None),
            size=(400, 200),
        )
        popup.open()

    def delete_holiday(self, instance):
        popup = Popup(
            title="Delete Holiday",
            content=Label(text="Holiday deleted successfully."),
            size_hint=(None, None),
            size=(400, 200),
        )
        popup.open()

    def refresh_table(self):
        table_row_data = [(holiday["name"], holiday["date"])
                          for holiday in self.holiday_list]
        self.holiday_table.row_data = table_row_data


class CalendarManagerContentPanel:
    def create_content_panel(self):
        panel = GridLayout(cols=1)
        panel.add_widget(Label(text="Calendar Management Panel"))
        return panel


class SignoutManagerContentPanel:
    def create_content_panel(self):
        panel = GridLayout(cols=1)
        panel.add_widget(Label(text="Sign out Management Panel"))

        signout_button = Button(text="Sign Out", size_hint=(
            None, None), size=(200, 50), background_color=(1, 0, 0, 1))
        signout_button.bind(on_press=self.sign_out)

        panel.add_widget(signout_button)
        return panel

    def sign_out(self, instance):
        popup = Popup(
            title="Signed Out",
            content=Label(text="You have been signed out successfully."),
            size_hint=(None, None), size=(400, 200)
        )
        popup.open()

        if self.manager:
            self.manager.current = "login"


class CustomerManagementContentPanel:
    def __init__(self):
        self.customer_list = []

    def create_content_panel(self):
        panel = GridLayout(cols=1, padding=30, spacing=20)

        panel.add_widget(
            Label(text="Customer Management Panel", font_size="24sp"))

        self.name_input = MDTextField(
            hint_text="Customer Name", size_hint=(0.8, None), height=40)
        self.email_input = MDTextField(
            hint_text="Customer Email", size_hint=(0.8, None), height=40)
        self.phone_input = MDTextField(
            hint_text="Phone Number", size_hint=(0.8, None), height=40)

        panel.add_widget(self.name_input)
        panel.add_widget(self.email_input)
        panel.add_widget(self.phone_input)

        button_panel = GridLayout(
            cols=3, spacing=10, size_hint=(1, None), height=50)
        add_button = Button(text="Add Customer", size_hint=(
            None, None), size=(150, 50), background_color=(0, 0.7, 0.9, 1))
        update_button = Button(text="Update Customer", size_hint=(
            None, None), size=(150, 50), background_color=(0.9, 0.7, 0, 1))
        delete_button = Button(text="Delete Customer", size_hint=(
            None, None), size=(150, 50), background_color=(1, 0, 0, 1))

        add_button.bind(on_press=self.add_customer)
        update_button.bind(on_press=self.update_customer)
        delete_button.bind(on_press=self.delete_customer)

        button_panel.add_widget(add_button)
        button_panel.add_widget(update_button)
        button_panel.add_widget(delete_button)

        panel.add_widget(button_panel)

        self.customer_table = self.create_customer_table()
        panel.add_widget(self.customer_table)

        return panel

    def create_customer_table(self):
        table_row_data = [(customer["name"], customer["email"],
                           customer["phone"]) for customer in self.customer_list]

        self.customer_table = MDDataTable(
            pos_hint={"center_x": 0.5, "center_y": 0.5},
            check=True,
            use_pagination=True,
            rows_num=10,
            column_data=[
                ("Name", dp(30)),
                ("Email", dp(40)),
                ("Phone", dp(30)),
            ],
            row_data=table_row_data
        )
        return self.customer_table

    def refresh_table(self):
        table_row_data = [(customer["name"], customer["email"],
                           customer["phone"]) for customer in self.customer_list]
        self.customer_table.row_data = table_row_data

    def add_customer(self, instance):
        name = self.name_input.text.strip()
        email = self.email_input.text.strip()
        phone = self.phone_input.text.strip()

        if name and email and phone:
            self.customer_list.append(
                {"name": name, "email": email, "phone": phone})
            self.refresh_table()
            popup = Popup(
                title="Customer Added",
                content=Label(text=f"Customer '{name}' added successfully."),
                size_hint=(None, None),
                size=(400, 200),
            )
            popup.open()
            self.name_input.text = ""
            self.email_input.text = ""
            self.phone_input.text = ""
        else:
            popup = Popup(
                title="Input Error",
                content=Label(
                    text="Please provide name, email, and phone number."),
                size_hint=(None, None),
                size=(400, 200),
            )
            popup.open()

    def update_customer(self, instance):
        selected_row = self.customer_table.get_row_checks()
        if selected_row:
            index = selected_row[0][0]
            customer = self.customer_list[index]
            customer["name"] = self.name_input.text.strip() or customer["name"]
            customer["email"] = self.email_input.text.strip(
            ) or customer["email"]
            customer["phone"] = self.phone_input.text.strip(
            ) or customer["phone"]
            self.refresh_table()
            popup = Popup(
                title="Customer Updated",
                content=Label(
                    text=f"Customer '{customer['name']}' updated successfully."),
                size_hint=(None, None),
                size=(400, 200),
            )
            popup.open()
        else:
            popup = Popup(
                title="Selection Error",
                content=Label(text="Please select a customer to update."),
                size_hint=(None, None),
                size=(400, 200),
            )
            popup.open()

    def delete_customer(self, instance):
        selected_row = self.customer_table.get_row_checks()
        if selected_row:
            index = selected_row[0][0]
            del self.customer_list[index]
            self.refresh_table()
            popup = Popup(
                title="Customer Deleted",
                content=Label(text="Customer deleted successfully."),
                size_hint=(None, None),
                size=(400, 200),
            )
            popup.open()
        else:
            popup = Popup(
                title="Selection Error",
                content=Label(text="Please select a customer to delete."),
                size_hint=(None, None),
                size=(400, 200),
            )
            popup.open()


class SalesManagementContentPanel:
    def __init__(self):
        self.sales_list = []

    def create_content_panel(self):
        panel = GridLayout(cols=1, padding=30, spacing=20)

        panel.add_widget(
            Label(text="Sales Management Panel", font_size="24sp"))

        self.item_input = MDTextField(
            hint_text="Item Name", size_hint=(0.8, None), height=40)
        self.quantity_input = MDTextField(
            hint_text="Quantity", size_hint=(0.8, None), height=40)
        self.price_input = MDTextField(
            hint_text="Price", size_hint=(0.8, None), height=40)

        panel.add_widget(self.item_input)
        panel.add_widget(self.quantity_input)
        panel.add_widget(self.price_input)

        button_panel = GridLayout(
            cols=3, spacing=10, size_hint=(1, None), height=50)
        add_button = Button(text="Add Sale", size_hint=(
            None, None), size=(150, 50), background_color=(0, 0.7, 0.9, 1))
        update_button = Button(text="Update Sale", size_hint=(
            None, None), size=(150, 50), background_color=(0.9, 0.7, 0, 1))
        delete_button = Button(text="Delete Sale", size_hint=(
            None, None), size=(150, 50), background_color=(1, 0, 0, 1))

        add_button.bind(on_press=self.add_sale)
        update_button.bind(on_press=self.update_sale)
        delete_button.bind(on_press=self.delete_sale)

        button_panel.add_widget(add_button)
        button_panel.add_widget(update_button)
        button_panel.add_widget(delete_button)

        panel.add_widget(button_panel)

        self.sales_table = self.create_sales_table()
        panel.add_widget(self.sales_table)

        return panel

    def create_sales_table(self):
        table_row_data = [(sale["item"], sale["quantity"], sale["price"])
                          for sale in self.sales_list]

        self.sales_table = MDDataTable(
            pos_hint={"center_x": 0.5, "center_y": 0.5},
            check=True,
            use_pagination=True,
            rows_num=10,
            column_data=[
                ("Item", dp(30)),
                ("Quantity", dp(30)),
                ("Price", dp(30)),
            ],
            row_data=table_row_data
        )
        return self.sales_table

    def refresh_table(self):
        table_row_data = [(sale["item"], sale["quantity"], sale["price"])
                          for sale in self.sales_list]
        self.sales_table.row_data = table_row_data

    def add_sale(self, instance):
        item = self.item_input.text.strip()
        quantity = self.quantity_input.text.strip()
        price = self.price_input.text.strip()

        if item and quantity and price:
            self.sales_list.append(
                {"item": item, "quantity": quantity, "price": price})
            self.refresh_table()
            popup = Popup(
                title="Sale Added",
                content=Label(text=f"Sale of '{item}' added successfully."),
                size_hint=(None, None),
                size=(400, 200),
            )
            popup.open()
            self.item_input.text = ""
            self.quantity_input.text = ""
            self.price_input.text = ""
        else:
            popup = Popup(
                title="Input Error",
                content=Label(
                    text="Please provide item name, quantity, and price."),
                size_hint=(None, None),
                size=(400, 200),
            )
            popup.open()

    def update_sale(self, instance):
        selected_row = self.sales_table.get_row_checks()
        if selected_row:
            index = selected_row[0][0]
            sale = self.sales_list[index]
            sale["item"] = self.item_input.text.strip() or sale["item"]
            sale["quantity"] = self.quantity_input.text.strip() or sale["quantity"]
            sale["price"] = self.price_input.text.strip() or sale["price"]
            self.refresh_table()
            popup = Popup(
                title="Sale Updated",
                content=Label(
                    text=f"Sale of '{sale['item']}' updated successfully."),
                size_hint=(None, None),
                size=(400, 200),
            )
            popup.open()
        else:
            popup = Popup(
                title="Selection Error",
                content=Label(text="Please select a sale to update."),
                size_hint=(None, None),
                size=(400, 200),
            )
            popup.open()

    def delete_sale(self, instance):
        selected_row = self.sales_table.get_row_checks()
        if selected_row:
            index = selected_row[0][0]
            del self.sales_list[index]
            self.refresh_table()
            popup = Popup(
                title="Sale Deleted",
                content=Label(text="Sale deleted successfully."),
                size_hint=(None, None),
                size=(400, 200),
            )
            popup.open()
        else:
            popup = Popup(
                title="Selection Error",
                content=Label(text="Please select a sale to delete."),
                size_hint=(None, None),
                size=(400, 200),
            )
            popup.open()


class CalendarManagementContentPanel:
    def create_content_panel(self):
        panel = GridLayout(cols=1)
        panel.add_widget(Label(text="Calendar Management Panel"))
        return panel


print(sys.modules.get('admin_view'))
