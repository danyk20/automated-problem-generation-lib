class Challenge:
    """
    Object to represent challenge (level) of the CTFd game
    ...
    Attributes
                ----------
                id : Integer
                    challenge_id

                type : String
                    flag type
    """
    def __init__(self, name, id=None):
        self.id = id
        self.name = name

    def __str__(self):
        return str(self.id) + ". " + str(self.name)

    def __repr__(self):
        return self.__str__()
