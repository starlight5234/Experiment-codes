#include<unistd.h>
#include<stdio.h>
#include<fcntl.h>

int main()
{
    int fd;
    char buffer[80];
    char msg[50] = "OS Expt 2\n";
    fd = open("fl1.txt", O_RDWR);
    printf("fd = %d\n",fd);
    if(fd != -1){
        printf("fl1.txt opened with read write access.\n");
        write(fd, msg, sizeof(msg));
        lseek(fd, 0, SEEK_SET);
        read(fd, buffer, sizeof(msg));
        printf("Message was written to my file.\n");
        close(fd);
    }
    return 0;
}