%{
#include<stdio.h>
%}

%%
[\t ]+ ;
[?:]+ { printf("%s is Ternary Operator\n", yytext);}
\+|\-|\*|\/ { printf("%s is Arithmetic Operator\n", yytext);}
\==|\<=|\>=|\<|\>|\!= { printf("%s is Relational Operator\n", yytext);}
\=|\+=|\-=|\*=|\/= { printf("%s is Assignment Operator\n", yytext);}
\++|\-- { printf("%s is Unary Operator\n", yytext);}
\n { ECHO;}
%%

int main()
{
	while(yylex());
}

int yywrap( )
{
	return 1;
}
