class CredsNotFoundError(AssertionError):
    def __init__(self, message='username or password not found in .env file'):
        super().__init__(message)

class NoTokenInResponseError(AssertionError):
    def __init__(self, message='no_token_in_response'):
        super().__init__(message)

class TokenNotGeneratedError(Exception):
    def __init__(self, status_code):
        self.status_code = status_code
        self.message = self._create_message()
        super().__init__(self.message)

    def _create_message(self):
        return f"Failed to retrieve the token. Status code: {self.status_code}"
