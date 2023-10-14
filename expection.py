class StoryExpection(Exception):
    #this is a constructor for the class
    def __init__(self, message:str, statuscode:int):
        self.message = message
        self.statuscode = statuscode