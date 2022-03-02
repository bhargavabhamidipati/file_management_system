import os
class User:

    """
        this class represents the users and their operations on files
        with the help of commands
    """
    def __init__(self,userid):
        """
            a constructor to initialise all the parameters of a
            user
        """
        self.userid = userid
        self.path = os.getcwd()+"/root/"+self.userid
        self.char_count = 0
        self.data = ""
        if self.userid not in os.listdir(os.getcwd()+"/root"):
            try:
                os.mkdir(self.path)
            except OSError:
                print ("creation of the user directory failed")
            else:
                print("user directory created successfully")

    def open_the_user_folder(self):
        """
            a function to open the users directory
        """
        try:
            self.path=os.getcwd()+"/root/"+self.userid
        except OSError as err:
            print(err)

    def create_folder(self,folder_name):
        """
            a function that creates a folder with the folder name
            of the users choice
        """
        try:
            dir_list = os.listdir(self.path)
            if folder_name in dir_list:
                return "folder already exists"
            else:
                os.mkdir(self.path+"/"+folder_name)
                return "folder created....."
        except OSError as err:
            return err

    def change_folder(self,folder_name):
        """
            this function helps the user to move from one directory
            to the other
        """
        try:
            dir_list = os.listdir(self.path)
            new_path = ""
            if folder_name == "..":
                path_split = self.path.split("/")
                print(path_split)
                if path_split[len(path_split)-1] == self.userid:
                    return "you are already in the user folder"
                else:
                    new_path = path_split[0]
                    for i in range(1,len(path_split)-1):
                        new_path = new_path + "/" + path_split[i]
                    self.path = new_path
                    return "path changed to required location"
            else:
                if folder_name in dir_list:
                    self.path=self.path + "/" + folder_name
                    return "path changed to required location"
                else:
                    return "file not found in the folder"
        except OSError as err:
            return err

    def write_file(self,file_name,input_data):
        """
            function definition that is used to write to a file
            as per the users choice
        """
        try:
            dir_list = os.listdir(self.path)
            if file_name in dir_list:
                if input_data == "":
                    with open(self.path+"/"+file_name,'a') as handle:
                        handle.write("")
                else:
                    with open(self.path+"/"+file_name,'a') as handle:
                        handle.write(input_data)
            else:
                if input_data == "":
                    with open(self.path+"/"+file_name,'a') as handle:
                        handle.write("")
                else:
                    with open(self.path+"/"+file_name,'a') as handle:
                        handle.write(input_data)
            return "data written"
        except FileNotFoundError as err:
            return err

    #------------------------------------------------------------------------------------------------


    # reading text files for the user
    def read_file(self,file_name):
        """
            a function that reads a file from beginning to the end
        """
        try:
            dir_list = os.listdir(self.path)
            if file_name in dir_list:
                with open(self.path+"/"+file_name,"r") as file_handle:
                    self.data = file_handle.read()
            else:
                return "fail to open file"
        except FileNotFoundError as err:
            return err

    def start_reading(self):
        """
            a function that returns characters read from from the
            file
        """
        text = self.data[self.char_count:self.char_count + 100]
        self.char_count += 100
        return text


    # closing the opened file
    def close_file(self):
        """
            a function that closes a file that is open
        """
        self.handle.close()
    #-----------------------------------------------------------------------------------------------

    # display the list of files
    def files_list(self):
        """
            a function that returns the path of current position of
            the user
        """
        return self.path
    #-------------------------------------------------------------------------------------------------

