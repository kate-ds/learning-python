import json

with open("my_file.json", encoding="utf-8") as read_f:
    data = json.load(read_f)
    print(data)
#
# data = {
#     "income": {
#         "salary": 50000,
#         "bonus": 20000
#     }
# }
#
# json_str = json.dumps(data)
# print(type(json_str))
