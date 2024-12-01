class LoggerException(Exception):
    def __init__(self, message):
        super().__init__(message)

class PermissionDeniedException(LoggerException):
    def __init__(self, action, user, resource_name):
        message = f"Ошибка: пользователь {user} не имеет права на {action} в {resource_name}"
        super().__init__(message)


class InvalidPermissionException(LoggerException):
    def __init__(self, action):
        message = f"Ошибка: модификатор доступа {action} не существует"
        super().__init__(message)
