import random
alphabet=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
number=[1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
special_character=['@', '#', '$', '%', '^', '&', '*', '(', ')', '_', '-', '+', '=']
password= ""
no_alphabet=int(input("Enter no of alphabets in your password: "))
no_number=int(input("Enter no of numbers in your password: "))
no_special_char=int(input("Enter no of special character in your password: "))
shuffle_pass=""
for i in range(1, no_alphabet + 1):
    a=random.choice(alphabet)
    password += a
for i in range(1, no_number + 1):
    n=str(random.choice(number))
    password+=n
for i in range(1, no_special_char + 1):
    s=random.choice(special_character)
    password += s
pss_lst=list(password)
random.shuffle(pss_lst)
for i in pss_lst:
    shuffle_pass+=i
print(shuffle_pass)