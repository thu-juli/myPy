user = []
user.append({
    "id": 1,
    "name": "Leanne Graham",
    "username": "Bret",
    "email": "Sincere@april.biz",
})

print("Use for Index")
for i in user:
    print(f"{i['id']}")
    print(f"{i['username']}")
    print(f"{i['name']}")

print("\nUse for Range")
for i in range(0, len(user)):
    print(f'{user[i]["id"]}')
    print(f'{user[i]["username"]}')
    print(f'{user[i]["name"]}')

print('\nNew Dictionary')
user = {
    "id": 1,
    "name": "Leanne Graham",
    "username": "Bret",
    "email": "Sincere@april.biz",
    "address": {
      "street": "Kulas Light",
      "suite": "Apt. 556",
      "city": "Gwenborough",
      "zipcode": "92998-3874",
      "geo": {
        "lat": "-37.3159",
        "lng": "81.1496"
      }
    }
}

print(user["address"]["geo"]['lat'])
for key, value in user.items():
    print(f'{key} : {value}')