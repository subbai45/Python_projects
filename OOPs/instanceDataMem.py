try:
    class MulTable():
        def read_table(self):
            self.n = int(input("Enter the table number: "))

        def display_table(self):
            if self.n <= 0:
                print(f"{self.n} is Invalid Input")
            else:
                print("=" * 20)
                print(f"{self.n}th Table ")
                print("=" * 20)
                for i in range(1, 11):
                    print(f"\t{self.n} x {i} = {self.n * i}")
                print("=" * 20)



    #Main Program

    mul = MulTable()
    mul.read_table()
    mul.display_table()

except ValueError:
    print("please enter valid input")