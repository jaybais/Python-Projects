class Customer(): 
    def set_name(self, name):   
        self.name = name  
    
    def get_name(self):        
        return self.name     
    
    def set_address(self, address):  
        self.address = address
    
    def get_address(self):     
        return self.address
    
    def set_services(self, services):
        self.services = services
    
    def get_services(self):
        return self.services
    
    def set_monthly_rate(self, monthly_rate):
        self.monthly_rate = monthly_rate
    
    def get_monthly_rate(self):
        return self.monthly_rate


Thomas_OConnor = Customer()

Thomas_OConnor.set_name("Thomas O'Connor")
print(f'Name: {Thomas_OConnor.get_name()}')
Thomas_OConnor.set_address("123 Main St. Unit A, Brooklyn, NY 45678")
print(f'Address: {Thomas_OConnor.get_address()}')
Thomas_OConnor.set_services("Ultimate TV, Gig Extra Internet, Xfinity Mobile")
print(f'Services: {Thomas_OConnor.get_services()}')
Thomas_OConnor.set_monthly_rate("$245.00")
print(f'Monthly Rate: {Thomas_OConnor.get_monthly_rate()}')

print('\n')

Patrick_DeAngelo = Customer()

Patrick_DeAngelo.set_name("Patrick DeAngelo")
print(f'Name: {Patrick_DeAngelo.get_name()}')
Patrick_DeAngelo.set_address("521 King Ave., Brooklyn, NY 45678")
print(f'Address: {Patrick_DeAngelo.get_address()}')
Patrick_DeAngelo.set_services("Ultimate TV, 1 Gig Internet, Xfinity Voice Premium")
print(f'Services: {Patrick_DeAngelo.get_services()}')
Patrick_DeAngelo.set_monthly_rate("$165.00")
print(f'Monthly Rate: {Patrick_DeAngelo.get_monthly_rate()}')

print('\n')

Kathleen_Davis = Customer()

Kathleen_Davis.set_name("Kathleen Davis")
print(f'Name: {Kathleen_Davis.get_name()}')
Kathleen_Davis.set_address("484 Circle Ln., Brooklyn, NY 45678")
print(f'Address: {Kathleen_Davis.get_address()}')
Kathleen_Davis.set_services("Popular TV, 500 Mbps Internet, Xfinity Mobile")
print(f'Services: {Kathleen_Davis.get_services()}')
Kathleen_Davis.set_monthly_rate("$125.00")
print(f'Monthly Rate: {Kathleen_Davis.get_monthly_rate()}')