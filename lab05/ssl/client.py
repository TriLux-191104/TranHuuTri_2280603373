import socket
import ssl
import threading

# Thông tin server
server_address = ('localhost', 12345)

# Hàm nhận dữ liệu từ server
def receive_data(ssl_socket):
    try:
        while True:
            data = ssl_socket.recv(1024)
            if not data:
                break
            print("📩 Nhận:", data.decode('utf-8'))
    except:
        pass
    finally:
        ssl_socket.close()
        print("❌ Kết nối đã đóng.")

# Tạo socket client
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Tạo SSL context
context = ssl.SSLContext(ssl.PROTOCOL_TLS)
context.verify_mode = ssl.CERT_NONE        # ⚠️ Bỏ xác thực (dev only)
context.check_hostname = False             # ⚠️ Không kiểm tra hostname (dev only)

# Thiết lập kết nối SSL
ssl_socket = context.wrap_socket(client_socket, server_hostname='localhost')
ssl_socket.connect(server_address)

# Bắt đầu một luồng để nhận dữ liệu từ server
receive_thread = threading.Thread(target=receive_data, args=(ssl_socket,))
receive_thread.start()

# Gửi dữ liệu từ bàn phím
try:
    while True:
        message = input("Nhập tin nhắn: ")
        if message.strip() == "":
            break
        ssl_socket.send(message.encode('utf-8'))
except:
    print("⚠️ Lỗi khi gửi dữ liệu.")
finally:
    ssl_socket.close()
try:
    while True:
        message = input("Nhập tin nhắn: ")
        ssl_socket.send(message.encode('utf-8'))
except KeyboardInterrupt:
    pass
finally:
    ssl_socket.close()
