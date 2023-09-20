"""l1 = [1,2,3]
l2 = [3,4,5]
l3 = []

for i in range(len(l2)):
    print(l2[i])
    found = False
    for j in range(len(l1)):
        print(l1[j])
        if l2[i] == l1[j]:
            found = True
            break
    if not found:
        l3.append(l1[j])

print(l3)"""


"""l1=[{"RegisterNumber":1234,"Name":"Alex"},{"RegisterNumber":43,"Name":"Alexander"}]
n=123
name='Alexs'

for i in range(len(l1)):
    if l1[i]['RegisterNumber']!=n and l1[i]['Name']!=name:
        l1.append({['RegisterNumber']=n,['Name']=name})

print(l1)"""


l1 = [{"RegisterNumber": 1234, "Name": "Alex"}, {"RegisterNumber": 43, "Name": "Alexander"}]
n = 1234
name = 'Alex'

add_new_entry = True  # Flag to check if a new entry should be added

for i in range(len(l1)):
    if l1[i]['RegisterNumber'] == n or l1[i]['Name'] == name:
        add_new_entry = False
        break

if add_new_entry:
    l1.append({"RegisterNumber": n, "Name": name})

print(l1)



