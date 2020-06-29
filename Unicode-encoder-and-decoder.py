choice = str(input("encode or decode ? "))
if choice.lower().strip() == "encode":
    text = input("enter message: ")
    list = []
    def encode():
        for i in text:
            list.append(ord(i))
        print("your encrypted message:", str(list).strip('[]'))
    encode()
elif choice.lower().strip() == "decode":
    lista = input("give me the numbers: ")
    lista = lista.replace(',', '').split()
    new_lista = []
    def decode():
        for i in lista:
            i = int(i)
            new_lista.append(chr(i))
        print("the message:", "".join(map(str, new_lista)))
    decode()
else:
    print("really?")
    exit()

