import re
from pprint import pprint
import csv
from decorator import to_log

if __name__ == '__main__':
    # читаем адресную книгу в формате CSV в список contacts_list
    with open("phonebook_raw.csv", encoding='utf-8') as f:
        rows = csv.reader(f, delimiter=",")
        contacts_list = list(rows)

    # rewriting phone numbers
    phone_num = r'(\+7|8)\s?\(?(\w{3})\)?\s?-?(\w{3})-?(\w{2})-?(\w{2})(\s?)(\(?((доб\.)\s(\w{4}))\)?)?'
    num_format = r'+7(\2)\3-\4-\5\6\9\10'

    i = 1
    form_list = contacts_list
    while i < len(contacts_list):
        form_list[i][5] = re.sub(phone_num, num_format, contacts_list[i][5])
        i += 1


    # pprint(form_list)

    # put names, surnames... as different elements


    @to_log(path=r"C:\Users\olesy\PycharmProjects\regex_decorated\log.txt")
    def arrange_names(some_list):
        new_list = some_list

        for n in range(0, 2):
            for i in range(1, 9):
                if re.search(r'\s', some_list[i][n]):
                    name = some_list[i][n].split(' ')
                    if n == 0:
                        if some_list[i][1] != '':
                            name.extend(some_list[i][3:])
                            new_list[i] = name
                        else:
                            name.extend(some_list[i][2:])
                            new_list[i] = name
                    else:
                        new_list[i][n] = name[0]
                        new_list[i][n + 1] = name[1]
                else:
                    pass

        return new_list


    arrange_names(form_list)
