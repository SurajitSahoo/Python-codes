class calculator:
    def __init__(self, n):
        self.n = n
    def squar(self):
        print(f"The square is: {self.n*self.n}")    
    def cube(self):
        print(f"The square is: {self.n*self.n*self.n}")    
    def squarroot(self):
        print(f"The square is: {self.n**1/2}")    

n = int(input("Enter the value of n: "))
a = calculator(n) 
a.squar()
a.cube() 
a.squarroot()      
