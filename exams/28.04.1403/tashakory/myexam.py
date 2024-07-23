from datetime import date

class Pharmesy:
    name = 'dr akbari'
    loc = 'qom'
    medicines = []
    patients = []
    active_employees = []
    employees = []
    prescriptions_list = []
    total_income = 0  
    
    @staticmethod
    def show_pharmacy():
        return f'Welcome to {Pharmesy.name} at {Pharmesy.loc} city'
    
    @staticmethod
    def buy_medicine(medicine):
        Pharmesy.total_income += medicine.price
        print(f'Bought {medicine.name} for {medicine.price}.')

class Daro:
    def __init__(self, name, year, exp, price):
        self.name = name
        self.year = year
        self.exp = exp
        self.price = price
        if self not in Pharmesy.medicines:
            Pharmesy.medicines.append(self)
        
    @classmethod
    def init(cls, name, year, price):
        exp = date.today().year - year
        return cls(name, year, exp, price)

    def __str__(self):
        return f'{self.name} (Year: {self.year}, Exp: {self.exp} years, Price: {self.price})'

class Employee:
    def __init__(self, name, lastname, phone):
        self.name = name
        self.lastname = lastname
        self.phone = phone
        self.active = True
        
        Pharmesy.employees.append(self)
        Pharmesy.active_employees.append(self)
        
    @staticmethod   
    def show_patients():
        return f'These are the list of our patients: {[str(patient) for patient in Pharmesy.patients]}'
    
    @staticmethod
    def show_medicines():
     medicines_list = [f'{medicine.name}: {medicine.price}' for medicine in Pharmesy.medicines]
     return f'These are the list of medicines: {medicines_list}'

    
    @staticmethod
    def show_prescriptions():
        return f'These are the list of prescriptions: {Pharmesy.prescriptions_list}'
    
    @staticmethod
    def show_income():
        return f'Total income: {Pharmesy.total_income}'  
    
    def add_medicine(self, *args):
        for med in args:
            if med not in Pharmesy.medicines:
                Pharmesy.medicines.append(med)
                print(f'Added medicine: {med.name}')
            
    def go_off(self):
        if self.active:
            print("you are going to go off")
            Pharmesy.active_employees.remove(self)
            self.active = False
            print("You are off now")
        else:
            print("You are already offed...")
    
    def back_off(self):
        if not self.active:
            print("You are backing off")
            Pharmesy.active_employees.append(self)
            self.active = True
            print("You're back")
        else: 
            print("You are already back")
    
    def __str__(self):
        return f'{self.name} {self.lastname} (Phone: {self.phone})'

class Patient:
    prescriptions = []  

    def __init__(self, name, lastname, phone):
        self.name = name
        self.lastname = lastname
        self.phone = phone
        Pharmesy.patients.append(self)
        
    def give_prescription(self, prescription):
        self.prescriptions.append(prescription)  
        Pharmesy.prescriptions_list.append(prescription)  
        print(f'Prescription added: {prescription}')
        print(Pharmesy.prescriptions_list)
    
    def __str__(self):
        return f'{self.name} {self.lastname} (Phone: {self.phone})'

# Sample Usage
d1 = Daro.init('antibiotic', 2020, 50)
d2 = Daro.init('painkiller', 2021, 30)

em1 = Employee('Ali', 'Amiri', '8383763')
em1.add_medicine(d1, d2)

print(Employee.show_medicines())

Pharmesy.buy_medicine(d1)
Pharmesy.buy_medicine(d2)

pat1 = Patient('Reza', 'Nazari', '123456789')
pat1.give_prescription('Prescription 1')

pat2 = Patient('Ali', 'Ahmadi', '76363535')
pat2.give_prescription('Prescription 2')

print(Employee.show_patients())
print(Employee.show_medicines())
print(Employee.show_prescriptions())
print(Employee.show_income())  

em1.go_off()
em1.back_off()

#########################################################################
print(pat1.prescriptions)
print(pat2.prescriptions)
##########################################################################

"""

    weakness in prescription system , it should gets drug objects by args 

    GPT code Spotted


"""