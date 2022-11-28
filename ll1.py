#Epsilon represented by @
#Starting Variable must be in the left hand side of first production
#Production Rules should be in the following format only
# A -> R/G/...

import numpy as np
from prettytable import PrettyTable

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

def ll1_parser(gra,nonterm,term):
    mat=np.array([["0"]*(len(term)+2)]*(len(nonterm)+1))
    mat=mat.astype('<U100')
    term.append('$')
    for i in range((len(nonterm)+1)):
        for j in range((len(term)+1)):
            if i==0 and j>=1:
                mat[i,j]=term[j-1]
            elif i>=1 and j==0:
                mat[i,j]=nonterm[i-1]

    isll1=True

    for left_v in gra:
        row_n=nonterm.index(left_v)+1
        for prod in gra[left_v]:
            first_rule=first(prod,gra,nonterm)
            if '@' in first_rule:
                first_rule=first_rule-{'@'}
                first_rule=first_rule | follow_set[left_v]
            for i in first_rule:
                col_n=term.index(i)+1
                if mat[row_n,col_n]=='0':
                    mat[row_n,col_n]=left_v+'->'+prod
                else:
                    mat[row_n,col_n]=mat[row_n,col_n]+'\n'+left_v+'->'+prod
                    isll1=False
    x=PrettyTable()
    x.field_names=mat[0]
    for i in range(len(mat)):
        if i>0:
            x.add_row(mat[i])
    print(x)
    if isll1:
        print("This grammar can be used for LL1 Parser")
    else:
        print("This grammar cannot be used for LL1 Parser")

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


follow_set=dict({})
first_set=dict({})

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
ll1_parser(gra,nonterm,term)
# E -> TB
# B -> +TB/@
# T -> FY
# Y -> *FY/@
# F -> (E)/i
# ------------------------
# def first(left, rules_map):
#     if ord(left) >= 65 and ord(left) <= 90:
#         ans = []
#         right = rules_map[left]
#         flag = 0
#         for p in right:
#             if ord(p[0]) >= 65 and ord(p[0]) <= 90:
#                 temp = first(p[0], rules_map)
#                 if 'e' in temp:
#                     ind = 0
#                     flag = 1
#                     while 'e' in temp:
#                         temp.remove('e')
#                         ind += 1
#                         if ind < len(p):
#                             temp += first(p[ind], rules_map)
#                 ans += temp 
                
#             else:
#                 ans.append(p[0])
        
#         if flag == 1:
#             ans.append('e')          
       
#         return list(dict.fromkeys(ans))  
    
#     else:
#         return [left]

# def follow_helper(left, ind, p, follows, rules_map):
#     if ind == len(p):
#         if left in follows:
#             temp = follows[left]
#         else:
#             temp = follow(left, rules_map, follows)
#     else:
#         temp = first(p[ind], rules_map)
    
#     return temp
    
# def follow(symbol, rules_map, follows):
#     ans = []
    
#     for left, right in rules_map.items():
#         for p in right:
#             ind = p.find(symbol)
#             if ind != -1:
#                 if ind == len(p)-1:
#                     if left in follows:
#                         temp = follows[left]
#                     else:
#                         if symbol != left:
#                             temp = follow(left, rules_map, follows)
#                 else:
#                     temp = first(p[ind+1], rules_map)
                
#                 if 'e' in temp:
#                     ind += 1
#                     while 'e' in temp:
#                         temp.remove('e')
#                         ind += 1
#                         if ind <= len(p):
#                             temp += follow_helper(left, ind, p, follows, rules_map)
                        
#                 ans += temp    
                    
#     return list(dict.fromkeys(ans))
           
# def ll1parser(rules, rules_map, ss, non_terminals, terminals, terminals_map):
#     firsts = {}
#     for left in rules_map:
#         ans = first(left, rules_map)
#         print(f'FIRST({left}) = {ans}')
#         firsts[left] = ans
        
#     print()    
        
#     follows = {}    
#     for left in rules_map:
#         ans = follow(left, rules_map, follows)
#         if left == ss:
#             ans = ['$'] + ans
#         print(f'FOLLOW({left}) = {ans}')  
#         follows[left] = ans
        
#     print()
#     print('Parsing Table:')
#     print()
    
#     #print(non_terminals)
#     #print(terminals)
#     #print(terminals_map)
    
#     m = len(non_terminals)
#     n = len(terminals)
    
#     parsing_table = [[[] for j in range(n)] for i in range(m)]

#     print('',end='     ')
#     for t in terminals:
#         print(t, end = '       ')

#     print()    
    
#     for i in range(len(non_terminals)):
#         left = non_terminals[i]
#         for p in rules_map[left]:
#             ind = 0
            
#             if p[0] != 'e':
#                 ts = first(p[0], rules_map)
#             else:
#                 ts = follows[left]
            
#             for t in ts:
#                 if t == 'e':
#                     ind += 1
#                     if ind < len(p):
#                         ts += first(p[ind], rules_map)
#                     continue
#                 j = terminals_map[t]
#                 parsing_table[i][j].append(f'{left}->{p}')
            
#             if ind == len(p):
#                 ts = follows[left]
#                 for t in ts:
#                     j = terminals_map[t]
#                     parsing_table[i][j].append(f'{left}->{p}')
    
#     #print(parsing_table)   
    
#     for i in range(m):
#         print(non_terminals[i], end='  ')
#         for j in range(n):
#             print(parsing_table[i][j], end =' ')
#         print()    

# rules=["S->ACB|Cbb|Ba",
#        "A->da|BC",
#        "B->g|e",
#        "C->h|e"]
       
# rules2 = ["E->TL",
#           "L->+TL|e",
#           "T->FM",
#           "M->*FM|e",
#           "F->(E)|i"]    

# rules_map = {}
# non_terminals = []
# terminals = []

# for rule in rules:
#     temp = rule.split('->')
#     left = temp[0]
#     non_terminals.append(left)
#     right = temp[1]
#     parts = right.split('|')
    
#     for p in parts:
#         for s in p:
#             if (ord(s) >= 65 and ord(s) <= 90) or s == 'e':
#                 pass
#             else:
#                 if s not in terminals:
#                     terminals.append(s)
                    
#     rules_map[left] = parts

# terminals.append('$')    

# terminals_map = {}
# for i in range(len(terminals)):
#     terminals_map[terminals[i]] = i

# print(rules)   
# ss = 'S'
# ll1parser(rules, rules_map, ss, non_terminals, terminals, terminals_map)
