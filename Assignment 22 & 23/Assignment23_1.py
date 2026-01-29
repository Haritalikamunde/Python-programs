class BookStore:
    NoOfBooks=0

    def __init__(self,BookName, AuthorName):
        self.Name=BookName
        self.Author=AuthorName

        BookStore.NoOfBooks+=1

    def Display(self):
        print(f"{self.Name} by {self.Author} No of Books is :{ BookStore.NoOfBooks}")
        

if __name__=="__main__":
    obj1=BookStore("Linux system Programming","Robert Love")
    obj1.Display()


    obj2=BookStore("C Programming","Dennis Ritchie")
    obj2.Display()
