import requests
import jsonschema
from support.json_loader import json_load
from env_setup import SINGLE_EMPLOYEE_SCHEMA_PATH
import allure


class Employees:
    def __init__(self, url: str, session: requests.Session, token):
        self.session = session
        self.url = url
        self.token = token
        self.json_data = {
            "name": "Sergey",
            "organization": "Advertising",
            "role": "Advertiser"
        }
        self.headers = {
            "Authorization": f"Bearer {self.token}",
            "Content-Type": "application/json"
        }
        self.json_update = {
            "name": "Mikhail",
            "organization": "Accounting",
            "role": "Consultant"
        }

    @allure.step('step 1')
    def fetch_all_employees(self):
        response = self.session.get(self.url, headers=self.headers)
        assert response.status_code == 200, f'status code is incorrect: {response.status_code}'


    def create_employee(self):
        response = self.session.post(self.url, headers=self.headers, json=self.json_data)
        assert response.status_code == 200, f'status code is incorrect: {response.status_code}'
        assert response.json()['name'] == 'Sergey'
        assert response.json()['organization'] == 'Advertising'


    def update_employee(self):
        response = requests.put(self.url, headers=self.headers)
        assert response.status_code == 200, f'status code is incorrect: {response.status_code}'
        assert response.json()['message'] == 'Employee updated'


    def delete_employee(self):
        response = requests.delete(self.url, headers=self.headers)
        assert response.status_code == 201, f'status code is incorrect: {response.status_code}'
        assert response.json()['message'] == 'Employee deleted'


    @allure.step('fetch single employee')
    def fetch_single_employee(self, emp_id, data):
        response = self.session.get(self.url + emp_id, headers=self.headers)
        assert response.json() == data, f"FAILED. Actual data: {response.json()} but need: {data}"

    def validate_single_employee_schema(self):
        response = self.session.get(self.url + '/1', headers=self.headers)
        jsonschema.validate(response.json(), json_load(SINGLE_EMPLOYEE_SCHEMA_PATH))

    def validate_all_employees_schema(self):
        response = self.session.get(self.url, headers=self.headers)
        jsonschema.validate(response.json(), json_load(ALL_EMPLOYEES_SCHEMA_PATH))
