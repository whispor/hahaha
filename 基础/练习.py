#str1 = ["明月出天山，苍茫云海间。  #1\n", "长风几万里，吹度玉门关。  #2\n", "汉下白登道，胡窥青海湾。  #3\n", "汉下白登道，胡窥青海湾。  #4\n", "由来征战地，不见有人还。  #5\n", "戍客望边色，思归多苦颜。  #6\n", "戍客望边色，思归多苦颜。  #7\n"]
# str1 = ["明月出天山，苍茫云海间。  \n", "长风几万里，吹度玉门关。  \n", "汉下白登道，胡窥青海湾。  \n", "汉下白登道，胡窥青海湾。  \n", "由来征战地，不见有人还。  \n", "戍客望边色，思归多苦颜。  \n", "戍客望边色，思归多苦颜。  \n"]
# a = enumerate(str1)
# print(str1)
# print(list(a))
with open("haha.txt", "r", encoding='utf-8') as f:
    lines = f.readline()
    lines = [value.rstrip()+"#"+str(index) for index, value in enumerate(lines)]

with open("haha.txt", "w", encoding='utf-8') as f:
    f.writelines(lines)