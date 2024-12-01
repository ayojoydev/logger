'''
Логгер — это инструмент или компонент, который используется для записи событий, происходящих в программе.
Логирование помогает разработчикам и системным администраторам отслеживать выполнение программы, находить ошибки,
диагностировать проблемы, а также понимать, как программа работает в различных условиях.
'''

from datetime import datetime
import exceptions as exc
class Logger:
    def __init__(self):
        self.logs = []
        self.time = datetime.now().strftime("%H:%M:%S")
        self.date = datetime.now().strftime("%Y-%m-%d")

    def log(self, message):
        log = f"{self.time} " + message
        self.logs.append(log)
        self.__write_to_file(log)

    def __write_to_file(self, data):
        name = f"{self.date}.log"
        with open(name, "a", encoding="utf-8") as file:
            file.write(data + "\n")

class AccessControl:
    def __init__(self, user):
        self.user = user
        self.permissions = {"read": True, "write": False}

    def has_permission(self, action):
        return self.permissions.get(action, False)

    def change_permission(self, action, value=bool()):
        try:
            if action in self.permissions:
                self.permissions[action] = value
                print(f"Модификатор доступа '{action}' изменен на {value} для пользователя {self.user}.")
                self.log(f"Модификатор доступа '{action}' изменен на {value} для пользователя {self.user}.")
            else:
                raise exc.InvalidPermissionException(action)
        except exc.InvalidPermissionException as e:
            self.log(str(e))
            print(e)
class SecureResource(Logger, AccessControl):
    def __init__(self, user, resource_name):
        Logger.__init__(self)
        AccessControl.__init__(self, user)
        self.resource_name = resource_name

    def read(self):
        try:
            if self.has_permission("read"):
                self.log(f"{self.user} прочитал ресурс {self.resource_name}.")
                print(f"Чтение ресурса {self.resource_name}")
            else:
                raise exc.PermissionDeniedException("read", self.user, self.resource_name)
        except exc.PermissionDeniedException as e:
            self.log(str(e))
            print(e)

    def write(self, data):
        try:
            if self.has_permission("write"):
                self.log(f"{self.user} записал в ресурс  {self.resource_name}.")
                print(f"запись завершенга {data}")
            else:
                raise exc.PermissionDeniedException("write", self.user, self.resource_name)
        except exc.PermissionDeniedException as e:
            self.log(str(e))
            print(e)


resource = SecureResource(user="Alice", resource_name="pharmacyDataBase")
resource.change_permission("read", False)
resource.change_permission("delete", False)
resource.read()
resource.write("Paracetomol")
resource.change_permission("write", True)
resource.write("Paracetomol")