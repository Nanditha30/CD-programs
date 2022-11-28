%{
int comment=0;
int l=1;
%}
id [a-z][a-z0-9]*
%%
#.* {printf("%d\t",l);printf("%s is a PREPROCESSOR DIRECTIVE\n",yytext);}
int|double|char {printf("\n");printf("%d\t",l);printf("%s is a KEYWORD\n",yytext);}
if|then|endif|for|while|return {printf("\n");printf("%d\t",l);printf("%s is a
KEYWORD\n",yytext);}
else {printf("%d\t",l);printf("%s is a KEYWORD\n",yytext);}
"/*" {comment=1;}
"*/" {comment=0;}
{id}\( {if(!comment)printf("\n");printf("%d\t",l);printf("FUNCTION %s\n",yytext);}
{id}(\[[0-9]*\])? {if(!comment)printf("\n");printf("%d\t",l);printf("%s identifier\n",yytext);}
\{ {if(!comment) printf("\n");printf("%d\t",l);printf("%s BLOCK BEGINS\n",yytext); }
\} {if(!comment) printf("\n");printf("%d\t",l);printf("%s BLOCK ends\n",yytext); }
\".*\" {if(!comment)printf("\n");printf("%d\t",l);printf("%s is a STRING\n",yytext);}
[+\-]?[0-9]+ {if(!comment)printf("\n");printf("%d\t",l);printf("%s is a NUMBER\n",yytext);}
\( {if(!comment)printf("\n");printf("%d\t",l);printf("( is delim openparanthesis\n");}
\) {if(!comment)printf("\n");printf("%d\t",l);printf(") is delim closed paranthesis\n");}
\; {if(!comment)printf("\n");printf("%d\t",l);printf("; is delim semicolon\n");}
\, {if(!comment)printf("\n");printf("%d\t",l);printf(", is comma\n");}
\= {if(!comment)printf("\n");printf("%d\t",l);printf("%s is an ASSIGNMENT
OPERATOR\n",yytext);}
\<|\> {printf("\n");printf("%d\t",l);printf("%s is relational operator\n",yytext);}
"+"|"-"|"*"|"/" {printf("\n");printf("%d\t",l);printf("%s is an operator\n",yytext);}
"\n" {l=l+1;}
%%
main(int argc ,char **argv)
{

if (argc > 1)
yyin = fopen(argv[1],"r");
else
yyin = stdin;
yylex();
printf ("\n");
}
int yywrap(){
return 0;
}
# %{
# int COMMENT=0;
# %}
# id [a-z][a-z0-9]*
# %%
# #.* {printf("\n%s is a PREPROCESSOR DIRECTIVE",yytext);}
# int|double|char {printf("\n %s is a KEYWORD",yytext);}
# if|then|endif|for|while {printf("\n %s is a KEYWORD",yytext);}
# else {printf("\n %s is a KEYWORD",yytext);}
# "/*" {COMMENT=1;}
# "*/" {COMMENT=0;}
# {id}\( {if(!COMMENT)printf("\n\nFUNCTION\n %s",yytext);}
# {id}(\[[0-9]*\])? {if(!COMMENT) printf("\n %s identifier",yytext);}
# \{ {if(!COMMENT) printf("\n BLOCK BEGINS");ECHO; }
# \} {if(!COMMENT)printf("\n BLOCK ends");ECHO; }
# \".*\" {if(!COMMENT)printf("\n %s is a STRING",yytext);}
# [+\-]?[0-9]+ {if(!COMMENT)printf("\n %s is a NUMBER",yytext);}
# \( {if(!COMMENT)printf("\n ( is delim openparanthesis");}
# \) {if(!COMMENT)printf("\n ) is delim closed paranthesis");}
# \; {if(!COMMENT)printf("\n ; is delim semicolon");}
# \= {if(!COMMENT)printf("\n %s is an ASSIGNMENT OPERATOR",yytext);}
# \<|\> {printf("\n %s is relational operator",yytext);}
# "+"|"-"|"*"|"/" {printf("\n %s is an operator",yytext);}
# "\n" ;
# %%
# int main()
# {
# yylex ();
# }
# int yywrap()
# {
# return 1;
# }
# main(int argc ,char **argv)
# {
# if (argc > 1)
# yyin = fopen(argv[1],"r");
# else
# yyin = stdin;
# yylex();
# printf ("\n");
# }
# int yywrap()
# {
# return 0;
# }