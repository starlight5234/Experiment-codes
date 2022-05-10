#include <stdio.h>
#include <stdlib.h>

int sys_time=0;
int idle=0;

struct process{
    int pid;
    int at;
    int bt;
    int ct;
    int tat;
    int wt;
    int executed;
};

void fcfs(struct process *proc, int n);
void printProcs(struct process *proc, int n);
void sort(struct process *proc, int n);
void swap(struct process *a, struct process *b);

int main(){

    int n;
    printf("Enter the number of processes: ");
    scanf("%d", &n);

    struct process *proc = (struct process *)malloc(n* sizeof(struct process));

    for(int i=0; i<n; ++i){
        proc[i].pid = i+1;
        printf("Enter the Arrival Time of Proccess %d: ", i+1);
        scanf("%d", &proc[i].at);

        printf("Enter the Burst Time of Proccess %d: ", i+1);
        scanf("%d", &proc[i].bt);

        proc[i].ct=0;
        proc[i].tat=0;
        proc[i].wt=0;
        proc[i].executed=0;
    }

    sort(proc, n);
    fcfs(proc, n);
    printProcs(proc, n);

    return 0;
}

void sort(struct process *proc, int n){
    for(int i=0; i<n; i++){
        for(int j=0; j<i; j++){
            if(proc[j].at > proc[i].at)
                swap(&proc[i], &proc[j]);
            
            if(proc[j].at == proc[i].at)
                if(proc[j].pid > proc[i].pid)
                    swap(&proc[i], &proc[j]);
        }
    }
}

void swap(struct process *a, struct process *b){
    struct process temp = *a;
    *a = *b;
    *b = temp;
}

void printProcs(struct process *proc, int n){
    printf("\nPid\tAT\tBT\tCT\tTAT\tWT\n");
    float avg_tat = 0;
    float avg_wt = 0;
    for(int i=0; i<n; i++){
        printf("%d\t%d\t%d\t%d\t%d\t%d\n", proc[i].pid, proc[i].at, 
            proc[i].bt, proc[i].ct, proc[i].tat, proc[i].wt);
        avg_tat += proc[i].tat;
        avg_wt += proc[i].wt;
    }

    printf("Average TAT: %.2f\n", (avg_tat/n));
    printf("Average WT: %.2f\n", (avg_wt/n));
    printf("CPU Idle time: %d\n", idle);
}

void fcfs(struct process *proc, int n){
    for(int i=0; i<n; i++){
        check:
        if(proc[i].at <= sys_time){
            sys_time += proc[i].bt;
            //printf("%d\n", sys_time);
            proc[i].ct = sys_time;
            proc[i].tat = proc[i].ct - proc[i].at;
            proc[i].wt = proc[i].tat - proc[i].bt;
        }else{
            idle++;
            sys_time++;
            goto check;
        }
    }
}