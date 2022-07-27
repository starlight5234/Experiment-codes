#include <stdio.h>
#include <stdlib.h>
#include <string.h>

char XOR(int a, int b){
    if(a == b)
        return '0';
    return '1';
}

int CRC(long int data, int key){
    
    int lenOfKey, lenOfData;

    char dataBuf[50];
    sprintf(dataBuf, "%ld", data);
    lenOfData = strlen(dataBuf);

    char keyBuf[10];
    sprintf(keyBuf, "%ld", key);
    lenOfKey = strlen(keyBuf);

    memset(dataBuf + lenOfData, '0', (lenOfKey-1));
    lenOfData = strlen(dataBuf);

    int dataIdx = 0, keyIdx = 0;
    int nonZeroIdx = dataIdx;
    int ignoreZero = 1;

    while((dataIdx + lenOfKey) <= lenOfData){
        if(ignoreZero){
            if(dataBuf[dataIdx] == '0'){
                dataIdx++;
                continue;
            }
            ignoreZero = 0;
            nonZeroIdx = dataIdx;
        }
        dataBuf[nonZeroIdx] = XOR(dataBuf[nonZeroIdx], keyBuf[keyIdx]);
        if(keyIdx+1>=lenOfKey){
            keyIdx = 0;
            ignoreZero = 1;
            nonZeroIdx = dataIdx;
        }else{
            keyIdx++;
        }
        nonZeroIdx++;
    }

    printf("Data: %d\n", data);
    printf("Key: %d\n", key);
    printf("CRC: ");
    for(int i=(lenOfData-lenOfKey+1); i<lenOfData; i++)
        printf("%d", dataBuf[i]-48);

    return 0;
}

int main(){

    long int data;
    int key;

    // printf("Data: ");
    // scanf("%ld", &data);
    // printf("Key: ");
    // scanf("%d", &key);

    data = 100100;
    key = 1101;

    CRC(data, key);

    return 0;
}