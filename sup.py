class dog:
    sound="bark" #class variable
    legs=4

    def __init__(self,name,breed):
        self.name=name
        self.breed=breed


    def get_info(self):
        return"{}-{}".format(self.name,self.breed)

d1 = dog("laika", "japanesespitz")
d1.legs = 3


d2 = dog("churpi", "pomerian")

print(d1.get_info(), d1.sound, d1.legs)
print(d2.get_info(), d2.sound, d2.legs)




