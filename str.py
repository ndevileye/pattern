string = input("enter")
l = ['a', 'i', 'e', 'o', 'u']
string = list(string)
for i in range(len(string)):
    if string[i] in l:
        temp_index = i
        break
i = i+1
while i < len(string):
    if string[i] in l:
        string[temp_index], string[i] = string[i], string[temp_index]
        break
    i = i+1
string = "".join(string)
print(string)
