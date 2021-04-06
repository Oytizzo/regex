import os

def create_directory(name):
    try:
        os.mkdir(name)
    except FileExistsError:
        print(name, "already exists")

create_directory("dimik_pub")
