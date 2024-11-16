'''
Логгер — это инструмент или компонент, который используется для записи событий, происходящих в программе.
Логирование помогает разработчикам и системным администраторам отслеживать выполнение программы, находить ошибки,
диагностировать проблемы, а также понимать, как программа работает в различных условиях.
'''

from datetime import datetime

class Logger:
    def __init__(self):
        self.logs = []

    def log(self, message):
        self.logs.append(message)
        time = datetime.now().strftime("%H:%M:%S")
        print(f"LOG from {time}: {message}")

class AccessControl:
    def __init__(self, user):
        self.user = user
        self.permissions = {"read": True, "write": False}

    def has_permission(self, action):
        return self.permissions.get(action, False)

    def change_permission(self, action, value):

        if action in self.permissions:
            self.permissions[action] = value
            print(f"Модификатор доступа '{action}' изменен на {value} для пользователя {self.user}.")
        else:
            print(f"Неверный типа модификатора доступа: {action}. Доступные модификаторы доступа: {list(self.permissions.keys())}.")


class SecureResource(Logger, AccessControl):
    def __init__(self, user, resource_name):
        Logger.__init__(self)
        AccessControl.__init__(self, user)
        self.resource_name = resource_name

    def read(self):
        if self.has_permission("read"):
            self.log(f"{self.user} прочитал ресурс {self.resource_name}.")
            print(f"Чтение рпесурса {self.resource_name}")
        else:
            self.log(f"{self.user} попытался прочитал ресурс {self.resource_name}.")
            print(f"ошибка доступа к ресурсу {self.resource_name}")

    def write(self, data):
        if self.has_permission("write"):
            self.log(f"{self.user} записал в ресурс  {self.resource_name}.")
            print(f"запись завершенга {data}")
        else:
            self.log(f"{self.user} попытался записать в ресурс  {self.resource_name}.")
            print(f"ошибка доступа к ресурсу {self.resource_name}")


resource = SecureResource(user="Alice", resource_name="pharmacyDataBase")
resource.read()
resource.write("Paracetomol")

for log in resource.logs:
    print(log)