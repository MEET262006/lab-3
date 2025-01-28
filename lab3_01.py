def count_vowels(input_str):
    vowels="aeiouAEIOU"
    count=0
    for i in input_str:
        if i in vowels:
            count +=1
    print("the number of vowels are:",count)
s=input("Enter the string")
count_vowels(s)
    
    
