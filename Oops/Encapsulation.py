class BankAccount:
    def __init__(self,account_number,balance):
        self.__account_number = account_number;
        self.__balance = balance;

    def deposit(self,amount):
        if amount > 0:
            self.__balance += amount;
            print(f"Deposited : {amount}, New Balance: {self.__balance}")
        else:
            print("Invalid Deposited amount");

    def withdraw(self,amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount;
            print(f"Withdrawn: {amount} , Remaining Balance: {self.__balance}");
        else:
            print("Invalid withdrawl")

    def get_balance(self):
        return self.__balance
    

account = BankAccount("12345",50000);
account.withdraw(20000);
account.deposit(30000);
print("Final Answer:", account.get_balance());

