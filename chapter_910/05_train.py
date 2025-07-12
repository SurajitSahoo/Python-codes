from random import randint
class train():
    def __init__(self, trainno):
        self.trainno = trainno

    def book(self, fro, to):
        print(f"Ticket is book in train no: {self.trainno} from {fro} to {to}")
    
    def getstatus(self, trainno):
        print(f"Train no {self.trainno} is running on time")
    
    def getfare(self, fro, to):
        print(f"Ticket fare is  book in train no: {self.trainno} from {fro} to {to} is {randint(222, 5555)}")
t = train(12366)
t.book("Howrah", "Balichak")