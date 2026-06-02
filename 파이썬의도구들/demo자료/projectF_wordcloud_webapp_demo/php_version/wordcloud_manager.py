#!/usr/bin/env python3
"""
wordcloud_manager.py - PHP에서 shell_exec으로 호출 가능한 워드클라우드 생성기
사용법: python3 wordcloud_manager.py "단어"
"""
import numpy as np
from PIL import Image
from wordcloud import WordCloud
import os
import sys
import json

static_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'static')
words_file = os.path.join(static_dir, 'words.json')
masking_image = np.array(Image.open(os.path.join(static_dir, 'apple_img.png')))


def load_words():
    """저장된 단어 목록 불러오기"""
    if os.path.exists(words_file):
        with open(words_file, 'r', encoding='utf-8') as f:
            return json.load(f)
    return []


def save_words(words):
    """단어 목록 저장"""
    with open(words_file, 'w', encoding='utf-8') as f:
        json.dump(words, f, ensure_ascii=False)


def add_word(new_word):
    """단어를 추가하고 워드클라우드 이미지를 생성"""
    words = load_words()
    words.append(str(new_word))
    save_words(words)

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

    if not os.path.exists(static_dir):
        os.makedirs(static_dir, exist_ok=True)

    png_path = os.path.join(static_dir, 'wordcloud.png')
    wordcloud.to_file(png_path)


if __name__ == '__main__':
    if len(sys.argv) > 1:
        word = sys.argv[1]
        add_word(word)
        print(f"Word '{word}' added successfully.")
    else:
        print("Usage: python3 wordcloud_manager.py <word>")

