class UniversityNotFoundError(Exception):
    def __init__(self, *args):
        super().__init__("University Not Found !!!")