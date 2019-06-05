#!/usr/bin/python3

from sys import argv
import json
import os.path

load_from_json_file = __import__('8-load_from_json_file').load_from_json_file
save_to_json_file = __import__('7-save_to_json_file').save_to_json_file

my_file = "add_item.json"

if not os.path.exists(my_file):
    temp = open(my_file, "w")
    temp.write(json.dumps([]))
    temp.close()

new_list = load_from_json_file(my_file)

for i in argv[1:]:
    new_list.append(i)
save_to_json_file(new_list, my_file)
