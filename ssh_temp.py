import paramiko
import sys, time,os

## EDIT SSH DETAILS ##


SSH_ADDRESS = ["192.168.0.139","192.168.0.149"]

SSH_USERNAME = "pi"

SSH_PASSWORD = "123456"

SSH_COMMAND = "sudo "

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

ssh_stdin = ssh_stdout = ssh_stderr = None
option = '/opt/vc/bin/vcgencmd measure_temp'

while 1:

    ssh.connect(SSH_ADDRESS[0], username="pi", password="au4a8333")
    ssh_stdin, ssh_stdout, ssh_stderr = ssh.exec_command(SSH_COMMAND+option)
    print(SSH_ADDRESS[0],":",ssh_stdout.readlines()[0][5:9])
    ssh.close()
    
    # ssh.connect(SSH_ADDRESS[1], username="linaro", password="au4a8333")
    # ssh_stdin, ssh_stdout, ssh_stderr = ssh.exec_command("cat /sys/class/thermal/thermal_zone1/temp")
    # tem = float(ssh_stdout.readlines()[0])/1000
    # print(SSH_ADDRESS[1],":","%.1f" % tem,'\n')
    ssh.close()
    
    time.sleep(5)