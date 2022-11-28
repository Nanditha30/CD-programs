def first(seq,gra,nonterm):
    first_=set()
    #print(seq)
    for i in seq:
        flag=0
        if i in nonterm:
            for j in gra[i]:
                first_= first_ | first(j,gra,nonterm)
                if '@' in first(j,gra,nonterm):
                    flag=1
            if flag==0:
                break
        else:
            first_=first_|{i}
            break
    return first_
def follow(var_nt,gra,nonterm):
    follow_=set()
    start_var=(list(gra.keys())[0])  
    if var_nt==start_var:
        follow_=follow_|{'$'}
    for left_v in gra:
        for prod in gra[left_v]:
            if prod!='@':
                for i in range(len(prod)):
                    if prod[i]==var_nt:
                        if i!=(len(prod)-1):
                            next_str=prod[(i+1):]
                            first_str=first(next_str,gra,nonterm)
                            if '@' in first_str:
                                follow_= follow_ | (first_str-{'@'})
                                if(left_v!=var_nt):
                                    follow_=follow_  | follow(left_v,gra,nonterm)
                            else:
                                follow_= follow_ | first_str
                        else:
                            if(left_v!=var_nt):
                                follow_=follow_  | follow(left_v,gra,nonterm)
    return follow_
def read_gra(fname):
    f=open(fname,"r")
    raw_gra=f.read()
    lines=raw_gra.split('\n')
    gra=dict({})
    for i in lines:
        words=i.split()
        prod=words[2].split('/')
        gra[words[0]]=prod
    return gra

first_set=dict({})
follow_set=dict({})

nonterm=[]
term=[]
n_nonterm=int(input("Enter number of non terminals: "))
print("Enter the non terminals:")
for i in range(n_nonterm):
    c=input()
    nonterm.append(c)

n_term=int(input("Enter number of terminals: "))
print("Enter the terminals:")
for i in range(n_term):
    c=input()
    term.append(c)

gra=read_gra("grammar.txt")
#print(gra)

for i in gra:
    first_set[i]=first(i,gra,nonterm)
for i in gra:
    follow_set[i]=follow(i,gra,nonterm)

print("First of Variables of Grammar: ",end='')
print(first_set)
print("Follow of Variables of Grammar: ",end='')
print(follow_set)