import paramiko

host = '127.0.0.1'
port = 22

trans = paramiko.Transport((host, port))
trans.start_client()

sftp = paramiko.SFTPClient.from_transport(trans)
print(sftp.listdir('/'))
sftp.close()
