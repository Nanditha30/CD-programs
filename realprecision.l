Int[0-9]+
Real[0-9]+[.][0-9]+
%%
{Int} printf("this is an Integer");
{Real} printf("this is a real number");
%%
main()
{
yylex();
}
int yywrap()
{
return 1;
}
