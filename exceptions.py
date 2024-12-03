class LoggerExceptions(Exception):
    def __init__(self, message):
        super().__init__(message)

class PermissionDeniedException(LoggerExceptions):
    def __init__(self, action, user, name):
        message = f"Ошибка: пользователь {user}, не имеет права на использование {action} в {name}"
        super().__init__(message)

class InvalidPermissionExceoption(LoggerExceptions):
    def __init__(self, action):
        message = f"Ошибка: {action} - недопустимый модификатор доступа"
        super().__init__(message)
