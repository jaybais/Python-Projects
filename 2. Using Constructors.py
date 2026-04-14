# Using Constructors to Create Objects  V.2

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