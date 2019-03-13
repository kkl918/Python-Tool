import paramiko
import sys

## EDIT SSH DETAILS ##

#SSH_ADDRESS = ["192.168.0.142","192.168.0.139","192.168.0.178","192.168.0.172"]
SSH_ADDRESS = ["192.168.0.142","192.168.0.139"]
#SSH_ADDRESS = ["192.168.0.193","192.168.0.179"]
SSH_USERNAME = "pi"
#SSH_USERNAME = "linaro"
SSH_PASSWORD = "123456"
#SSH_PASSWORD = "au4a8333"
SSH_COMMAND = "sudo "

## CODE BELOW ##

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

ssh_stdin = ssh_stdout = ssh_stderr = None
option = 'shutdown now'
for pi in SSH_ADDRESS:
    ssh.connect(pi, username=SSH_USERNAME, password=SSH_PASSWORD)
    ssh_stdin, ssh_stdout, ssh_stderr = ssh.exec_command(SSH_COMMAND+option)
    print(SSH_COMMAND + option + ' ' + pi,'\n',ssh_stdout.readlines(),'\n')

# if sys.argv[1].startswith('--'):
    # option = sys.argv[1][2:]
    # if option == 'shutdown':
        # option = 'shutdown now'
    # elif option == 'temp':
        # option = '/opt/vc/bin/vcgencmd measure_temp'
    # elif option == 'update':
        # option = 'echo 123456 | apt update -y'
    # elif option == 'upgrade':
        # option = 'echo 123456 | apt upgrade -y'
    # elif option == 'ps_aux':
        # option = 'echo 123456 | ps aux'
        
    # # try:
    # for pi in SSH_ADDRESS:
        # ssh.connect(pi, username=SSH_USERNAME, password=SSH_PASSWORD)
        # ssh_stdin, ssh_stdout, ssh_stderr = ssh.exec_command(SSH_COMMAND+option)
        # print(SSH_COMMAND + option + ' ' + pi,'\n',ssh_stdout.readlines(),'\n')
        # # print(SSH_COMMAND + option + ' ' + pi,'\n',ssh_stdout.read().decode('ascii').strip("\n"))
    # # except Exception as e:
            # # print('wrong argument.')
            # # sys.exit()
            # # sys.stderr.write("SSH connection error: {0}".format(e))

# else:
    # print('wrong type argv')
    # sys.exit()