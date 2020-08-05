choice = str(input("encode or decode ? "))
if choice.lower().strip() == "encode":
    text = input("enter message: ")
    list_with_encoded_message = []


    def encode():
        for i in text:
            list_with_encoded_message.append(ord(i))
        print("your encrypted message:", str(list_with_encoded_message).strip('[]'))


    encode()

elif choice.lower().strip() == "decode":
    users_input = input("give me the numbers: ")
    splitted_input = users_input.replace(',', '').split()
    new_list = []


    def decode():
        for i in splitted_input:
            i = int(i)
            new_list.append(chr(i))
        print("the message:", "".join(map(str, new_list)))


    decode()
else:
    print("really?")
    exit()
