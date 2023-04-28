%{
#include <string.h>
int counter = 0;
char longestString[30];
%}

%%
[a-zA-Z]+ { if (yyleng > counter) {
	                    counter = yyleng;
                        strcpy(longestString,yytext);
                    }
                }
%%

int main() {
    yylex();
    printf("Largest length: %d\n", counter);
    printf("Largest word: %s\n", longestString);
    return 0;
}

