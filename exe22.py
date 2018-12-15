import datetime

class user:
    def __init__(self, name, lastloggedIn = None):
        self.name = name
        self.loggedIn = False
        self.lastloggedIn = lastloggedIn

    def name(self):
        return self.name

    def name(self, value):
        self.name = value

    def is_logged_in(self):
        return self.loggedIn

    def last_logged_in_at(self):
        return self.lastloggedIn

    def log_in(self):
        self.loggedIn = True
        self.lastloggedIn = datetime.datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S")

    def log_out(self):
        self.loggedIn = False

    def can_edit(self, comment):
        if comment.author.name == self.name:
            return True
        else:
            return False

    def can_delete(self, comment):
        return False

# def to_string(self):
# pass

class moderator(user):
    def __init__(self, name):
        user.__init__(self, name)

    def can_delete(self, comment):
        return True



class admin(moderator):
    def __init__(self, name):
        moderator.__init__(self, name)

    def can_edit(self, comment):
        return True


class comment:
    def __init__(self, author, message, replied_to = None, createdAt = None):
        self.createdAt = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.author = author
        self.message = message
        self.replied_to = replied_to

    def author(self):
        return self._author

    def author(self, value):
        self.author = value

    def message(self):
        return self.message

    def message(self, value):
        self.message = value

    def created_at(self):
        return self.createdAt

    def replied_to(self):
        return self.replied_to

    def replied_to(self, value):
        self.replied_to = value

    def to_string(self):
        if self.replied_to == None:
            return self.replied_to + " by " + self.author.name

