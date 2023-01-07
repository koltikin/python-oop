class Employe(object):
    num_of_Employe = 0
    raise_amount = 1.04

    def __init__(self, frist, last, pay):
        self.frist_name = frist
        self.last_name = last
        self.email = "{}.{}@gmail.com".format(frist, last)
        self.pay = pay
        self.full_name = "{} {}".format(self.frist_name, self.last_name)
        Employe.num_of_Employe += 1

    def full_name(self):
        print("{} {}".format(self.frist_name, self.last_name))

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)

    @classmethod
    def set_raise_amount(cls, raise_amount):
        cls.raise_amount = raise_amount

    @classmethod
    def make_new_em(cls, em_str):
        name, last, pay = em_str.split("-")
        return Employe(name, last, pay)

    def __str__(self):
        return f"{self.frist_name}\n{self.last_name}\n{self.pay}"


class Developer(Employe):
    num_of_developer = 0

    def __init__(self, frist, last, pay, dev_lang):
        super().__init__(frist, last, pay)
        self.dev_lang = dev_lang
        Developer.num_of_developer += 1

    def __str__(self):
        # return f"{self}\n{self.dev_lang}"
        return super.__str__(self) + "\n" + self.dev_lang


class Manager(Employe):
    num_of_manager = 0

    def __init__(self, frist, last, pay, em_list=None):
        super().__init__(frist, last, pay)
        if em_list is None:
            self.em_list = []
        else:
            self.em_list = em_list

        Manager.num_of_manager += 1

    def add_em(self, em):
        if em not in self.em_list:
            self.em_list.append(em)

    def remove_em(self, em):
        if em in self.em_list:
            self.em_list.remove(em)

    def print_emps(self):
        for empo in self.em_list:
            print("-----> ", empo.full_name)


dev_1 = Developer("ziya", "kasgari", 18000, "python")
dev_2 = Developer("abduhabir", "tograk", 25000, "java")

em_1 = Developer.make_new_em("ziya-kasgari-6800")
em_2 = Employe.make_new_em("abduhabir-tograk-9500")

manager_1 = Manager("ziya", "kasgari", 25_000)
manager_2 = Manager("perhat", "tursun", 30_000)

manager_1.add_em(em_1)
manager_1.add_em(em_2)

manager_1.remove_em(em_2)

# print(Employe.num_of_Employe)
# print(Developer.num_of_developer)
# print(Manager.num_of_manager)

# print(len(manager_1.em_list))
# print(manager_1.print_emps())

print(help(Developer))
print(em_1)
print(dev_2)
