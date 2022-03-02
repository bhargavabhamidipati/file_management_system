import asyncio
import os
import time

async def tcp_echo_client():
    """function defined to run the client in a loop"""
    reader,writer = await asyncio.open_connection('127.0.0.1',8888)
    message=''
    command_history = []
    while True:

        # displaying choice
        print("1.login<username> <password>\n2.Register <username> <password>\n3.create_folder <name>\n4.write_file <name> <input>")
        print("5.read_file <name>\n6.list\n7.change_folder <name>\n8.exit ")
        print("please enter the command in the above formats\n")

        # sending request to the server
        choice = input()
        #if choice == 'exit':
           # break
        writer.write(choice.encode())
        command_history.append(choice)

        data = await reader.read(5000)
        message = data.decode().strip()
        if choice == "list":
            dir_list = os.listdir(message)
            for file_name in dir_list:
                file = message+"/" +file_name
                size = os.stat(file).st_size
                created = os.path.getctime(file)
                print(file_name + " "+ str(size) + " " + time.ctime(created) )
            message = "done*********"
        print(message)
        if choice == 'exit':
            break
    print('close the connection')
    writer.close()

asyncio.run(tcp_echo_client())
