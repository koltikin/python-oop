class Employe():
    raise_amount = 1.04
    em_num = 0
    def __init__(self, name, last_name, pay) -> None:
        self.first_name = name
        self.last_name = last_name
        self.full_nane = f"{name} {last_name}"
        self.email = f"{name}.{last_name}@gmai.com"
        self.pay = pay
        Employe.em_num +=1


    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    
    @full_name.setter
    def full_name(self, full_name):
        first ,last = full_name.split(" ")
        self.first_name = first
        self.last_name = last

        self.email = f"{first}.{last}@gmail.com"

    @full_name.getter
    def full_name(self):
        return f"boldima---> {self.first_name} {self.last_name}"



    def applay_raise(self, raise_amount = raise_amount):
        self.pay*=raise_amount
        self.pay = int(self.pay)

    @classmethod
    def set_raise(cls, raise_amount):
        cls.raise_amount = raise_amount

    @classmethod
    def make_new_em(cls, em_str):
        first, last, pay = em_str.split("_")
        return cls(first, last, int(pay))

    # full_name = property(set_full_name, get_full_name)



em1 = Employe("ziya", "kasgari", 6900)
# em2 = Employe("ziya", "kasgari", 6900)
# em1 = Employe.make_new_em("ziya_kasgari_6900")
# em2 = Employe.make_new_em("abdulhabir_akyol_5400")

em1.full_name = "hakan telva"
em1.first_name = "cuskun"
# em1.raise_amount = 1.09
# em1.applay_raise()
print(em1.full_name)
# print(em1.pay)
# print(em2.em_num)



    


