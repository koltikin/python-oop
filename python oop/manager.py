from employe import Employe

class Manager(Employe):
    man_of_mum = 0
    def __init__(self, name, last_name, pay, list_of_em = []) -> None:
        super().__init__(name, last_name, pay)
        self.list_of_em = list_of_em
        Manager.man_of_mum +=1 
  
    def add_empo(self, emp):
        if not(emp in self.list_of_em):
            self.list_of_em.append(emp)

    def remove_empo(self, emp):
        if emp in self.list_of_em:
            self.list_of_em.remove(emp)

    def get_emp_list(self):
        for emp in self.list_of_em:
            print(emp.first_name)

em1 = Employe("ziya", "yilmaz", 9500)
em2 = Employe.make_new_em("abdulhabir_akyol_9500")
man1 = Manager("ziya", "huseyin", 1500, [em1])
man1.add_empo(em2)

print(len(man1.list_of_em))
for h in man1.list_of_em:
    print(h.first_name)


print(Employe.em_num)
print(Manager.man_of_mum)
