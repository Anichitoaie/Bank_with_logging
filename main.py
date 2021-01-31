
import logging
import traceback
import inspect
def get_function_name():
    return traceback.extract_stack(None, 2)[0][2]

def get_function_parameters_and_values():
    frame = inspect.currentframe().f_back
    args, _, _, values = inspect.getargvalues(frame)
    return ([(i, values[i]) for i in args])

class User:

    def __init__(self,user_name,password):
        self.user_name=user_name
        self.password = password

class account():

    def createAccount(self,user_name):
        self.user_name=user_name
        self.accNo=user_name
        self.accNo += "_" + str(input("Enter the account no : "))
        loop=1
        while loop==1:
            try:
                self.deposit = int(input("Enter The Initial amount :"))
                loop=0
            except ValueError:
                print("invalid input")
        print("\nAccount Created")
        logging.info('call function ' + get_function_name() + '(' + str(get_function_parameters_and_values()) + ')-->')

    def add_initial_sum_to_register(self,initial_sum_register,accNr):

        self.initial_sum_register = initial_sum_register
        self.accNr = accNr
        self.initial_sum_register[self.accNo]=self.accNr
        logging.info('call function ' + get_function_name() + '(' + str(get_function_parameters_and_values()) + ')-->')
        return  self.initial_sum_register

    def add_to_register(self,account_register,user_name):

        self.account_register = account_register
        self.user_name=user_name

        if self.user_name not in self.account_register:
            self.account_register[self.user_name]=[]
        self.account_register[self.user_name].append(self.accNo)
        logging.info('call function ' + get_function_name() + '(' + str(get_function_parameters_and_values()) + ')-->')
        return  self.account_register

    def count_nr_of_acc_per_user(self,user_name):
        count=0
        for key in  self.account_register[user_name]:
            count+=1
            print("Account "+key+" has a value of "+ str(initial_sum_register[key])+"$")
        print("user:"+user_name+" has "+str(count)+" accounts")
        logging.info('call function ' + get_function_name() + '(' + str(get_function_parameters_and_values()) + ')-->')

def Add_user():

    a=input("Insert your user name:")
    b=input("Insert your password:")
    added_user=User(a,b)
    logging.info('call function ' + get_function_name() + '(' + str(get_function_parameters_and_values()) + ')-->')
    return  added_user

def Add_account(user_name):

    new_acc=account()
    new_acc.createAccount(user_name)
    logging.info('call function ' + get_function_name() + '(' + str(get_function_parameters_and_values()) + ')-->')
    return new_acc

def Addcurrency(user_name):

    add = ''
    add += user_name + "_" + str(input("Type the nr of the account you want to add: "))
    loop = 1
    while loop == 1:
        try:
            add_to_acc = int(input("How much to add:"))
            loop = 0
        except ValueError:
            print("invalid input")

    logging.info('call function ' + get_function_name() + '(' + str(get_function_parameters_and_values()) + ')-->')
    for i in range(len(Account)):
        if add in Account[i].accNo:
            initial_sum_register[add]=str(int(initial_sum_register[add])+add_to_acc)

def Withdrawcurrency(user_name):

    withdraw = ''
    withdraw += user_name + "_" + str(input("Type the nr of the account you want to withdraw: "))
    loop =1
    while loop == 1:
        try:
            withdraw_from_acc = int(input("How much to withdraw:"))
            loop = 0
        except ValueError:
            print("invalid input")

    logging.info('call function ' + get_function_name() + '(' + str(get_function_parameters_and_values()) + ')-->')
    for i in range(len(Account)):
        if withdraw in Account[i].accNo:
            initial_sum_register[withdraw] = str(int(initial_sum_register[withdraw]) - withdraw_from_acc)

def Transfercurrency(user_name,to_whom):

    acc_to_transfer_from = ''
    acc_to_transfer_from += user_name + "_" + str(input("Type the nr of the account you want to transfer from: "))
    if acc_to_transfer_from not in initial_sum_register:
        print("Account does not exist")
        return
    acc_to_transfer_to = ''
    acc_to_transfer_to += to_whom + "_" + str(input("Type the nr of the account you want to transfer to: "))
    if acc_to_transfer_to not in initial_sum_register:
        print("Account does not exist")
        return
    loop = 1
    while loop == 1:
        try:
            sum = int(input("How much you want to transfer: "))
            loop = 0
        except ValueError:
            print("invalid input")

    logging.info('call function ' + get_function_name() + '(' + str(get_function_parameters_and_values()) + ')-->')
    for i in range(len(Account)):
        if acc_to_transfer_from in Account[i].accNo:
            initial_sum_register[acc_to_transfer_from]=str(int(initial_sum_register[acc_to_transfer_from])-sum)
            initial_sum_register[acc_to_transfer_to]=str(int(initial_sum_register[acc_to_transfer_to])+sum)

