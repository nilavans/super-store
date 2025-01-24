class User:
    def __init__(self, id, name, email, phone, type, password):
        self.id = id
        self.name = name
        self.email = email
        self.phone = phone
        self.type = type
        self.password = password

    def __str__(self):
        return f"USER ID: {self.id}\tNAME:{self.name}\tEMAIL:{self.email}\tPHONE:{self.phone}\tPASSWORD: {self.password}"