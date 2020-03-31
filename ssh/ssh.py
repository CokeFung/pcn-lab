from netmiko import ConnectHandler

router = {
	'device_type':'cisco_ios',
	'host':'192.168.10.1',
	'username':'noob',
	'password':'N00b',
	#'port':8022,
	'secret':'class'
}

router_connect = ConnectHandler(**router)
output = router_connect.send_command('show ip int brief')
print(output)