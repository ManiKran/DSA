# heaps

class heap:
    def __init__(self):
        self.l=[0]
        self.size=0
        
    def insert_element(self,data):
        self.l.append(data)
        self.size+=1
        if self.size%2!=0:
            c=self.size
            while self.l[c]<self.l[(c-1)//2]:
                a=self.l[c]
                b=self.l[(c-1)//2]
                self.l[c]=b
                self.l[(c-1)//2]=a
                c=(c-1)//2
        else:
            c=self.size
            while self.l[c]<self.l[c//2]:
                a=self.l[c]
                b=self.l[c//2]
                self.l[c]=b
                self.l[c//2]=a
                c=c//2
                
    def Print(self):
        print(self.l)
        
h=heap()
h.insert_element(3)
h.insert_element(5)
h.insert_element(6)
h.insert_element(7)
h.insert_element(9)
h.insert_element(10)
h.insert_element(2)
h.Print()
