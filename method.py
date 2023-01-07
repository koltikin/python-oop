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

    @classmethod
    def set_raise_amount(cls, raise_amount):
        cls.raise_amount = raise_amount

em_1 = Employe("ziya","kasgari",6500)
em_2 = Employe("ablet","kasgari",7500)
print(em_1.raise_amount)
em_1.raise_amount = 1.09
em_2.raise_amount = 1.02
Employe.set_raise_amount(1.08)
print(em_1.raise_amount)
print(em_2.raise_amount)
print(Employe.raise_amount)