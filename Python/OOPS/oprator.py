class coordinate:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def sum(self,p):
        return coordinate(self.x+p.x,self.y+p.y)
    def print_point(self):
        print(f"x is{self.x} y is {self.y}")
    def __add__(self,p):
        return coordinate(self.x+p.x,self.y+p.y)
p1=coordinate(3,2)
p2=coordinate(4,5)

# p=p1.sum(p2)
p=p1+p2
p.print_point()

