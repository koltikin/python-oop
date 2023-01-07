
import datetime

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
        return Employe(name, last , pay)

    @staticmethod
    def is_work_day(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        else:
            return True


my_date = datetime.date(2022,10,28)
my_date_1 = datetime.date(2022,10,29)
em_1 = Employe.make_new_em("ziya-kasgari-7800")
print(Employe.is_work_day(my_date))
print(em_1.is_work_day(my_date_1))