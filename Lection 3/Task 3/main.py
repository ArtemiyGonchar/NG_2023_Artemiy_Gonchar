import json


def jsonKeySearch(userjson, userkey):
    for value in userjson.values():
        if userkey in value:
            print(value[userkey])
            return
        if isinstance(value, dict):
            jsonKeySearch(value, searchKey)

with open(input("Enter your file name: "), "r") as not_parsed_json:
  parsed_json = json.load(not_parsed_json)
  searchKey = input("Enter your key to search: ")
  jsonKeySearch(parsed_json, searchKey)
#userfile = open(input("Enter your file: "), "r")
#info = json.loads(userfile)
#searchKey = input("Enter your key to search: ")
#jsonKeySearch(parsed_json, searchKey)
#userfile.close()