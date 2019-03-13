import paramiko
import sys

## EDIT SSH DETAILS ##

SSH_ADDRESS = ["192.168.0.123","192.168.0.172"]
SSH_USERNAME = "pi"
SSH_PASSWORD = "123456"
SSH_COMMAND = "sudo shutdown"

## CODE BELOW ##

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

ssh_stdin = ssh_stdout = ssh_stderr = None

try:
    for pi in SSH_ADDRESS:
        ssh.connect(pi, username=SSH_USERNAME, password=SSH_PASSWORD)
        ssh_stdin, ssh_stdout, ssh_stderr = ssh.exec_command(SSH_COMMAND)
except Exception as e:
    sys.stderr.write("SSH connection error: {0}".format(e))

if ssh_stdout:
    sys.stdout.write(ssh_stdout.read())
if ssh_stderr:
    sys.stderr.write(ssh_stderr.read())