class UserManager:
    def __init__(self):
        self.users = []

    def add_user(self, username):
        if username in self.users:
            raise ValueError("Username already exists")
        self.users.append(username)

    def remove_user(self, username):
        if username not in self.users:
            raise ValueError("Username not found")
        self.users.remove(username)

    def list_users(self):
        return self.users
