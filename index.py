class Person:
    def __init__(self,name,age,gender):
          
          self.name=name
          self.age=age
          self.gender=gender     
   
    def introduce(self):
         print("Your name is ", self.name, " you are ", self.age, " years old", " and belong to the ", self.gender, " gender") 
         
         

thisPesron=Person("olumide", 30, "male")

thisPesron.introduce()         