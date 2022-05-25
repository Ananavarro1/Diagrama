from datetime import date


class User():
    
    def _init_(self, userid:int, password:str, registerDate:date ):
       self.Userid = userid 
       self.Password = password 
       self.RegisterDate = registerDate
