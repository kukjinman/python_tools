import numpy as np
from PIL import Image
from wordcloud import WordCloud
import matplotlib.pyplot as plt
#1 단어 모음이 있는 words_data.py에서 words import
from words_data import words

#2 words의 단어마다 ' ' 띄어쓰기 부여
text = ' '.join(words)

#3 단어구름 masking 이미지를 numpy의 배열 데이터로 변환
masking_image = np.array(Image.open("apple_img.png"))

#4 text와 mask이미지로 단어구름 wordcloud 객체 생성
wordcloud = WordCloud(width=800, height=400, mask = masking_image, background_color='lightgrey').generate(text)

#5 wordcloud 객체를 matplotlib을 사용하여 출력
plt.figure(figsize=(10, 5))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')
plt.show()