#!/usr/bin/env python3
#data/users2.txt

import sys
import collections


ID, FORENAME, MIDDLENAME, SURNAME, DEPARTEMENT = range(5)

User = collections.namedtuple("PAPA",
            "username forename middlename surname id")

def main():
    if len(sys.argv) == 1 or sys.argv[1] in {"-h", "--help"}:
        print("usage: {0} file1 [file1 [... fileN]]".format(sys.argv[0][sys.argv[0].rfind("/")+1:]))
        sys.exit()

    usernames = set()
    users = {}
    for filename in sys.argv[1:]:
        for line in open(filename, encoding="utf8"):
            line = line.rstrip()
            if line:
                user = process_line(line, usernames)
                users[(user.surname.lower(), user.forename.lower(),
                       user.id)] = user
    print_users(users)


def process_line(line, usernames):
    fields = line.split(":")
    username = generate_username(fields, usernames)
    user = User(username, fields[FORENAME], fields[MIDDLENAME],
                fields[SURNAME], fields[ID])
    return user

def generate_username(fields, usernames):
    username = ((fields[FORENAME][0] + fields[MIDDLENAME][:1] +
                 fields[SURNAME]).replace("-", "").replace("'", ""))
    username = original_name = username[:8].lower()
    count = 1
    while username in usernames:
        username = "{0}{1}".format(original_name, count)
        count += 1
    usernames.add(username)
    return username

def print_users(users):
    namewidth = 17
    usernamewidth = 9
    columngap = " " * 2

    head_line1 = "{0:-<{nw}} {0:-<6} {0:-<{uw}}".format(
        "", nw=namewidth, uw=usernamewidth)
    head_line2 = "{0:<{nw}} {1:^6} {2:{uw}}".format(
        "Name", "ID", "Username", nw=namewidth, uw=usernamewidth)    

    main_head_line = "".join((head_line1,columngap,head_line1,"\n",
                              head_line2,columngap,head_line2,"\n",
                              head_line1,columngap,head_line1))
    stroka = ""
    i = 0
    for key in sorted(users):
        if i % 64 == 0:
            print(main_head_line)
        i += 1
        user = users[key]
        initial = ""
        if user.middlename:
            initial = " " + user.middlename[0]
        name = "{0.surname}, {0.forename}{1}".format(user, initial)
        stroka += "{0:.<{nw}.{nw}} ({1.id:4}) {1.username:{uw}} ".format(
            name, user, nw=namewidth, uw=usernamewidth)
        if i % 2 == 0:
            print(stroka)
            stroka = ""
    
    if i % 2 != 0:
            print(stroka)


main()
