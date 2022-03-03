text = "amo roma"
text = text.replace (" ","")
print(text)

reversed = text[::-1]
if text == reversed:
    print("this is a palindrome")
else:
    print(" this is not a palindrome")
