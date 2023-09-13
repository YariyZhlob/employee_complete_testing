from dataclasses import dataclass
import os
from dotenv import load_dotenv
from support.custom_errors import CredsNotFoundError


ROOT_PATH = os.path.dirname(os.path.realpath(__file__))
SCENARIOS_PATH = os.path.join(ROOT_PATH, "support", "scenarios.json")
SINGLE_EMPLOYEE_SCHEMA_PATH = os.path.join(ROOT_PATH,'schemas', 'single_employees_schema.json')
ALL_EMPLOYEES_SCHEMA_PATH = os.path.join(ROOT_PATH,'schemas', 'all_employees_schema.json')

# print(ALL_EMPLOYEES_SCHEMA_PATH)
# print(SINGLE_EMPLOYEE_SCHEMA_PATH)


@dataclass
class Credentials:
    load_dotenv()
    APP_USERNAME: str = os.getenv("APP_USERNAME")
    APP_PASSWORD: str = os.getenv("APP_PASSWORD")

    @classmethod
    def get_env_variables(cls):

        if not Credentials.APP_USERNAME or not Credentials.APP_PASSWORD:
            raise CredsNotFoundError

        return cls(Credentials.APP_USERNAME, Credentials.APP_PASSWORD)