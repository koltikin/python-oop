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

    @classmethod
    def make_new_em(cls,em_str):
        name, last , pay = em_str.split("-")
        return Employe(name, last , int(pay))


    def __add__(frist_emp, secode_emp):
        return frist_emp.pay + secode_emp.pay

    def __len__(self):
        return len(self.frist_name)

    def __repr__(self) -> str:
        return "it is created from --> Employe('{}','{}',{})".format(self.frist_name,
        self.last_name, self.pay)

    def __str__(self) -> str:
        return f"{self.frist_name}-{self.last_name}-{self.pay}"

em1_str = "ziya-kasgari-6500"
em2_str = "abdullah-yusuf-9500"
em_1 = Employe.make_new_em(em1_str)
em_2 = Employe.make_new_em(em2_str)

# print(em_1)
# print(str(em_1))
# print(em_1.__str__())

# print(repr(em_1))
# print(em_1.__repr__())

print(em_1 + em_2)
print(len(em_2))

