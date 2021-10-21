able_users = []
with open("users.txt", 'r') as file_all_able_users:
    all_able_users = file_all_able_users.readlines()
for able_user_line in all_able_users:
    try:
        able_users.append(int(able_user_line))
    except:
        pass

print(able_users)
