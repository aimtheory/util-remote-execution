import paramiko
import argparse
import os


def upgrade_servers(username, keyfile, serverlist):
    # Load SSH key
    private_key = paramiko.RSAKey.from_private_key_file(keyfile)

    # Loop through servers and execute upgrade command
    for server in serverlist:
        try:
            ssh = paramiko.SSHClient()
            ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            ssh.connect(server, username=username, pkey=private_key)
            stdin, stdout, stderr = ssh.exec_command('sudo apt-get update && sudo apt-get upgrade -y')
            print(f"Upgrade completed successfully on {server}")
        except paramiko.SSHException as e:
            print(f"Failed to connect to {server}: {e}")
        except Exception as e:
            print(f"An error occurred while upgrading {server}: {e}")
        finally:
            ssh.close()


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Upgrade remote Linux servers via SSH')
    parser.add_argument('-u', '--username', type=str, help='SSH username', required=True)
    parser.add_argument('-k', '--keyfile', type=str, help='SSH private key file path', required=True)
    parser.add_argument('-s', '--serverfile', type=str, help='Server list file path')
    parser.add_argument('-d', '--domain', type=str, help='Domain name')
    parser.add_argument('-r', '--range', type=int, nargs=2, metavar=('START', 'STOP'), help='Range of integer values as hostnames')
    parser.add_argument('-sd', '--subdomain', type=str, help='Subdomain name')
    args = parser.parse_args()

    if not os.path.isfile(args.keyfile):
        print(f"Key file not found at {args.keyfile}")
        exit(1)

    if args.serverfile:
        if not os.path.isfile(args.serverfile):
            print(f"Server file not found at {args.serverfile}")
            exit(1)
        else:
            with open(args.serverfile, 'r') as f:
                serverlist = f.read().splitlines()
    else:
        serverlist = []

    if args.range:
        start, stop = args.range
        if args.subdomain:
            subdomain = args.subdomain
        else:
            subdomain = ''
        for i in range(start, stop+1):
            serverlist.append(f"{subdomain}{i}.{args.domain}")

    if not serverlist:
        print("No servers found to upgrade")
        exit(0)

    upgrade_servers(args.username, args.keyfile, serverlist)
