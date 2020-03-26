import telnetlib

devices = [
    "192.168.0.1",
    "192.168.7.2",
    "192.168.8.2",
    "192.168.9.2",
    "192.168.10.2",
    "192.168.11.2"
    ]
user = "cisco"
password = "cisco"
en_pass = "cisco"

for device in devices:
    #connect
    tn = telnetlib.Telnet(device)

    #authen
    tn.read_until(b"Password: ").decode('ascii')
    tn.write(password.encode('ascii') + b"\n")

    #acess privilege
    tn.read_until(b">")
    tn.write(b"\n")
    router_name = tn.read_until(b">").decode('ascii').replace('\r', '').replace('\n', '')[:-1]
    tn.write(b"enable\n")
    tn.read_until(b"Password: ").decode('ascii')
    tn.write(en_pass.encode('ascii') + b"\n")
    tn.read_until(b"#").decode('ascii')
    tn.write(b"terminal length 0\n")
    tn.read_until(b"#").decode('ascii')

    #sending command
    tn.write(b"conf t\n")
    tn.read_until(b"conf t")
    tn.read_until(b"#").decode('ascii').replace('\r', '')[1:-len("Rx(config)#")]

    router_name = router_name+"s"
    command = "hostname " + router_name + "\n"
    tn.write(command.encode('ascii'))
    tn.read_until(command[:-1].encode('ascii'))
    tn.read_until(b"#").decode('ascii').replace('\r', '')[1:-len("Rx(config)#")]

    tn.write(b"line vty 0 15\n")
    tn.read_until(b'#')
    tn.write(b"password cisco")
    tn.read_until(b'#')

    tn.write(b"end\n")
    tn.read_until(b"#")
    tn.write("show run")
    router_runningconfig = tn.read_until(b"#").decode('ascii').replace('\r', '')[1:-len("Rx#")]

    #disconnect
    tn.write(b"exit\n")

    print(tn.read_all().decode('ascii'))
    content = "Running config: " + router_runningconfig

    file_name = router_name + ".txt"
    save_out = open(file_name, "w")
    save_out.write(content + "\n")
    save_out.close()
