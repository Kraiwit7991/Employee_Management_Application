from django.test import TestCase
from employee_app.models import Employee, Position, Department, Status

class ModelTest(TestCase):
    def setUp(self):
        # สร้างข้อมูลที่จำเป็นก่อนรันทุก test
        self.status = Status.objects.create(name="Working")
        self.position = Position.objects.create(name="Developer", salary=50000)
        self.department = Department.objects.create(name="IT")

    def test_create_status(self):
        status = Status.objects.create(name="In Recruitment")
        self.assertEqual(status.name, "In Recruitment")
        self.assertEqual(Status.objects.count(), 2)  

    def test_create_department(self):
        department = Department.objects.create(name="Human Resources")
        self.assertEqual(department.name, "Human Resources")
        self.assertEqual(Department.objects.count(), 2) 

    def test_create_position(self):
        position = Position.objects.create(name="Software Engineer", salary=60000)
        self.assertEqual(position.name, "Software Engineer")
        self.assertEqual(position.salary, 60000)
        self.assertEqual(Position.objects.count(), 2)  

    def test_create_employee(self):
        employee = Employee.objects.create(
            fname="John",
            lname="Doe",
            address="123 Main St",
            is_manager=False,
            position=self.position,
            department=self.department,
            status=self.status
        )

        self.assertEqual(employee.fname, "John")
        self.assertEqual(employee.lname, "Doe")
        self.assertEqual(employee.address, "123 Main St")
        self.assertFalse(employee.is_manager)
        self.assertEqual(employee.position.name, "Developer")
        self.assertEqual(employee.department.name, "IT")
        self.assertEqual(employee.status.name, "Working")
        self.assertEqual(Employee.objects.count(), 1)
