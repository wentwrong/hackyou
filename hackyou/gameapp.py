class GameApp:

    def __init__(self, **kwargs):
        self.name = kwargs.get("name", "default")
        self.size = kwargs.get("size", 0)
        self.version = kwargs.get("version", 1)
        self.type = kwargs.get("filetype", "text")