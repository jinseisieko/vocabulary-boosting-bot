from datetime import datetime


class Data:
    __slots__ = ("data", "date_time",)

    def __init__(self, data: dict):
        super().__init__()
        self.data = data
        self.date_time = datetime.now()


class SResponse(Data):
    ...


class SMRequest(Data):

    def __init__(self, request: str):
        data = {
            "request": request,
        }
        super().__init__(data)

    def __hash__(self):
        return self.data["request"].__hash__()
