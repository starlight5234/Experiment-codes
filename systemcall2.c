#include <stdio.h>
#include <sys/types.h>
#include <stdlib.h>
#include <unistd.h>

int main(void){
    pid_t pid;

    if ((pid = fork())<0)
    {
        printf("Problem Forking.\n");
        exit(1);
    }
    else if (pid==0)
    {
        printf("This is a child process.\n");
    }
    else
    {
        printf("This is a parent process & process ID of the new child.\n");
    }
    return 0;
}
