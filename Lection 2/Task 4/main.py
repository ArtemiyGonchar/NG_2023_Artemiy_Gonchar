st = input("Enter your message: ")
stclear = ''
for i in st.lower():
    if i in "aeyuoi":
        stclear += i
print (stclear)