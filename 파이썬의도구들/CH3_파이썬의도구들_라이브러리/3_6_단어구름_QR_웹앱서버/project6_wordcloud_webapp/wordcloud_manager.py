import numpy as np
from PIL import Image
from wordcloud import WordCloud
import os


words = []
masking_image = np.array(Image.open("apple_img.png"))

#7 add_word 함수
def add_word(new_word):
    global words
    # print(words)
    words.append(str(new_word))
    text = ' '.join(words)
    wordcloud = WordCloud(mask = masking_image, background_color='lightgrey', include_numbers=True).generate(text)

    #8 static 폴더 생성 및 wordcloud.png 저장
    if not os.path.exists('./static'):
        os.makedirs('./static', exist_ok=True)

    wordcloud.to_file("./static/wordcloud.png")