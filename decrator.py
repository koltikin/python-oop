class Employe(object):
    num_of_Employe = 0
    raise_amount = 1.04
    def __init__(self, frist, last, pay):
        self.frist_name = frist
        self.last_name = last
        self.pay = pay
        Employe.num_of_Employe +=1

    def apply_raise(self):
            self.pay = int(self.pay*self.raise_amount)


    @property
    def email(self):
        # print("full_name called!")
        return '{}.{}@gmail.com'.format(self.frist_name,self.last_name)

    @property
    def full_name(self):
        print("full_name called!")
        return f"{self.frist_name} {self.last_name}"

    @full_name.setter
    def full_name(self, name):
        frist, last = name.split(" ")
        self.frist_name = frist
        self.last_name = last

    @full_name.deleter
    def full_name(self):
        print(f"deleted {self.full_name}")
        self.frist_name = None
        self.last_name = None

em_1 = Employe("ziya","kasgari",5200)
em_2 = Employe("ablet","atus",7800)
em_3 = Employe("ablet","atus",7800)
em_4 = Employe("ablet","atus",7800)
# print(Employe.__dict__)
# print(em_1.__dict__)
# em_1.apply_raise()
# em_2.apply_raise()

# print(em_2.full_name)
print(em_2.email)
em_2.full_name = "alim zahir"
# print(Employe.num_of_Employe)
print(em_2.full_name)
print(em_2.email)

# del em_2
# del em_2.full_name
# print(em_2.full_name)