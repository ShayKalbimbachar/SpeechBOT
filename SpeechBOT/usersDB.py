import os

filename = "users_db.txt"
users = {}
with open(filename) as file:
    for line in file.readlines():
        if len(line) > 2:
            users[line.split(":")[0]] = line.split(":")[1]


def save_db_to_file():
    with open(filename, 'w', encoding='utf-8') as file:
        for user in users.keys():
            file.write(f"{user}:{users[user]} \n")


def write_to_db(user, lang):
    users[user] = lang
    save_db_to_file()
    return


def get_user_lang(user):
    if user in users.keys():
        return users[user].split(" ")[0][0,2]
    else:
        return None


def remove_user(user):
    if user in users.keys():
        del users[user]
    os.remove(filename)
    save_db_to_file()
