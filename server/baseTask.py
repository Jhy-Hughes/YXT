from typing import List

class baseTask:
    def __init__(self, fuwushang: str, value: str):
        self.fuwushang = fuwushang
        self.value = value

    def __str__(self):
        return f"Fuwushang: {self.fuwushang}, Value: {self.value}"

    def to_dict(self):
        return {
            "fuwushang": self.fuwushang,
            "value": self.value
        }

class userTaskInfo:
    def __init__(self, username: str, password: str, company: str, isWhole: bool, partialTasks: List[baseTask]):
        self.username = username
        self.password = password
        self.company = company
        self.isWhole = isWhole
        self.partialTasks = partialTasks

    def __str__(self):
        tasks_str = ', '.join(str(task) for task in self.partialTasks)
        return (f"Username: {self.username}, Password: {self.password}, "
                f"Company: {self.company}, IsWhole: {self.isWhole}, "
                f"PartialTasks: [{tasks_str}]")

    def to_dict(self):
        return {
            "username": self.username,
            "password": self.password,
            "company": self.company,
            "isWhole": self.isWhole,
            "partialTasks": [task.to_dict() for task in self.partialTasks]
        }