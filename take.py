
if __name__ == "__main__":
    teachers=[]
    final_teachers=[]
    groups=[]
    f=open('modules.txt','r')
    for i in f:
        arr=i.split('*')
        if arr[1]=='  ':
            pass
        else:
            if '/' in arr[2]:
                b=arr[2].split('/')
                teachers.append(b[0])
                teachers.append(b[1])
            else:
                teachers.append(arr[2])
            group=arr[len(arr)-1].split('\n')[0][1:]
            groups.append(group)
    for i in teachers:
        teacher1=i[1:]
        teacher=teacher1[:-1]
        final_teachers.append(teacher)
    final_teachers=list(dict.fromkeys(final_teachers))
    groups=list(dict.fromkeys(groups))
    f.close()
    f=open('teachers.txt','w')
    g=open('groups.txt','w')
    for i in final_teachers:
        f.write(i)
        f.write('\n')
    for i in groups:
        g.write(i)
        g.write('\n')
    