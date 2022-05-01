class bankAccount:
    id = int
    name = str
    document = str
    email = str
    password = str

    def __init__(self, id, name) -> None:
        self.id = id
        self.name = name