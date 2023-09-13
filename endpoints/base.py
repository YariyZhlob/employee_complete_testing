from dataclasses import dataclass


@dataclass
class Endpoints:
    BASE_URL: str = 'http://127.0.0.1:5000'
    TOKEN_URL: str = BASE_URL + '/generate-token'
    EMPLOYEES_URL: str = BASE_URL + '/employees'
    EMPLOYEES_URL_ID: str = BASE_URL + '/employees' + '/3'
