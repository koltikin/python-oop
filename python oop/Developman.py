
from employe import Employe

class Developman(Employe):
    dev_num = 0
    def __init__(self, name, last_name, pay, dev_lang) -> None:
        super().__init__(name, last_name, pay)
        self.dev_lang_name = dev_lang
        Developman.dev_num +=1


    @property
    def dev_lang(self):
        return self.dev_lang_name

    @dev_lang.setter
    def dev_lang(self, new_dev_lang):
        self.dev_lang_name = new_dev_lang
        return self.dev_lang_name

    
    @classmethod
    def make_new_dev(cls, dev_str):
        first, last, pay, dev_lang = dev_str.split("_")
        return cls(first, last, int(pay), dev_lang)


    
# dev1 = Developman("ziay","yilmaz", 6400,"python")
# dev2 = Developman.make_new_dev("abdullah_ali_6400_python")

# print(dev2.dev_lang)
# print(dev1.dev_num)



