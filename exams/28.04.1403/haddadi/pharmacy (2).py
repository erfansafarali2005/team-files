from datetime import datetime

class Pharmacy :
    p_name ='boali'
    p_loc = "qom , jomhory"
    p_phone = '32456789'
    medicines = []
    p_medicines = []
    p_value = 0
    personnel = []
    personnel_active =[]
    prescription =[]
    patients =[]
    p_order = []

    @staticmethod
    def about():
        print(f' <<{Pharmacy.p_name} Pharmacy >> \n Address :{Pharmacy.p_loc} \n Phone : {Pharmacy.p_phone}')
    
   
class Medicines:

    def __init__(self , i_name,i_year , i_expiration  , i_remaining ,i_price ) :
        self.name_drug =i_name
        self.production_year =i_year
        self.expiration_date = i_expiration
        self.remaining_date =i_remaining
        self.price =i_price
        Pharmacy.medicines.append((self.name_drug , self.expiration_date))
        Pharmacy.p_medicines.append(self)
        print('The drug was successfully registered .')

    @classmethod
    def init(cls ,i_name ,i_year ,i_expiration ,i_price)  :
        i_remaining = i_expiration - datetime.now().year 
        return cls(i_name ,i_year ,i_expiration ,i_remaining , i_price)



class Personnel :

    def __init__(self  , name , lname , phone,personnel_code) :
        self.name = name
        self.last_name = lname
        self.phone =phone
        self.personne_code = personnel_code
        Pharmacy.personnel.append(self.personne_code)
        Pharmacy.personnel_active.append(self.personne_code)
        select = input('welcome ... \n Do you want  to go to the menu section ?(y or n)')
        match select :
            case 'y':
                Personnel.menu(None)
            case 'n':
                exit()    
    
    @staticmethod
    def view_patient():
        print('patients ...')
        for item in Pharmacy.patients :
            print(item ,'\n')
        Personnel.menu(None)    

    @classmethod    
    def drug_registetation(cls , *args):
       pass 

    @staticmethod
    def view_drug():
        print('Drugs ...')
        for item in Pharmacy.medicines:
            print(item , '\n')
        Personnel.menu(None)

    @staticmethod
    def taking_leave():
        print('Taking leave ...')
        code =input('Pleas enter your personal code ...')
        for item in Pharmacy.personnel_active:
            if item == code :
                Pharmacy.personnel_active.remove(item)
                print('Your leave has been successfully registered .')
            else :
                print('Leave has already been registered for you .')   
        Personnel.menu(None)  
        
    @staticmethod
    def back_from_leave():
        print('returning from leave ...')
        code =input('Pleas enter your personal code ...')
        try :
            if code in Pharmacy.personnel :
                if code in Pharmacy.personnel_active   :
                    print('Your leave has been successfully cannelled.') 
                    Personnel.menu()
        except:
            print('Invalid code !')
   
           
    
    @staticmethod
    def view_prescription():
        print('prescriptions ...')
        for i in Pharmacy.prescription :
            print(i) 
       
        
    @staticmethod        
    def log_out():
        Personnel
            
    
    def menu(self):
        # print(f'Hello {self.name} {self.last_name}')  
        print("what are you going to do ? \n")
        select = input('1)drug registration \n 2)view the list of patients \n 3)view the list of medications \n 4)taking leave \n 5)back from leave \n 6)view list of prescription \n 7)log_out \n')
        
        match select :
            case '1':
                Personnel.drug_registetation()
            case '2':
                Personnel.view_patient()
            case '3':
                Personnel.view_drug()
            case '4':
                Personnel.taking_leave()
            case '5':
                Personnel.back_from_leave()
            case '6':
                Personnel.view_prescription()
            case '7':
                Personnel.log_out()

   

class Patients :
     
    patient_list =[]
    
    def __init__(self , p_name , p_lname , p_phone) :
        self.patient_name = p_name
        self.patient_lname = p_lname
        self.patient_phone = p_phone
        Pharmacy.patients.append((self.patient_name , self .patient_lname , self.patient_phone))

   
    @classmethod
    def provide_prescription(cls ,*args):
        for i in args  :
            Patients.patient_list.append(i)
        print('Your medications have been seccessfully registered .')

    @staticmethod    
    def order():

        for j in Patients.patient_list :
            Pharmacy.p_order.append(j)
            if j in Pharmacy.medicines:
                print(f'{j} medicine is available .')
                Pharmacy.p_value += j.p_medicines
            
            else:
                print(f'{j}  medicine is not  available .')
        Pharmacy.prescription.append(Patients.patient_list) 
        Patients.patient_list.clear()       

############################################################################################################################
drug1 =Medicines.init('mosaken' , '2024' , 2026 , 1200)    
drug2 =Medicines.init('jelofen' , '2024' , 2025, 1000) 

patient1 =Patients('reza' , 'asghary' , '097866555')

p1 =Personnel('roya' , 'rad' , '09365487409' ,'123')
p2 = Personnel('sahar' , ' rad' , '09051601761' , '124')



