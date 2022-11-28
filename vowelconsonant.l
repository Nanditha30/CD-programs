%{

int vowel_cnt=0,consonant_cnt=0;

%}

vowel [aeiou]+

consonant [^aeiou]

eol \n

%%

{eol} return 0;

[\t]+ ;

{vowel} {vowel_cnt++;}

{consonant} {consonant_cnt++;}




%%

int main()

{

printf("\n Enter some input string:\n");

yylex();

printf("Vowels=%d and consonant=%d\n",vowel_cnt,consonant_cnt);

return 0;

}

int yywrap()

{

return 1;

}

Vowel[aeiou|AEIOU]
Consonant[b-d|B-Df-h|F-Hj-n|J-Np-t|P-Tv-z|V-Z]

%%
{Vowel} printf("this is an Vowel");
{Consonant} printf("this is a Consonant");
%%
main()
{
yylex();
}
int yywrap()
{
return 1;
}

