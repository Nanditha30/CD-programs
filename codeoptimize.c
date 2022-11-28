#include<stdio.h>
#include<string.h>
struct op
{
char l;
char r[20];
}
op[10],pr[10];
void main()
{
int a,i,k,j,n,z=0,m,q;
char *p,*l;
char temp,t;
char *tem;
printf("Enter the Number of Values:");
scanf("%d",&n);
for(i=0;i<n;i++)
{
printf("left: ");
scanf(" %c",&op[i].l);
printf("right: ");
scanf(" %s",&op[i].r);
}
printf("Intermediate Code\n") ;
for(i=0;i<n;i++)
{
printf("%c=",op[i].l);
printf("%s\n",op[i].r);
}
for(i=0;i<n-1;i++)
{
temp=op[i].l;
for(j=0;j<n;j++)
{
p=strchr(op[j].r,temp);
if(p)
{
pr[z].l=op[i].l;
strcpy(pr[z].r,op[i].r);
z++;
}
}
}
pr[z].l=op[n-1].l;
strcpy(pr[z].r,op[n-1].r);
z++;
printf("\nAfter Dead Code Elimination\n");
for(k=0;k<z;k++)
{
printf("%c\t=",pr[k].l);
printf("%s\n",pr[k].r);
}
for(m=0;m<z;m++)
{
tem=pr[m].r;
for(j=m+1;j<z;j++)
{
p=strstr(tem,pr[j].r);
if(p)
{
t=pr[j].l;
pr[j].l=pr[m].l;
for(i=0;i<z;i++)
{
l=strchr(pr[i].r,t) ;
if(l)
{
a=l-pr[i].r;
printf("pos: %d\n",a);
pr[i].r[a]=pr[m].l;
}}}}}
printf("Eliminate Common Expression\n");
for(i=0;i<z;i++)
{
printf("%c\t=",pr[i].l);
printf("%s\n",pr[i].r);
}
for(i=0;i<z;i++)
{
for(j=i+1;j<z;j++)
{
q=strcmp(pr[i].r,pr[j].r);
if((pr[i].l==pr[j].l)&&!q)
{
pr[i].l='\0';
}
}
}
printf("Optimized Code\n");
for(i=0;i<z;i++)
{
if(pr[i].l!='\0')
{
printf("%c=",pr[i].l);
printf("%s\n",pr[i].r);
}
}
}

p
c
q
b*p
r
c
s
b*r
t
q+s
a
t

tac={}
code=input("Enter 3 address code : ").split()
exp1=[]
exp2=[]
for i in code:
    x,y=i.split("=")
    exp1.append(x)
    exp2.append(y)
    tac[x]=y
print("=============================")
print("Intermediate code")
for k,v in tac.items():
    print(k,"=",v)

for k in exp1:
    delet=1
    for ex in exp2:
        if k in ex or tac[k] in exp1:
            delet=0
    if delet==1:
        del tac[k]
print("=============================")
print("After dead code elimination")
for k,v in tac.items():
    print(k,"=",v)
    
same={}
for k1,v1 in tac.items():
    for k2,v2 in tac.items():
        if v1==v2 and k1!=k2 and (k1 not in same and k2 not in same):
            same[k1]=k2
for k,v in same.items():
    del tac[k]
optimizetac={}
for k,v in tac.items():
    s1=v
    for s in s1:
        if s in same:
            v=v.replace(s,same[s])
    optimizetac[k]=v
print("=============================")
print("After common sub expression elimination")
for k,v in optimizetac.items():
    print(k,"=",v)
print("=============================")
print("Optimized code")
for k,v in optimizetac.items():
    print(k,"=",v)
Enter 3 address code : t1=a-b t2=a-c t3=t1+t2 d=t3+t2