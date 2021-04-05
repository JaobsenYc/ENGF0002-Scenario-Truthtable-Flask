from lin.exception import Duplicated, Failed, NotFound


class QuizNotFound(NotFound):
    message = "测试不存在"
    _config = False


class QuizDuplicated(Duplicated):
    code = 419
    message = "测试已存在"
    _config = False


class RefreshFailed(Failed):
    message = "令牌刷新失败"
    message_code = 10052
    _config = False

class StrIndexError(Failed):
    message = "Index Error"
    _config = False