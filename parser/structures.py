from datetime import datetime


class Data:
    __slots__ = ("data", "date_time",)

    def __init__(self, data: dict):
        super().__init__(data)
        self.data = data
        self.date_time = datetime.now()


class SResponse(Data):
    ...


class SRequest:
    ...
