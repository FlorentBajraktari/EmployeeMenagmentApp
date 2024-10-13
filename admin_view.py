from kivy.uix.actionbar import CheckBox
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from dataprovider import DataProvider
from kivymd.uix.textfield import MDTextField
from kivy.uix.button import Button
from kivymd.uix.datatables import MDDataTable
from kivy.metrics import dp
from kivymd.uix.menu import MDDropdownMenu


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
    def create_content_panel(self):
        panel = GridLayout(cols=1)
        panel.add_widget(Label(text="Department Management Panel"))
        return panel


class PayrollManagerContentPanel:
    def create_content_panel(self):
        panel = GridLayout(cols=1)
        panel.add_widget(Label(text="Payroll Management Panel"))
        return panel


class AccountManagerContentPanel:
    def create_content_panel(self):
        panel = GridLayout(cols=1)
        panel.add_widget(Label(text="Account Management Panel"))
        return panel


class HolidayManagerContentPanel:
    def create_content_panel(self):
        panel = GridLayout(cols=1)
        panel.add_widget(Label(text="Holiday Management Panel"))
        return panel


class CalendarManagerContentPanel:
    def create_content_panel(self):
        panel = GridLayout(cols=1)
        panel.add_widget(Label(text="Calendar Management Panel"))
        return panel


class SignoutManagerContentPanel:
    def create_content_panel(self):
        panel = GridLayout(cols=1)
        panel.add_widget(Label(text="Sign out Management Panel"))
        return panel


class CustomerManagementContentPanel:
    def create_content_panel(self):
        panel = GridLayout(cols=1)
        panel.add_widget(Label(text="Customer Management Panel"))
        return panel


class SalesManagementContentPanel:
    def create_content_panel(self):
        panel = GridLayout(cols=1)
        panel.add_widget(Label(text="Sales Management Panel"))
        return panel


class CalendarManagementContentPanel:
    def create_content_panel(self):
        panel = GridLayout(cols=1)
        panel.add_widget(Label(text="Calendar Management Panel"))
        return panel
