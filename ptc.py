if __name__ == '__main__':
    N = int(input())
    s = []
    for i in range(N):
        com = input().split()
        if(com[0] == 'insert'):
            s.insert(int(com[1]), int(com[2]))
        elif(com[0] == 'print'):
            print(s)
        elif(com[0] == 'remove'):
            s.remove(int(com[1]))
        elif(com[0] == 'append'):
            s.append(int(com[1]))
        elif(com[0] == 'sort'):
            s.sort()
        elif(com[0] == 'pop'):
            s.pop()
        elif(com[0] == 'reverse'):
            s.reverse()
        