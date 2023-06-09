class NameTooShortError(ValueError):
    """Exception raised when the email name is too short."""


class MustContainAtSymbolError(ValueError):
    """Exception raised when the email doesn't contain '@'."""


class InvalidDomainError(ValueError):
    """Exception raised when the email has an invalid domain."""


valid_domains = ['.com', '.bg', '.net', '.org']

while True:
    try:
        email = input()
        if email == "End":
            break

        if "@" not in email:
            raise MustContainAtSymbolError("Email must contain @")

        email_parts = email.split("@")
        name = email_parts[0]
        domain = "." + email_parts[1].split(".")[-1]

        if len(name) <= 4:
            raise NameTooShortError("Name must be more than 4 characters")

        if domain not in valid_domains:
            raise InvalidDomainError("Domain must be one of the following: .com, .bg, .org, .net")

        print("Email is valid")
    except (NameTooShortError, MustContainAtSymbolError, InvalidDomainError) as e:
        print(e)
