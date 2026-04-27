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