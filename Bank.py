class Bank:
    def getData(self):
        self.ano=int(input("Enter Number"))
        self.name=input("Enter Name")
        self.bal=int(input("Enter Balance"))
    def showData(self):
        print(self.ano)
        print(self.name)
        print(self.bal)
b1=Bank()
b1.getData()
b1.showData()



