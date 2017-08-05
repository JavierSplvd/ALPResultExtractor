class Table:
    def __init__(self, title):
        self.content = []
        self.content.append(title)

    def append(self, Object):
        self.content.append(Object)
