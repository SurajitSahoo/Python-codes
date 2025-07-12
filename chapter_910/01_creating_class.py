class programmer:
    company = "Microsoft"
    def __init__(self, name, salary, pin):
        self.name = name
        self.salary = salary
        self.pin = pin
p = programmer("Surajit", 30000, 721124) 
print(p.name, p.salary, p.pin, p.company)       