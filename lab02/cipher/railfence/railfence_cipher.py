class RailFenceCipher:
    def __init__(self):
        pass

    def rail_fence_encrypt(self, plain_text, num_rails):
        # Tạo danh sách các "đường ray" (rails) rỗng
        rails = [[] for _ in range(num_rails)]
        rail_index = 0
        direction = 1  # 1: xuống, -1: lên

        # Điền các ký tự vào các đường ray
        for char in plain_text:
            rails[rail_index].append(char)

            # Thay đổi hướng khi đạt đến đường ray trên cùng hoặc dưới cùng
            if rail_index == 0:
                direction = 1
            elif rail_index == num_rails - 1:
                direction = -1

            # Di chuyển đến đường ray tiếp theo
            rail_index += direction

        # Nối các ký tự từ các đường ray để tạo ra văn bản mã hóa
        cipher_text = ''.join(''.join(rail) for rail in rails)
        return cipher_text

    def rail_fence_decrypt(self, cipher_text, num_rails):
        # Tính toán độ dài của từng đường ray trong quá trình mã hóa
        rail_lengths = [0] * num_rails
        rail_index = 0
        direction = 1

        for _ in range(len(cipher_text)):
            rail_lengths[rail_index] += 1
            if rail_index == 0:
                direction = 1
            elif rail_index == num_rails - 1:
                direction = -1
            rail_index += direction

        # Tách văn bản mã hóa thành các đường ray dựa trên độ dài đã tính
        rails = []
        start = 0
        for length in rail_lengths:
            rails.append(cipher_text[start : start + length])
            start += length

        # Xây dựng lại văn bản gốc bằng cách đọc các ký tự theo kiểu zigzag
        plain_text = ""
        rail_index = 0
        direction = 1

        for _ in range(len(cipher_text)):
            plain_text += rails[rail_index][0]
            rails[rail_index] = rails[rail_index][1:] # Xóa ký tự đã dùng

            if rail_index == 0:
                direction = 1
            elif rail_index == num_rails - 1:
                direction = -1
            rail_index += direction

        return plain_text