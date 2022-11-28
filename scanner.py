#: To develop a lexical analyser for identifiers, constants, operators, etc, and get lexemes line wise.
# int main()
# {
# return x + y;
# }
keyword = ['break','case','char','const','countinue','deafult','do','int','else','enum','extern','float',
           'for','goto','if','long','register','return','short','signed','sizeof','static','switch','typedef',
           'union','unsigned','void','volatile','while']
built_in_functions = ['printf','scanf','main']
operators = ['+','-','*','/','%','==','!=','>','<','>=','<=','&&','||','!','&','|','^','~','>>','<<','=','+=','-=','*=']
#specialsymbol = ['@','#','$','_','!']
#separator = [',',':',';','\n','\t','{','}','(',')','[',']']
specialchars = ['@','#','$','_','!',',',':',';','\n','\t','{','}','(',')','[',']']

keywords_count = 0
operators_count = 0
strings_count = 0
constants_count = 0
special_chars_count = 0
identifiers_count = 0

line = 1

print('LineNo','Lexeme','Token')

f = open('tokenseperator.c', 'r')
while True:
    c = f.read(1)
    if not c:
        break

    if c.isdigit():
        #print(c)
        temp = ''
        while c.isdigit() or c == '.':
            temp += c
            c = f.read(1)

        constants_count += 1
        print(line,'     constant',temp)
        
    if c == '"':
        temp = ''
        c = f.read(1)
        while c != '"':
            temp += c
            c = f.read(1)

        strings_count += 1
        print(line,'     string',temp)

    if ord(c) >= 97 and ord(c) <= 122:
        temp = c
        c = f.read(1)
        while ord(c) >= 97 and ord(c) <= 122:
            temp += c
            c = f.read(1)

        if temp in keyword:
            keywords_count += 1
            print(line,'     keyword',temp)
        elif temp in built_in_functions:
            print(line,'     builtinfunction',temp)
        else:
            identifiers_count += 1
            print(line,'     identifier',temp)

    if c in operators:
        temp = ''
        while c in operators:
            temp += c
            c = f.read(1)

        f.seek(f.tell() - 1, 0)
        operators_count += 1
        print(line,'     operator',temp)

    #if c in specialsymbol:
    #    print('special symbol:',c)

    if c in specialchars:
        special_chars_count += 1
        if c == '\n':
            print(line,'     Special Character \\n')
            line += 1
        elif c== '\t':
            print(line,'     Special Character \\t')
        else:
            print(line,'     Special Character',c)

f.close()

print('Keywords:',keywords_count)
print('Operators:',operators_count)
print('Constants:',constants_count)
print('Identifiers:',identifiers_count)
print('Strings:',strings_count)
print('Special Characters:',special_chars_count)