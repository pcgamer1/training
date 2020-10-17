users = [
    ("Sarthak", 21),
    ("Siddhant", 21)
]

temp = [{user[0]: user} for user in users]
print(temp[0]['Sarthak'][1])
