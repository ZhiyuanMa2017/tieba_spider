import jieba
jieba.load_userdict('gudingcikui.txt')
def stopwordslist(filepath):
    stopwords = [line.strip() for line in open(filepath, 'r', encoding='utf-8').readlines()]
    return stopwords

def seg_sentence(sentence):
    sentence_seged = jieba.cut(sentence.strip())
    outstr = ''
    for word in sentence_seged:
            if word != '\t':
                outstr += word
                outstr += " "
    return outstr

inputs = open('title.txt', 'r',encoding='utf-8')
outputs = open('output2.txt', 'w',encoding='utf-8')
for line in inputs:
    line_seg = seg_sentence(line)  # 这里的返回值是字符串
    outputs.write(line_seg + '\n')
outputs.close()
inputs.close()
