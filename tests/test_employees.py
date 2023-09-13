import pytest
import allure

@allure.description('new login')
@allure.label('owner', 'Yura')
@allure.title('Something')
@allure.suite('Some suite')
@allure.severity(allure.severity_level.BLOCKER)
def test_get_all_employees(employees_endpoint):
    employees_endpoint.fetch_all_employees()


def test_create_employee(employees_endpoint):
    employees_endpoint.create_employee()


def test_update_employee(employees_update_delete_endpoint):
    employees_update_delete_endpoint.update_employee()


def test_delete_employee(employees_update_delete_endpoint):
    employees_update_delete_endpoint.delete_employee()

@pytest.mark.api
def test_fetch_single_employee(employees_endpoint, get_id_created_employees, first_created_employee_data):
    employees_endpoint.fetch_single_employee(f"/{get_id_created_employees}", data=first_created_employee_data)

def test_validate_single_employee_schema(employees_endpoint):
    employees_endpoint.validate_single_employee_schema()

def test_validate_all_employees_schema(employees_endpoint):
    employees_endpoint.validate_all_employees_schema()



#написать тесты на employees -get, post, put, delete
