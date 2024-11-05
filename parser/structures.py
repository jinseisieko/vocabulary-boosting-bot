from datetime import datetime


class Data:
    __slots__ = ("data",)

    def __init__(self, data: dict):
        super().__init__()
        self.data: dict = data


class SResponse(Data):
    __slots__ = ("date_time",)

    def __init__(self, data: dict):
        super().__init__(data)
        self.date_time = datetime.now()


class SRequest:
    ...
