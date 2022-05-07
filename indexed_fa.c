#include <stdio.h>
#include <stdlib.h>

int fArray[50], idx[50];
int size=50;

void printArray(int *array);
void undoAllocation(int *block, int *fArray,int f_idx, int block_index);
int main(){

    int f_idx, f_size, block[50]={};

    while(1){
    index_input:
        printf("Enter index block: ");
        scanf("%d", &f_idx);
        if(idx[f_idx] != 0){
            printf("Index already allocated!\n");
            goto index_input;
        }else{
            idx[f_idx] = 1;
        }

    size:
        printf("Enter the size of file: ");
        scanf("%d", &f_size);
        if(f_size > size){
            printf("File size greater than available!\n");
            goto size;
        }

    block:
        printf("Enter the blocks for index %d: ", f_idx);
        for(int i=0; i<f_size; i++){
            scanf("%d", &block[i]);
        }

        for(int i=0; i<50; ++i){
            if(block[i] != 0){
                if(fArray[block[i]] != 1){
                    fArray[block[i]] = 1;
                    printf("Index %d ----> Allocated block %d : %d\n", f_idx, block[i], fArray[block[i]]);
                    --size;
                }else{
                    printf("Block %d already allocated!\n", block[i]);
                    undoAllocation(block, fArray, f_idx, i);
                    goto block;
                }
            }
            
        }

        printf("Allocated blocks: ");
        printArray(fArray);

        for(int i=0; i<50; ++i){
            block[i]=0;
        }

        int quit;
        printf("Enter 0 to add more files or 1 to quit: ");
        scanf("%d", &quit);
        if(quit == 1)
            goto exit;
    }

exit:
    return 0;
}

void printArray(int *array){
    for(int i=0; i<50; i++){
        if(array[i] == 1){
            printf("%d ", i);
        }
    }
    printf("\n");
}

void undoAllocation(int *block, int *fArray, int f_idx, int block_index){
    for(int i=0; i<50; ++i){
        if(block[i] != 0 ){
            if(fArray[block[i]] == 1 && i != block_index){
                fArray[block[i]] = 0;
                printf("Index %d ----> Block %d unallocated : %d\n", f_idx, block[i], fArray[block[i]]);
                ++size;
            }
        }
    }
}