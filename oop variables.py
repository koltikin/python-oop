class Employe(object):
    num_of_Employe = 0
    raise_amount = 1.04
    def __init__(self, frist, last, pay):
        self.frist_name = frist
        self.last_name = last
        self.email = '{}.{}@gmail.com'.format(frist,last)
        self.pay = pay
        Employe.num_of_Employe +=1

    def apply_raise(self):
            self.pay = int(self.pay*self.raise_amount)

em_1 = Employe("ziya","kasgari",5200)
em_2 = Employe("ablet","atus",7800)
em_3 = Employe("ablet","atus",7800)
em_4 = Employe("ablet","atus",7800)
# print(Employe.__dict__)
# print(em_1.__dict__)
em_1.apply_raise()
em_2.apply_raise()
print(Employe.num_of_Employe)
print(em_2.pay)
