bank = {}

class Bank:
  def __init__(self, bank):
    self.bank = bank

  def create_account(self,account_number,name):
   used = False
   for i in self.bank :
    if account_number==i:
     used=True
   if used==True:
     return "This account number has been taken"
   else:
      self.bank[account_number]= {"account name":name, "balance":0}
      return "Account created"

  def deposit_money(self,account_number,amount):
   check = False
   for i in self.bank:
     if account_number == i:
       check = True
   if check == True:
     self.bank[account_number]["balance"] = amount
     return "Your deposit was successful"
   else:
     return "This account does not exist! please check the account number provided"
   
  def withdraw_money(self,account_number,amount):
    check = False
    for i in self.bank:
     if account_number == i:
      check = True
    if check == True:
      if self.bank[account_number]["balance"] < amount:
        return "Insufficient balance"
      else:
        self.bank[account_number]["balance"] -= amount
        return "withdrawal successful"
    else:
        return "This account does not exist! please check the account number provided"

  def transfer_money(self,sender,receiver,amount):
    check1 = False
    check2 = False
    for i in self.bank:
      if sender == i:
        check1 = True
      if receiver == i:
        check2 = True
    if check1 and check2:
       if sender == receiver :
        return "You provided the same account for sender and receiver"
       elif self.bank[sender]["balance"] < amount:
        return "Insufficient balance"
       else:
        self.bank[sender]["balance"] -= amount
        self.bank[receiver]["balance"] += amount
        return "Transfer successful"
    elif check1 == False and check2:
     return f"Please double check the sender account number provided"
    elif check1 and check2 == False :
     return f"Please double check the receiver account number provided"
    else:
     return f"Please double check the account numbers provided"

  def check_balance(self,account_number):
    balance = self.bank[account_number]["balance"]
    return f"Your account balance is ${balance}"

  def list_all_accounts(self):
    list = []
    for i in self.bank:
      name = self.bank[i]["account name"]
      balance = self.bank[i]["balance"]
      list.append(f"account number:{i}, name:{name}, balance: {balance}")
    return "\n".join(list)

Mybank = Bank(bank)
print(Mybank.create_account("1445564","Godswill"))
print(Mybank.create_account("13324242","Godswill"))
print(Mybank.deposit_money("13324242",1200))
print(Mybank.withdraw_money("13324242",200000))
print(Mybank.transfer_money("13324242","1445564",1000))
print(Mybank.transfer_money("1445568","1445564",300000))
print(Mybank.check_balance("1445564"))
print(Mybank.list_all_accounts())
