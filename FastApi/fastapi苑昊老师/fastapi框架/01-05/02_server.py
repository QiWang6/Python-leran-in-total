# @Time: 2024/10/10 
# @Author: Qi Wang
# @File: 02 server
# @Project: Python-leran-in-total
# @Quelle:

# web应用程序遵循http协议

import socket

sock = socket.socket()

# 绑定ip地址和端口
sock.bind(("127.0.0.1", 8000))

# 设置一个最大排列数
sock.listen(5)

while 1:
    # conn是来连接的客户端的套接字，就是接下来服务端和客户端连接的双向通道，addr是该客户端的远程地址
    conn, addr = sock.accept()  # 阻塞等待客户端连接
    data = conn.recv(1024)  # 取1KB的数据
    print("客户端发送的请求信息:\n", data)

    conn.send(b'HTTP/1.1 200 ok\r\nserver:yuan\r\ncontent-type:application/json\r\n\r\n{"user_id":101}')  # b代表字节数据
    conn.close()  # 使用完成一定要把这个管道关闭
