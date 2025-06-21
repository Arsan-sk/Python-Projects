from cryptography.fernet import Fernet
'''
def write_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)
write_key()
'''

def load_key():
    file = open("key.key", "rb")
    key = file.read()
    file.close()
    return key

key = load_key()
fer = Fernet(key)


master_pwd = input("Enter the master password: ")

def view():
    with open('passwords.txt', 'r') as f:
        for line in f.readlines():
            line = line.rstrip()
            website, username, pwd = line.split(" | ") #split every time | come, 
            #a,b,c = [hsbxb,hgsv,ahga] its form a list
            print(f"\nWebsite: {website} \nUsername: {username} \nPassword: {fer.decrypt(pwd.encode()).decode()} \n")


def add():
    website = input("Enter the website name: ")
    username = input("Enter the username of the account: ")
    pwd = input("Enter the password: ")
    
    with open('passwords.txt', 'a') as f:  #a creat if not exist or add || w overwrite delete existed make new file || r read only
        f.write(f"{website} | {username} | {fer.encrypt(pwd.encode()).decode()} \n")
        print("Password added successfully!")
        


while True:
    mode = input("Chose mode on basis of what you want q for quit (add/view/q): ").lower()

    if mode == 'add':
       add()

    elif mode == 'view':
       view()
    elif mode == 'q':
        break
    else:
        print("Invalid mode. Please choose 'add' or 'view'.")
        continue

        