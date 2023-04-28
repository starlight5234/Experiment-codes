
%{
#include<stdio.h>
#include<stdlib.h>
int flag,c,j;
%}

%%
[0-9]+ {c=atoi(yytext);
		if(c==2){
		    printf("Prime number\n");
		}else if(c==0 || c==1){
		    printf("Not a Prime number\n");
		}else{
		    for(j=2;j<c;j++){
		        if(c%j==0)
		            flag=1;
		    }
		    if(flag==1)
	    	    printf("Not a prime number\n");
		    else if(flag==0)
    		    printf("Prime number\n");
		}
	}
%%

int main()
{
yylex();
return 0;
}