def AverageValue():

    if Account == [] or conf_username  not in account_register:
        print("Make some accounts first")
    else:
        avg = 0
        counter = 0
        for char in initial_sum_register:
            avg += int(initial_sum_register[char])
            counter += 1
        avg = avg/counter
        logging.info('call function ' + get_function_name() + '(' + str(get_function_parameters_and_values()) + ')-->')
        print("The average sum of all accounts is :"+str(avg))

def TotalValue():

    if Account == [] or conf_username  not in account_register:
        print("Make some accounts first")
    else:
        total = 0

        for char in initial_sum_register:
            total += int(initial_sum_register[char])

        logging.info('call function ' + get_function_name() + '(' + str(get_function_parameters_and_values()) + ')-->')
        print("The total sum of all accounts is :" + str(total))

def MaxValue():

    if Account == [] or conf_username  not in account_register:
        print("Make some accounts first")
    else:
        max = 0

        for char in initial_sum_register:
            if int(initial_sum_register[char])>max:
                max = int(initial_sum_register[char])
                char_rich = char
        logging.info('call function ' + get_function_name() + '(' + str(get_function_parameters_and_values()) + ')-->')
        print("The account " + char_rich + " with "+str(max)+"value,is the wealthiest account")


loop=True
user_count = 0
user_array = []
user_nr_account = 0
account_register = {}
initial_sum_register = {}
Account = []
acc = 0
s1 = 1
s2 = 0
s3 = 0

logging.basicConfig(filename='logs.log', level=logging.DEBUG,format='%(asctime)s-> %(message)s',
                            datefmt='%m-%d-%Y %H:%M:%S')
while loop:
    if s1 == 1:
        print("\tU:ADD USER")
        print("\tA:ACCOUNT STATISTICS")
        print("\tE:EXIT")
        print("\n\n\n\n")
        decision = input("Please select an option by typing the  value:")

        if decision == "U":
            user_array.append(Add_user())
            user_count += 1
            s1 = 0
            s2 = 1
        if decision == "A":
            AverageValue()
        if decision == "E":
            loop = False
    if s2 == 1:
        print("\tU:ADD USER")
        print("\tL:LOGIN")
        print("\tA:ACCOUNT STATISTICS")
        print("\tE:EXIT")
        print("\n")
        decision = input("Please select an option by typing the corresponding value:")

        if decision == "U":
            user_array.append(Add_user())
            user_count += 1
        if decision == "L":
            login_succes=False
            while not login_succes:
                conf_username = input("Please insert username to log in:")
                conf_password = input("Please insert password to log in:")
                for i in range(user_count):
                    if conf_username in user_array[i].user_name and conf_password in user_array[i].password:
                        print("login successfully")
                        login_succes=True
                        s2 = 0
                        s3 = 1
                        break
                if login_succes is True:
                    break
                else:

                    print("Login attempt failed,try again")
                    login_succes = True

        if decision == "A":
            AverageValue()
            TotalValue()
            MaxValue()

        if decision == "E":
            loop = False
    if s3 == 1:
        print("\n\nHELLO "+conf_username)
        print("\tC:CREATE NEW ACCOUNT")
        print("\tD:DELETE ACCOUNT")
        print("\tAL:ACCOUNT LIST")
        print("\tAD:ADD TO ACCOUNT")
        print("\tW:WITHDRAW FROM ACCOUNT")
        print("\tT:TRANSFER")
        print("\tL:LOG OUT")
        print("\tE:EXIT")
        print("\n")
        decision = input("Please select an option by typing the corresponding value:")
        if decision == "C":
            user_nr_account += 1
            Account.append(Add_account(conf_username))
            print(Account[acc].add_to_register(account_register,conf_username))
            print(Account[acc].add_initial_sum_to_register(initial_sum_register, Account[acc].deposit))
            acc += 1

        if decision == "L":
            user_nr_account = 0
            s2 = 1
            s3 = 0
        if decision == "D":
            if Account == [] or conf_username  not in account_register:
                print("No accounts available")
            else:
                delete = ''

                delete += conf_username+"_"+str(input("Type the nr of the account you want to delete: "))

                for i in range(len(Account)):
                    print(Account[i].accNo)
                    if delete in Account[i].accNo:
                        Account.pop(i)
                        account_register[conf_username].remove(delete)
                        del initial_sum_register[delete]
                        acc = acc-1
                        break


        if decision == "AL":
            if Account == [] or conf_username  not in account_register:
                print("No accounts available")
            else:
                for i in range(acc):
                    if conf_username in Account[i].user_name:
                        Account[i].count_nr_of_acc_per_user(conf_username)
                        break
        if decision == "AD":
            if Account == [] or conf_username  not in account_register:
                print("No accounts available")
            else:
                Addcurrency(conf_username)
        if decision == "W":
            if Account == [] or conf_username  not in account_register:
                print("No accounts available")
            else:
                Withdrawcurrency(conf_username)
        if decision == "T":
            if Account == [] or conf_username  not in account_register:
                print("No accounts available")
            else:
                to_whom=input("Type the user you want to transfer:")
                if to_whom not in account_register:
                    print("No such user registered")
                else:
                    Transfercurrency(conf_username,to_whom)

        if decision == "E":
            loop = False

