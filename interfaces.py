import io
import os
from netmiko import ConnectHandler

with open(file="hosts.txt", mode="r") as hosts:

    devices = [{
        'device_type' : 'cisco_ios',
        'ip' : ip,
        'username' : 'username',
        'password' : 'password',
        #'secret' : '',
    }
    for ip in hosts.read().splitlines()
    ]

for device in (devices):
    try:
        net_connect = ConnectHandler(**device)
        net_connect.enable()

        device_ip = {device['ip']}
        print ({device['ip']})        
        
        sh_runn_name = net_connect.send_command('sh running-config | include hostname')
        sh_int_status = net_connect.send_command('show interface status')
        print(sh_runn_name)

        with open("GM_.txt", "a", encoding = 'utf-8' ) as arquivo:
            for texto in sh_runn_name, device_ip, sh_int_status:
                arquivo.write(str(texto))
                arquivo.write('\n\r')

        arquivo.close()

    except:
            erro = ({device['ip']})
            with open('erro.txt', 'a', encoding= 'utf-8') as falhas:
                for texta in erro:
                    falhas.write(str(texta))
                    falhas.write('\n\r')
                    falhas.close()
    continue
net_connect.disconnect()
os.system("pause")