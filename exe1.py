import datetime


class user:
    def __init__(self, name):
        self.name = name

    def name(self):
        return self.name

    def name(self, value):
        return value

    def is_logged_in(self):

    def last_logged_in_at(self):

    def log_in(self):

    def log_out(self):

    def can_edit(self, comment):

    def can_delete(self, comment):

    def to_string(self):


class moderator():
    def __init__(self, name):


class admin():
    def __init__(self, name):


class comment:
    def __init__(self, author, message, replied_to):

    def author(self):

    def author(self, value):

    def message(self):

    def message(self, value):

    def created_at(self):

    def replied_to(self):

    def replied_to(self, value):

    def to_string(self):