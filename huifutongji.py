huifu = open('zuozheandhuifu.txt', 'r',encoding='utf-8')
huifushu = []
nameshu=[]
for line in huifu:
    items = line.strip('\n').strip('\t').split()
    huifushu.append(items)
    nameshu.append(items[0])

huifushu[0] = huifushu[0][1:]

counthuifu = {}
for i in range(len(huifushu)):
    if huifushu[i][0] not in counthuifu:
        counthuifu[huifushu[i][0]] = int(huifushu[i][1])
    else:
        counthuifu[huifushu[i][0]] += int(huifushu[i][1])

huifutongji = open('huifutongji.txt', 'w',encoding='utf-8')
for line in counthuifu:  # 这里的返回值是字符串
    huifutongji.write(line +' '+ str(counthuifu[line]) +'\n')



namelist = list(counthuifu.keys())
nameshu.count(namelist[0])

fatieliang = []
for i in range(len(namelist)):
    fatieliang.append([namelist[i],int(counthuifu[namelist[i]]),int(nameshu.count(namelist[i])),int(counthuifu[namelist[i]])/int(nameshu.count(namelist[i]))])

huifubijiao = open('huifubijiao3.txt', 'w',encoding='utf-8')
for iii in fatieliang:  # 这里的返回值是字符串
    huifubijiao.write(str(iii[0])+'\t'+str(iii[1])+'\t'+str(iii[2])+'\t'+str(iii[3])+'\n')