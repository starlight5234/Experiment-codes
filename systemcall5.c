#include <unistd.h>
#include <stdlib.h>
#include <stdio.h>
#include <errno.h>

int main(int argc, char **argv) {

    printf("Old ID %d\n", geteuid());
    if(seteuid(0) == -1)
        perror("seteuid faied");
    printf("New ID %d\n", geteuid());

    return 0;

}