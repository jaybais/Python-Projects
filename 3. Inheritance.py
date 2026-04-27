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


Thomas_OConnor = Customer(
    "Thomas O'Connor", 
    "123 Main St. Unit A, Brooklyn, NY 45678", 
    "Ultimate TV, Gig Extra Internet, Xfinity Mobile", 
    "$245.00"
    )   

print('\n')

Patrick_DeAngelo = Customer(
    "Patrick DeAngelo", 
    "521 King Ave., Brooklyn, NY 45678", 
    "Ultimate TV, 1 Gig Internet, Xfinity Voice Premium", 
    "$165.00"
    )

print('\n')

Kathleen_Davis = Customer(
    "Kathleen Davis", 
    "484 Circle Ln., Brooklyn, NY 45678", 
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
        print('\n')
        print(f'New Address: {self.address}')   
    def update_services(self, services):   
        self.services = services
        print(f'New Services: {self.services}') 
    def update_monthly_rate(self, monthly_rate):   
        self.monthly_rate = monthly_rate
        print(f'New Monthly Rate: {self.monthly_rate}') 

print('\n')

print("Account Transfer Details")
transfer_customer = transfer_services(
    "Kathleen Davis", 
    "484 Circle Ln., Brooklyn, NY 45678", 
    "Popular TV, 500 Mbps Internet, Xfinity Mobile", 
    "$125.00", 
    "2026-10-01"
)

transfer_customer.update_address("13 Country Rd., Virginia, WV 67891")
transfer_customer.update_services("1 Gig Internet, Xfinity Mobile)")
transfer_customer.update_monthly_rate("$75.00")    

