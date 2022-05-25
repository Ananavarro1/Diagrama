from ast import Str
from User import User

class customer(User):

    def _init_(self, user=User, name:Str , address:str, customerld:int, accountBalance:float):
        self.User = user 
        self.Name = name 
        self.Address = address
        self.Customerld = customerld
        self.AccountBalance = accountBalance