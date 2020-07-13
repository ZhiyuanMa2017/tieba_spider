from collections import Counter
outputs = open('output3.txt', 'r',encoding='utf-8')
words = []
for line in outputs:
    items = line.strip('\n').strip('\t').strip(' ').split(' ')
    for i in items:
        if i !='':
            words.append(i)
result= dict(Counter(words))
sortlist = sorted(result.items(), key=lambda item: item[1], reverse=True)

cipinoutputs = open('cipinoutput.txt', 'w',encoding='utf-8')
for line in result:  # 这里的返回值是字符串
    cipinoutputs.write(line +' '+ str(result[line]) +'\n')

from wordcloud import WordCloud,ImageColorGenerator,STOPWORDS
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image

# image = Image.open('xuebi.png')
# img = np.array(image)

wordcloud = WordCloud(width=2000,height=1000,prefer_horizontal=1,scale=2,font_path = "simhei.ttf",max_words=5000).generate_from_frequencies(result)
# image_colors = ImageColorGenerator(img)
# wordcloud.recolor(color_func=image_colors)
wordcloud.to_file("505.png")

# wc = WordCloud(font_path = "simhei.ttf",background_color='white',max_font_size=150,mask=img)
# # WordCloud其他参数设置,random_state=42,max_words=2000,min_font_size=20
# wc.generate_from_frequencies(result)
# image_color = ImageColorGenerator(img)
# wc.recolor(color_func=image_color)
# # wc.to_file(r"D://ciyun/wordcloud1.png",dpi=3000)
# #图片的展示
# plt.imshow(wc)

import matplotlib.pyplot as plt
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")
plt.show()
wordcloud.to_file("501.png")