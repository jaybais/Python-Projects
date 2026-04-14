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


Cookie_Monster = Customer()

Cookie_Monster.set_name("Cookie Monster")
print(f'Name: {Cookie_Monster.get_name()}')
Cookie_Monster.set_address("123 Sesame St. Unit A, Brooklyn, NY 45678")
print(f'Address: {Cookie_Monster.get_address()}')
Cookie_Monster.set_services("Ultimate TV (Baking Channel incld.), Gig Extra Internet, Xfinity Mobile")
print(f'Services: {Cookie_Monster.get_services()}')
Cookie_Monster.set_monthly_rate("$245.00")
print(f'Monthly Rate: {Cookie_Monster.get_monthly_rate()}')

print('\n')

Grover_Smith = Customer()

Grover_Smith.set_name("Grover Smith")
print(f'Name: {Grover_Smith.get_name()}')
Grover_Smith.set_address("123 Sesame St. Unit B, Brooklyn, NY 45678")
print(f'Address: {Grover_Smith.get_address()}')
Grover_Smith.set_services("Ultimate TV, 1 Gig Internet, Xfinity Voice Premium")
print(f'Services: {Grover_Smith.get_services()}')
Grover_Smith.set_monthly_rate("$165.00")
print(f'Monthly Rate: {Grover_Smith.get_monthly_rate()}')

print('\n')

Big_Bird = Customer()

Big_Bird.set_name("Big Bird")
print(f'Name: {Big_Bird.get_name()}')
Big_Bird.set_address("123 Sesame St. Unit C, Brooklyn, NY 45678")
print(f'Address: {Big_Bird.get_address()}')
Big_Bird.set_services("Popular TV, 500 Mbps Internet, Xfinity Mobile")
print(f'Services: {Big_Bird.get_services()}')
Big_Bird.set_monthly_rate("$125.00")
print(f'Monthly Rate: {Big_Bird.get_monthly_rate()}')