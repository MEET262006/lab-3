str =input("enter the string:")
remove_str = input("enter the string that you want to remove:")
new_str=""

for ch in str:
    if ch in remove_str:
        new_str = new_str +""
    else:
        new_str = new_str + ch
print(new_str)


