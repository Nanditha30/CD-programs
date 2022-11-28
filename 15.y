%{
#include<stdio.h>
#include<stdlib.h>
%}

%token DIGIT LETTER UND NL

%%
stmt: variable NL {printf("valid identifiers\n"); exit(0);}
;
variable: LETTER alphanumeric
;
alphanumeric: LETTER alphanumeric | DIGIT alphanumeric | UND alphanumeric | LETTER | DIGIT | UND
;

%%

int yyerror(char *msg)
{
 printf("Invalid variable\n");
 exit(0);
}

main()
{
 printf("enter the variable: \n");
 yyparse();
}



%{
#include<stdio.h>
int valid=1;
%}
%token digit letter

%%
start : letter s
s : letter s
| digit s
|
;
%%

int yyerror()
{
printf("\nIts not a identifier!\n");
valid=0;
return 0;
}

int main()
{
printf("\nEnter a name to tested for identifier ");
yyparse();
if(valid)
{
printf("\nIt is a identifier!\n");
}
}