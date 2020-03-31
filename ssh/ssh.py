from netmiko import ConnectHandler

router = {
	'host':'192.168.10.1',
	'username':'noob',
	'password':'N00b',
	'port':8022,
	'secret':'class'
}

router_connect = ConnectHandler(**router)
output = router_connect.sendcommand('show ip int brief')
print(output)