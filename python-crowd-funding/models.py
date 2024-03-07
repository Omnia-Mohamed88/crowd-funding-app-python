# models.py

class User:
    def __init__(self, first_name, last_name, email, password, mobile):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = password
        self.mobile = mobile
        self.is_active = False

class Project:
    def __init__(self, title, details, total_target, start_time, end_time, owner):
        self.title = title
        self.details = details
        self.total_target = total_target
        self.start_time = start_time
        self.end_time = end_time
        self.owner = owner
