#!/bin/bash 
trap 'echo "# $BASH_COMMAND"' DEBUG

echo "a. Display OS version, release number, kernel version"
lsb_release -a
lsb_release -d
cat /etc/os-release
hostnamectl

uname -a

uname -s

uname -r

uname -v

uname -m

uname -p

uname -o

echo -e "\nb. Display top 10 processes in descending order"
top -b -o +%MEM | head -n 17

echo -e "\nc. Display processes with highest memory usage."
ps -eo pid,ppid,cmd,%mem,%cpu --sort=-%mem | head

echo -e "\nd. Display current logged in user and log name."
echo -e "Currently Logged: $(who -q | grep "=" | sed 's/.*=//') user(s)"
echo -e "User name: $USER (Login name: $LOGNAME)"

echo -e "\ne. Display current shell, home directory, operating system type, current path setting, current working directory."
echo -e "Current Shell: $SHELL"
echo -e "Home Directory: $HOME"
echo -e "Your O/s Type: $OSTYPE"
echo -e "PATH: $PATH"
echo -e "Current working directory: `pwd`"