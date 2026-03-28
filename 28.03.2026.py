class User:
    def __init__(self,first_name,last_name,age):
        self.first_name = first_name
        self.last_name = last_name
        self.__age = age

    def get_age(self):#getter
        return self.__age

    def set_age(self,value):#setter
        if value < 0:
            return ValueError("Yosh manfiy bo'lmasligi lozim!")
        self.__age = value

luiza=User("Luiza","Olimjonova",15)

print(f"Yosh: {luiza.get_age()}")
luiza.set_age(25)
print(f"Yangi yosh: {luiza.get_age()}")