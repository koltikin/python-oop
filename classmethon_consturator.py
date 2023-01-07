class Employe(object):

    num_of_Employe = 0
    raise_amount = 1.04

    def __init__(self, frist, last, pay):
        self.frist_name = frist
        self.last_name = last
        self.email = '{}.{}@gmail.com'.format(frist, last)
        self.pay = pay
        Employe.num_of_Employe += 1

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)

    @classmethod
    def set_raise_amount(cls, raise_amount):
        cls.raise_amount = raise_amount

    @classmethod
    def make_new_em(cls, em_str):
        name, last, pay = em_str.split("-")
        return Employe(name, last, pay)


em1_str = "ziya-kasgari-6500"
# name, last , pay = em1_str.split("-")
# em_1 = Employe(name, last , pay)
em_1 = Employe.make_new_em(em1_str)
em_2 = Employe.make_new_em(em1_str)

em_1.num_of_Employe = 8
print(em_1.last_name)
print(em_1.pay)
print(em_1.num_of_Employe)
print(Employe.num_of_Employe)
