import os
##获取文件路径下的所有文件，共18828个
rootdir = 'C:\\Users\\Administrator\\Desktop\\40152\\20newsgroups'
list = os.listdir(rootdir) #列出文件夹下所有的目录与文件
print ((rootdir+'\\'+list[0]))
path1 = []
for i in range(0,len(list)):
    path1.append(rootdir +'\\'+ list[i])
path_all = []
file_id = []
for i in range(0,len(path1)):
    list2 = os.listdir(path1[i])
    for j in range(0,len(list2)):
        path_all.append(path1[i] +'\\'+ list2[j])
    file_id.append(list2)
print(path_all[18827])
print(len(path_all))
print(file_id)
word_dict = {}
wcurrent = []
windex = 0
##(1)读入20newsgroup数据集20个文件夹中所有文件内容
##定义英文分词函数
def word_split(text):
    wcurrent = []
    windex = 0
    for j, c in enumerate(text):
        if c.isalnum():
            wcurrent.append(c)
        elif wcurrent:
            word = u''.join(wcurrent)
            word_dict[(path_all[i])[-5:]] = word
            windex += 1
            wcurrent = [] 
    if wcurrent:
        word = u''.join(wcurrent)
        word_list.append((windex, word))
        windex += 1
    return word_dict
##(2)创建单词字典{doc_id:word_id}
for i in range(0,len(path_all)):
    text = open(path_all[i],'r',encoding='cp936',errors='ignore').read()
    word_split(text)
##(3)为各个单词建立倒排索引
inverted_index = {}
for doc_id, words in word_dict.items():
    for word_id in words.keys():
        if word_id not in inverted_index.keys():
           inverted_index[word_id] = [doc_id]
        elif doc_id not in inverted_index[word_id]:
            inverted_index[word_id].append(doc_id)
#print(inverted_index)