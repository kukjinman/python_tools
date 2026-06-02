import numpy as np
from PIL import Image
from wordcloud import WordCloud
import os

words = []
static_dir = os.path.join(os.path.dirname(__file__), 'static')
masking_image = np.array(Image.open(f"{static_dir}/apple_img.png"))

#5 add_word 함수
def add_word(new_word):
    # print(words)
    words.append(str(new_word))
    text = ' '.join(words)

    # 한글 폰트 경로 (macOS)
    font_path = '/System/Library/Fonts/AppleSDGothicNeo.ttc'
    if not os.path.exists(font_path):
        # 다른 한글 폰트 시도
        font_path = '/Library/Fonts/NotoSansKR-Regular.otf'
    if not os.path.exists(font_path):
        # 기본 Arial
        font_path = None

    wordcloud = WordCloud(
        mask=masking_image,
        background_color='lightgrey',
        include_numbers=True,
        font_path=font_path
    ).generate(text)

    #6 static 폴더 생성 및 wordcloud.png 저장
    if not os.path.exists(static_dir):
        os.makedirs(static_dir, exist_ok=True)

    png_path = os.path.join(static_dir, 'wordcloud.png')

    wordcloud.to_file(png_path)