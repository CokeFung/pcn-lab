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
    tn.write(b"show version\n")
    tn.read_until(b"show version")
    router_spec = tn.read_until(b"#").decode('ascii').replace('\r', '')[1:-3]

    tn.write(b"show ip int brief\n")
    tn.read_until(b"brief")
    router_int = tn.read_until(b"#").decode('ascii').replace('\r', '')[1:-3]

    tn.write(b"show ip route\n")
    tn.read_until(b"show ip route")
    router_table = tn.read_until(b"#").decode('ascii').replace('\r', '')[1:-3]

    #disconnect
    tn.write(b"exit\n")

    print(tn.read_all().decode('ascii'))
    content = "Name: " + router_name + "\nSpec: \n" + router_spec + \
    "\nInterface: \n" + router_int + "\nRouting table: \n" + router_table + "\n"

    file_name = router_name + ".txt"
    save_out = open(file_name, "w")
    save_out.write(content + "\n")
    save_out.close()
    