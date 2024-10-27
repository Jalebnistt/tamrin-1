class CustomStr:
     def init(self, string):
         self.string = string

     def set(self, index, str_value):
        mylist=list(self.string)
        if index < 0 or index >= len(mylist):
            print("eror")
        mylist[index]=str_value
        self.string = ''.join(mylist)
 
     def ispalindrome(self):
        mylist = list(self.string)
        mylist2 = mylist[::-1] 
        string2 = ''.join(mylist2)

 
        if self.string == string2:
            return True
        else:
            return False

     def isfloat(self):
        try:
            float(self.string) 
            return True
        except :
            return False
 
     def str(self):
        return self.string