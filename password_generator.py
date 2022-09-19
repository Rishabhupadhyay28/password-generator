# password generator through random class

print('''                                                            _                                                      _                  
                                                           | |                                                    | |                 
  _ __     __ _   ___   ___  __      __   ___    _ __    __| |         __ _    ___   _ __     ___   _ __    __ _  | |_    ___    _ __ 
 | '_ \   / _` | / __| / __| \ \ /\ / /  / _ \  | '__|  / _` |        / _` |  / _ \ | '_ \   / _ \ | '__|  / _` | | __|  / _ \  | '__|
 | |_) | | (_| | \__ \ \__ \  \ V  V /  | (_) | | |    | (_| |       | (_| | |  __/ | | | | |  __/ | |    | (_| | | |_  | (_) | | |   
 | .__/   \__,_| |___/ |___/   \_/\_/    \___/  |_|     \__,_|        \__, |  \___| |_| |_|  \___| |_|     \__,_|  \__|  \___/  |_|   
 | |                                                                   __/ |                                                          
 |_|                                                                  |___/                                                           ''')
import random
letters=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
numbers=['1','2','3','4','5','6','7','8','9']
symbols=['!','@','#','$','%','&','*','(',')']
nr_letters=int(input("enter the numbers of letters you want??\n"))
nr_numbers=int(input("enter the numbers of numbers you want??\n"))
nr_symbols=int(input("enter the number of symbols you want?? \n"))
password=""
for char in range(1,nr_letters+1):
    password += random.choice(letters)
for char in range(1,nr_numbers+1):
    password += random.choice(numbers)
for char in range(1,nr_symbols+1):
    password+= random.choice(symbols)
print("your password is :",password)