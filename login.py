import bcrypt

def hash_password(password):
    binery_password = password.encode("utf-8")
    salt = bcrypt.gensalt()
    hash = bcrypt.hashpw(binery_password, salt)
    return hash.decode("utf-8")



def valid_hash(password, hash):
    bin_pwd = password.encode("utf-8")
    bin_hash = hash_password(password).encode("utf-8")
    print(bcrypt.checkpw(bin_pwd, bin_hash))

def register_user():
    user_name = input("Enter your username:")
    password = input("Enter your password:")
    hash = hash_password(password)
    with open("user.txt", "a") as f:
        f.write(f"{user_name},{hash}\n")

def login_user():
    user_name = input("Enter your username:")
    password = input("Enter your password:")
    
    with open("user.txt", "r") as f:
        lines = f.readlines()

        for line in lines:
            u_name, hash = line.strip().split(",")

            if user_name == u_name:
                return valid_hash(password,hash)
        return False
''' 
def menu():
    print("*"*30)
    print("***Welcome to my system***")
    print("Choose from the following options:")
    print("1. Register")
    print("2. Login")
    print("3. EXIT")
    print("*"*30)

def main():
    while True:
        menu()
        choice = input(">")
        if choice == "1":
            register_user()
        elif choice == "2":
            if login_user():
                print("You have been logged in!!")
            else:
                print("Incorrect Login!!")
        elif choice == "3":
            print("Goodbye!!!")
            break


main()
'''
