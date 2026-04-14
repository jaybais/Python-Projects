class Customer():
    def __init__(self, name, address, services, monthly_rate):
        self.name = name       
        print(f'Name: {self.name}')

        self.address = address
        print(f'Address: {self.address}')

        self.services = services
        print(f'Services: {self.services}')

        self.monthly_rate = monthly_rate
        print(f'Monthly Rate: {self.monthly_rate}')


Cookie_Monster = Customer(
    "Cookie Monster", 
    "123 Sesame St. Unit A, Brooklyn, NY 45678", 
    "Ultimate TV (Baking Channel incld.), Gig Extra Internet, Xfinity Mobile", 
    "$245.00"
    )   

print('\n')

Grover_Smith = Customer(
    "Grover Smith", 
    "123 Sesame St. Unit B, Brooklyn, NY 45678", 
    "Ultimate TV, 1 Gig Internet, Xfinity Voice Premium", 
    "$165.00"
    )

print('\n')

Big_Bird = Customer(
    "Big Bird", 
    "123 Sesame St. Unit C, Brooklyn, NY 45678", 
    "Popular TV, 500 Mbps Internet, Xfinity Mobile", 
    "$125.00"
    )

class transfer_services(Customer):
    def __init__(self, name, address, services, monthly_rate, transfer_date):
        super().__init__(name, address, services, monthly_rate)   
        self.transfer_date = transfer_date     
        print(f'Transfer Date: {self.transfer_date}')   
    def update_address(self, address):   
        self.address = address
        print(f'New Address: {self.address}')   
    def update_services(self, services):   
        self.services = services
        print(f'New Services: {self.services}') 
    def update_monthly_rate(self, monthly_rate):   
        self.monthly_rate = monthly_rate
        print(f'New Monthly Rate: {self.monthly_rate}') 

print('\n')

print("Account Transfer Details:")
transfer_customer = transfer_services(
    "Big Bird", 
    "123 Sesame St. Unit C, Brooklyn, NY 45678", 
    "Popular TV, 500 Mbps Internet, Xfinity Mobile", 
    "$125.00", 
    "2026-10-01"
)

transfer_customer.update_address("456 Sesame St. Unit D, Brooklyn, NY 45678")
transfer_customer.update_services("1 Gig Internet, Xfinity Mobile)")
transfer_customer.update_monthly_rate("$75.00")    

