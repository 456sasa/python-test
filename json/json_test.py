import json
from os import supports_dir_fd

def get_stored_username():
    filename = 'json\\usernametest.json'
    try:
        with open(filename) as f:
            username = json.load(f)
    except FileNotFoundError:
        return None
    
    # 这个是解码异常的问题，在报错的地方抛出异常就可以正常运行了
    except json.decoder.JSONDecodeError:
        print("文件解码异常需要重新输入")
        return None
    else:
        return username

def get_new_username():
    username = input("What's your name \n")
    filename = 'json\\usernametest.json'
    with open (filename,'w') as f:
        json.dump(username,f)
    return username

def greet_user():
    username = get_stored_username() 
    if username:
        print(f"Welcome back {username}")
    else:
        username = get_new_username()
        print(f"We'll remember you when you come back,{username}")

greet_user()