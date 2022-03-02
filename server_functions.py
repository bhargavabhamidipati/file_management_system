
def login_verify(message_uid,message_pwd):
    """
        function for verifying a user while logging in
    """
    try:
        data="Wrong password or username"
        with open("userid.txt",'r') as handle:
            counter = 0
            for i in handle:
                if message_uid + "\n" == i:
                    with open("password.txt",'r') as handle2:
                        for j in handle2:
                            if counter == 0 and (message_pwd + "\n" == j):
                                data = add_user(message_uid)
                                if data == "data written":
                                    data = "logged in successfully!!!!!"
                                    break
                                else:
                                    break
                            else:
                                data = "Wrong password or user name!!!!"
                            counter -= 1
                counter += 1
        return data
    except FileNotFoundError as err:
        return err



def register_user(message_uid,message_pwd):
    """
        function for registering a user
    """

    try:
        with open("userid.txt","r") as handle:
            for i in handle:
                if message_uid in i:
                    return "username already exists"
        with open("userid.txt",'a') as handle:
            handle.write(message_uid+"\n")
        with open("password.txt",'a') as handle:
            handle.write(message_pwd+"\n")
        return "user registered successfully!!!!"
    except FileNotFoundError as err:
        return err

def add_user(message_uid):
    """
        function to add a user to login list user
    """
    try:
        data = "data written"
        with open("log.txt",'a') as handle:
            handle.write(message_uid+"\n")
        return data
    except FileNotFoundError as err:
        return err


def user_verify(message_uid):
    """
        function to verify if user already logged in or not
    """
    try:
        data="not found"
        with open("log.txt",'r') as handle:
            for i in handle:
                if message_uid + "\n" == i:
                    data = "found"
                    break
        return data
    except FileNotFoundError as err:
        return err

def log_out(message_uid):
    """
        function to log out a user
    """
    try:
        data = "logged in"
        write_list = []
        flag = 0
        with open("log.txt",'r') as handle:
            for i in handle:
                if message_uid + "\n" != i:
                    write_list.append(i)
                else:
                    flag = 1
        with open("log.txt",'w') as handle:
            for i in write_list:
                handle.write(i)
        if flag == 0:
            data = "user has not logged in"
        else:
            data = "logged out"
        return data
    except FileNotFoundError as err:
        return err

def assert_test(message_uid,message_pwd):
    assert register_user(message_uid,message_pwd) == "user registered successfully!!!!", "registration test failed"
    assert login_verify(message_uid,message_pwd) == "logged in successfully!!!!!", "login test failed"
    assert user_verify(message_uid)=="found","user verification test failed"
    assert log_out(message_uid)== "logged out","logout test failed"

uid = input("enter username for testing")
pwd = input("enter password for testing")

assert_test(uid,pwd)
