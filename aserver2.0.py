import asyncio
import signal


from server_functions import *
from work_with_files import *

signal.signal(signal.SIGINT,signal.SIG_DFL)

async def handle_echo(reader,writer):
    """
        a server function that handles all the requests of the
        client and send's back the reply
    """
    addr = writer.get_extra_info('peername')
    message = f"{addr} is connected!!!!"
    users_loggedin = []
    print(message)
    while True:
        # reading command from the client
        data = await reader.read(5000)
        choice = data.decode().strip()
        split_choice = choice.split(" ")
        command = split_choice[0]
        reading_file = False
        uid = ""

        # logging in or registering as per user choice
        if command == "login":
            data = user_verify(split_choice[1])
            if data == "not found":
                data = login_verify(split_choice[1],split_choice[2])
                if data == "logged in successfully!!!!!":
                    user_obj = User(split_choice[1])
                    uid = split_choice[1]
                else:
                    data = "password and username mis match"
            else:
                data = "user already logged in from other client"



        elif command == "register":
            data = register_user(split_choice[1],split_choice[2])
            if data == "user registered successfully!!!!":
                user_obj = User(split_choice[1])

        elif command == "create_folder":
            data = user_obj.create_folder(split_choice[1])

        elif command == "write_file":
            write_info = ""
            for i in range(2,len(split_choice)):
                write_info += split_choice[i] + " "
            data = user_obj.write_file(split_choice[1],write_info)

        elif command == "read_file":
            split_choice.append(" ")
            if split_choice[1] == " ":
                user_obj.char_count = 0
                reading_file = False
                data = "closed the file"
            else:
                if reading_file:
                    data=user_obj.start_reading()
                    if data == "":
                        user_obj.close_file()
                        reading_file = False
                else:
                    user_obj.read_file(split_choice[1])
                    data=user_obj.start_reading()
                    reading_file = True

        elif command == "list":
            data = user_obj.files_list()
        elif command == "change_folder":
            data = user_obj.change_folder(split_choice[1])
        elif command == "exit":
            data =log_out(uid)
        else:
            data = "wrong choice reconnect to the server"

        # writing the response of logging in or registering
        writer.write(data.encode())
        await writer.drain()


async def main():
    server = await asyncio.start_server(handle_echo,'127.0.0.1',8888)
    addr = server.sockets[0].getsockname()
    print(f"serving on {addr}")
    async with server:
        await server.serve_forever()

asyncio.run(main())