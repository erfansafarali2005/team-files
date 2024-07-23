
from datetime import datetime
class Pharmacy:
    def __init__(self, name, location):
        self.name = name
        self.location = location
        self.medicine = []
        self.patients = []
        self.employees = []
        self.prescriptions = []
        self.price = 0

    def add_patient(self, patient):
        self.patients.append(patient)

    def add_employee(self, employee):
        self.employees.append(employee)

    def sell_medicine(self, drug, quantity):
        self.price += drug.price * quantity

    def get_active_employees(self):
        return [employee for employee in self.employees if employee.active]



class medicine:
    def __init__(self, name, production, expiration, price):
        self.name = name
        self.pr = production
        self.ex = expiration
        self.price = price
    

    @classmethod
    def init(cls, name, production, expiration, price):
        now = datetime.now()
        end_datetime = datetime.strptime(expiration, '%Y-%m-%d')
        time_left = end_datetime - now
        if time_left.days <= 0:
            expiration_days = 0
        else:
            expiration_days = time_left.days
        return cls(name, production, expiration_days, price)
   





class Employee:
    def __init__(self, fname, lname, phone):
        self.fname = fname
        self.lname = lname
        self.phone = phone
        self.active = True





    def register_medicine(self, drug, pharmacy):
        pharmacy.medicine.append(drug)

    def view_patients(self, pharmacy):
        return pharmacy.patients

    def view_medicine(self, pharmacy):
        return pharmacy.medicine

    def get_lazy(self):
        self.active = False

    def be_active(self):
        self.active = True

    def view_prescriptions(self, pharmacy):
        return pharmacy.prescriptions
    






class Patient:
    def __init__(self, fname, last_name, phone):
        self.fname = fname
        self.lname = last_name
        self.phone = phone
        self.prescriptions = []

    def submit_prescription(self, pharmacy, *drugs):
        self.prescriptions.append(drugs)
        pharmacy.prescriptions.append(drugs)






med1 = medicine.init("Aspirin", "2023-01-01", "2025-01-01", 10)
med2 = medicine.init("Ibuprofen", "2023-01-02", "2025-01-01", 15)

emp1 = Employee("ahmad", "ahmadi", "123456789")
emp2 = Employee("asghar", "farhadi", "987654321")

pat1 = Patient("mamad", "khalaji", "123123123")
pat2 = Patient("mobin", "nasri", "321321321")

pharmacy = Pharmacy("matin pharmacy", "qom,bonyad")




pharmacy.add_employee(emp1)
pharmacy.add_employee(emp2)



pharmacy.add_patient(pat1)
pharmacy.add_patient(pat2)


emp1.register_medicine(med1, pharmacy)



pat2.submit_prescription(pharmacy, med1, med2)


pharmacy.sell_medicine(med1, 2)
pharmacy.sell_medicine(med2, 1)


###############################################################
print(pat1.prescriptions)
print(pat2.prescriptions)
print(pharmacy.employees)
print(pharmacy.medicine)
print(pharmacy.patients)
print(pharmacy.price)