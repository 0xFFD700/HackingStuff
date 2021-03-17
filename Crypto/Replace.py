cipher = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
corresp =['e', 'd', 'f', 'b', 'g', 'n', 'x', 'c', 'w', 'o', 'r', 'p', 'h', 'n', 'i', 'q', 'k', 'r', 'v', 'l', 'u', 'v', 't', 'a', 's', 'm']
enflag = ''.lower()
deflag = ''

for i in range(len(enflag)):
    if enflag[i] == '_':
            deflag += '_'
            continue
    elif enflag[i] == ' ':
            deflag += ' '
            continue
    for j in range(len(cipher)):
        if enflag[i] == cipher[j]:
            deflag += corresp[j]

print(deflag)
