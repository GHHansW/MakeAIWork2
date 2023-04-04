class Rectangle:

    color  = "black"

    def __init__(self, widthArg, heightArg, newColor="black"):
        self.width = widthArg
        self.height = heightArg
        self.area = round(self.width * self.height)
        self.color = newColor

    def getWidth(self):
        pass

    def getArea(self):
        return self.area

class Box(Rectangle):

    def __init__(self, widthArg, heightArg, depthArg):
        super(widthArg, heightArg)
        self.depth = depthArg
        

