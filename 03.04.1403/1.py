import time

class Shop:

    name = 'khanomi shop'
    loc = 'iran , qom , azar washaington'
    shop_value = 0
    clients_list = []

    @staticmethod
    def about_us():
        print(f"this is about_us vew {Shop.name} {Shop.loc}")  

    @staticmethod
    def show_clients():
        print(f'clients are {Shop.clients_list}')    


class Product:
    shop_name = Shop.name
    products = []

    def __init__(self , i_name , i_amount , i_quality , i_price , i_color):

        print("creating your Product")

        self.product_name = i_name
        self.product_amount = i_amount
        self.product_quality = i_quality
        self.product_price = i_price
        self.product_color = i_color
        
        Shop.shop_value+= self.product_price
        Product.products.append(self)

        print(f"your product registered with {self.product_name} and {self.product_amount} ")


    def info(self):
        print("gattering your info about the product")

        print(f"the {self.product_name} with {self.product_amount} quantity with {self.product_price} also its quality is {self.product_quality}")
        


    def __str__(self):
        return self.product_name

class Shirt(Product):
    product_name = 'shirt'
    
    def __init__(self , i_amount , i_quality , i_price , i_color):

        print("registering your shirt")
        time.sleep(5)
        super().__init__(self.product_name ,i_amount , i_quality , i_price , i_color)
        print(f'your {self.product_name} tshirt with color of {self.product_color} is registered now')


class Pants(Product):   
    product_name = 'pants'

    def __init__(self , i_amount , i_quality , i_price , i_color):

        print("registering your pants")      
        time.sleep(5)
        super().__init__(self.product_name , i_amount , i_quality , i_price , i_color)
        print(f'your {self.product_name} pants with color of {self.product_color} is registered now')


class Shoes(Product):   
    product_name = 'shoes'

#                                                                    ^-> unique proeprty
    def __init__(self , i_amount , i_quality , i_price , i_color , i_pairs):

        print("registering your shoes")      
        time.sleep(5)
        self.pairs = i_pairs
        super().__init__(self.product_name , i_amount , i_quality , i_price , i_color)
        print(f'your {self.product_name} shoes with color of {self.product_color} is registered now')      

class Client :
    successfully_purchased = [] # can be a dictionary in order to have access to the فاکتور
    client_cart = []

    def __init__(self , i_name , i_lname ,i_wallet , i_phone , i_email):
        print("Registering your credentials...")
        time.sleep(5)
        self.client_name = i_name
        self.client_lname = i_lname
        self.client_wallet = i_wallet
        self.client_phone = i_phone
        self.client_email = i_email
        print("you are successfully registered , welcome to our shop")
        Shop.clients_list.append(f'{self.client_name} with {self.client_phone}')

    @classmethod
    def init(cls , i_name , i_lname , i_wallet , i_phone ):
        i_email = f'{i_name}{i_lname}@gmail.com'
        return cls(i_name , i_lname , i_wallet , i_phone , i_email)
    
    def add_cart(self , *args):
        #cart = [str(item) for item in args if self.client_wallet > item.product_price]  !!! we need generator here
    
        print("purchasing ...")
        time.sleep(2)

        try : 
            for item in args :
                self.client_cart.append(item)
                print(f"{item.product_name} with succussfully addded into cart")
        except :
            print("error while adding products into the cart please try again later")


    def purchase(self):
        final_price = 0

        for item in self.client_cart :
            final_price += item.product_price

        if final_price < self.client_wallet:
            for item in self.client_cart :
                if item.product_amount > 0:
                    print(f"you successfully purchased the {item.product_name} for {item.product_price}")
                    self.successfully_purchased.append(item.product_name)
                    item.product_amount -= 1
                    self.client_wallet -= item.product_price

                else:
                    print(f"the product {item.product_name} is out of stock")
        else:
            print("you don't have enough money ... go and find a job bipole badbakht")
        """
            for item in sellf.client_cart : 
                print(f"you successuflly purchased the {item.product_price}")
                successfully_purchased.update(item.product_name , {"color" : item.product_name ,
                                                                   "quality" : item.product_color
                                                                })                
        """        
    
    def what_can_i_buy(self):
        the_list = [item for item in Product.products]

        for item in the_list:
            if item.product_price > self.client_wallet :
                print(f"you can't buy the {item.product_name}")
            else : 
                print(f"you can buy the {item.product_name}") 

    def clear_cart(self):
        try : 
            self.client_cart.clear()
            print("cart successfully cleared")
        except:
            print("there was an error in clearing your cart ..")    

###########################################################################################################

tshirt_jeans = Shirt(50 , 'jeans' , 1000 , 'blue' )
tshirt_makhmal = Shirt(40 , 'makhmal' , 2000 , 'meshki' )
tshirt_baggy = Shirt(30 , 'baggy' , 5000 , 'nokmedadi' )

pants_baggy = Pants(20 , 'nakh' , 2000 , 'black')
pants_slash = Pants(30 , 'jeans' , 1000 , 'green')

shoes_allstar = Shoes(20 , 'charm' , 3000 , 'white' , True)
shoes_katoni = Shoes(40 , 'polymer' , 2000 , 'red' , True)

client1 = Client.init('mamad' , 'gholi' , 10000 , '09373260257')
client2 = Client.init('asqar' , 'kobra' , 40000 , '09016492293')


client1.add_cart(tshirt_baggy , pants_baggy , shoes_katoni)
client1.purchase()


print(client1.successfully_purchased)
client1.clear_cart()

Shop.show_clients()

Shop.about_us()


print(client1.client_wallet)