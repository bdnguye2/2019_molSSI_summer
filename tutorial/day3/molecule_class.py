#
#
# Purpose: write up a simple encapsulation to define a group of functions with
# similar functionality without the need write the function tens of times
#
#

class Molecule:
    # pass in name, charge, and symbol
    # Standard practice to name the pointer 'self'
    def __init__(self, name, charge, symbols):
        # prints out error and projects the class
        if isinstance(name, str):
            self.name = name
        else:
            raise TypeError('Name is not a string.')
        
        self.name = name
        self.charge = charge
        self.symbols = symbols

    def __str__(self):
        return 'name: '+str(self.name)+'\ncharge: '+str(self.charge)+'\nsymbols:'\
                +str(self.symbols)

# Sets a variable called water molecule that passes into the class
water = Molecule('water_molecule', 0.0, ['O','H','H'])
print(water)
print(water.__dict__,'\n')

# May directly specify the arguments (name, charge, & symbols) and doesn't
# matter where it is being defined
helium = Molecule(charge = 0.0,name = 'helium',symbols = 'He')
print(helium)
print(helium.__dict__,'\n')

# Type checking example with hydrogen and error will show up
hydrogen = Molecule(0.0,0.0, ['H'])
