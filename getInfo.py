import telnetlib

routers_list = {}

devices = [
	"100.0.10.1",
	"100.0.20.1",
	"100.0.30.1",
	"100.0.40.1",
	"100.0.50.1",
	"100.0.60.2"
	]
user = "cisco"
passwd = "cisco"
en_pass = "class"

for device in devices: 

  #connect
  #print("Connecting to", device)
  tn = telnetlib.Telnet(device)

  #authen
  tn.read_until(b"Password: ").decode('ascii')
  tn.write(passwd.encode('ascii') + b"\n")

  #access privilege mode and get router name
  router_name = tn.read_until(b">").decode('ascii').replace('\r', '').replace('\n', '')[:-1]
  tn.write(b"enable\n")
  tn.read_until(b"Password: ").decode('ascii')
  tn.write(en_pass.encode('ascii') + b"\n")
  tn.read_until(b"#").decode('ascii')
  tn.write(b"terminal length 0\n")
  tn.read_until(b'#').decode('ascii')

  #send command and get output  (specifications)
  tn.write(b"show version\n")
  tn.read_until(b'show version')
  router_spec = tn.read_until(b'#').decode('ascii').replace('\r', '')[1:-3]
  #print(router_spec, end='')


  #send command and get output  (interfaces)
  tn.write(b"show ip int brief\n")
  tn.read_until(b'brief')
  router_int = tn.read_until(b'#').decode('ascii').replace('\r', '')[1:-3]

  #send command and get output
  tn.write(b"show ip route\n")
  tn.read_until(b"show ip route")
  router_route = tn.read_until(b'#').decode('ascii').replace('\r', '')[1:-3]

  #disconnect
  tn.write(b"exit\n")

  print(tn.read_all().decode('ascii'))
  print("Name: " + router_name)
  print("Spec: \n" + router_spec)
  print("Interface: \n" + router_int)
  print("Routing Table: \n" + router_route)
  print('\n')


