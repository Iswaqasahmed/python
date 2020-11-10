import re # imported regular expression module

class Regexp:    
    # def __init__(self):
    #     self.text = " ";
    def mobileParse(self,text):
        phoneNumber = re.compile('\d{4}-\d{4}-\d{3}')
        search  = phoneNumber.search(text)
        print(text)
        print("my number is founded ",search.group())




        



reg = Regexp()
reg.mobileParse('0341-257866546446')