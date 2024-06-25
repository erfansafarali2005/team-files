import time

class Hospital : 
    name = 'shahid safarali'
    loc = 'aqaqiya'
    rooms_count = 50
    date_created = '1383'
    employee_list = []
    active_employee_list = []
    overal_patient_list = []
    active_patient_list = []
    overal_income = 0
    jobs = ['doctor' , 'nurse' , 'accpompliment']
    sickness = ['cold' , 'notok' , 'cancer' , 'fluid']
    price_of_bastary = 1000

    @staticmethod
    def show_active_patients():
        for a_p in Hospital.active_patient_list :
            print(f'{a_p.patient_name} is now in the hospital')

    @staticmethod
    def show_overal_patients():
        for o_p in Hospital.overal_patient_list:
            print(f'{o_p.patient_name} is a pateint')

    @staticmethod
    def type_of_sick(obj):
        print("i need some of your infromations ...")
        print('1)i got cold \n 2)i feel not ok \n 3)i have cancer \n 4)i have fluid \n')
        u_input = input(" ... : ")

        match u_input:
            case 1:
                time.sleep(1)
                print('so you got cold')
                return Hospital.sickness[0]
            case 2:
                time.sleep(1)
                print('you feel bad')
                return Hospital.sickness[1]
            case 3:
                time.sleep(1)
                print('so you got cancer')
                return Hospital.sickness[2]
            case 4:
                time.sleep(1)
                print('so you got fluid')
                return Hospital.sickness[3]

            
        print("ok wait for a minutes")
        time.sleep(2)
        

    @staticmethod
    def employeetype():
            print(f"welcome to {Hospital.name} employee , whats your job ?")
            print('1)doctor \n 2)nurse \n 3)acompliment \n')
            u_input = input(" ... : ")

            match u_input:
                case 1:
                    return Hospital.jobs[0]
                case 2:
                    return Hospital.jobs[1]
                case 3:
                    return Hospital.jobs[2]

            
            print("ok wait for a minutes")
            time.sleep(2)
            

############################################################################################3

class Employee:
    def __init__(self , i_name , i_lname , i_phone ,i_type, i_email):
        print("welcome employee authenticating ...")
        self.employee_name = i_name
        self.employee_lname = i_lname
        self.employee_phone = i_phone
        self.employee_type = i_type
        self.employee_email = i_email
        
        Hospital.employee_list.append(self)
        Hospital.active_employee_list.append(self)

        time.sleep(2)
        print(f"welcome {self.employee_name}")
    @classmethod
    def init(cls, i_name , i_lname , i_phone):
        i_email = f'{i_name}{i_lname}@gmail.com'
        i_type = Hospital.employeetype()
        return cls(i_name , i_lname , i_phone , i_type , i_email)

    @staticmethod
    def show_all_patients():
        Hospital.overal_patient_list()


    def off(self):
        try:
            print("offing you off ...")
            Hospital.active_employee_list.remove(self)
            time.sleep(2)
            print("you are off now , enjoy vacations ! ")
        except:
            print("you are already offed...")
    def back_off(self):
        if self not in  Hospital.active_employee_list :
            print("backing you off ...")
            Hospital.active_employee_list.append(self)
            time.sleep(2)
            print("your back ! good")
        else : 
            print("you are already back ! ")    

    @staticmethod
    def bastary_patient(obj):
        print("bastariing the patient ...")
        time.sleep(1)

        if obj.patient_wallet > Hospital.price_of_bastary :

            print("you have enough money so you are bastray now !")
            Hospital.active_patient_list.append(obj)
            Hospital.overal_income += Hospital.price_of_bastary
        else:
            print('you dont have enough money to be bastary in the hospital')    

    @staticmethod
    def release_patient(obj):
        if obj  in Hospital.active_patient_list:
            print("releasing the patient...")
            time.sleep(1)
            Hospital.active_patient_list.remove(obj)
        else :     
            print(f"this patient with name of {obj.patient_name} is not actively bastary")


######################################################################################################

class Patient:
    def __init__(self):
        print('welcome to our hostpital ...')

        

    def signup(self , i_name , i_lname , i_phone , i_age , i_sickness , i_wallet):
        print("siginig you up !")
        self.patient_name = i_name
        self.patient_lname = i_lname
        self.patient_phone = i_phone
        self.patient_age = i_age
        self.patient_situation = i_sickness
        self.patient_wallet = i_wallet

        # inaj zadam chon toye __init__ moghe tashkil hanoz self i tashkil nashode (etelaat nadarim)
        Hospital.overal_patient_list.append(self)

        time.sleep(1)

        print("you are signed up now !")

    def init(self , i_name , i_lname , i_phone , i_age , i_wallet):

        i_sickness = Hospital.type_of_sick(self)

        return self.signup(i_name , i_lname , i_phone , i_age , i_sickness , i_wallet) 


##################################################################################################

ep1 = Employee.init('dr mamad' , 'gholami' , '09373260257')
ep2 = Employee.init('dr reza' , 'rezai' , '09373260257')

ep1.off()
ep1.back_off()


p1 = Patient() # it needs the self so first lest create that
p1.init('erfan' , 'safarali' , '09016492293' , 20 , 2000)


ep1.bastary_patient(p1)
ep1.release_patient(p1)

print(Hospital.active_employee_list)
print(Hospital.active_patient_list)
print(Hospital.employee_list)
print(Hospital.overal_income)
print(Hospital.overal_patient_list)
