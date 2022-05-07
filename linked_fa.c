#include <stdio.h>
#include <stdlib.h>

int fArray[50] = {};
int last_known_block=0;

int checkPos(int f_idx, int fSize);
void allocateFile(int f_idx, int fSize);
void printArray(int array[]);

int main(){

    int f_idx, fSize, prealloc, prealloc_block;
    printf("Enter the number of blocks already allocated: ");
    scanf("%d", &prealloc);
    printf("Enter the blocks that are already allocated: ");    
    while(prealloc > 0){
        scanf("%d", &prealloc_block);
        fArray[prealloc_block] = 1;
        last_known_block = prealloc_block;
        --prealloc;
    }
    printf("\n");
input:
    while(1){
        f_idx=0, fSize=0;
        printf("Enter the start index of file: ");
        scanf("%d", &f_idx);

        if(checkPos(f_idx, fSize) != -1){
            printf("Block %d already allocated!\n", checkPos(f_idx, fSize));
            goto input;
        }else{
            printf("Enter the size of file: ");
            scanf("%d", &fSize);
            if(checkPos(f_idx, fSize) != -1){
                printf("Block already allocated!\n");
                goto input;
            }
            allocateFile(f_idx, fSize);
        }

        printf("Files allocated on block: ");
        printArray(fArray);

        int quit;
        printf("Enter 0 to add more files or 1 to quit: ");
        scanf("%d", &quit);
        if(quit == 1)
            goto exit;
    }

exit:
    return 0;
}

int checkPos(int f_idx, int fSize){
    if(fArray[f_idx] == 1)
            return f_idx;
    
    for(int i=f_idx; i<f_idx + fSize; i++){
        if(fArray[i] != 0)
            return i;
    }

    return -1;
}

void allocateFile(int f_idx, int fSize){
    for(int i=f_idx; i<f_idx + fSize; i++){
        fArray[i] = 1;
        printf("Block %d ---> %d\n", i, fArray[i]);
    }
    if(last_known_block == 0){
        printf("File allocated at block %d of size %d\n", f_idx, fSize);
    }else{
        printf("File allocated at block %d of size %d ----> %d\n", f_idx, fSize, last_known_block);
    }
    last_known_block = f_idx +fSize - 1;
}

void printArray(int *array){
    for(int i=0; i<50; i++){
        if(array[i] == 1){
            printf("%d ", i);
        }
    }
    printf("\n");
}