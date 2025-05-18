def dao_nguoc_chuoi(chuoi):
    return chuoi[::-1]
input_string = input("Mỗi chuỗi cần đảo ngược: ")
print("Chuối đảo ngược: ", dao_nguoc_chuoi(input_string))