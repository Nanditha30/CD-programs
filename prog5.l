identifier ^[A|a][a-z|A-Z]+

%%
{identifier} printf("Identifier starting with a");


%%
main()
{
yylex();
}
int yywrap()
{
return 1;
}

