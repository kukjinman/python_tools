#!/usr/bin/env python3
"""
check_and_add_word.py - Korcen을 사용한 비속어 검증 및 WordCloud 생성
사용법: python3 check_and_add_word.py "단어"
"""
import sys
import json
import os
import numpy as np
from PIL import Image
from wordcloud import WordCloud
from korcen import korcen

static_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'static')
words_file = os.path.join(static_dir, 'words.json')

# 마스킹 이미지
masking_image = np.array(Image.open(os.path.join(static_dir, 'apple_img.png')))


def is_bad_word(word):
    """Korcen을 사용하여 비속어 포함 여부 확인"""
    # korcen.check(text, id=None, foreign=False)
    # text: 검사할 텍스트
    # id: None (한글 일반 비속어 검사)
    # foreign: False (한글 검사)
    return korcen.check(word)


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

    # Korcen으로 비속어 검증
    if is_bad_word(new_word):
        print("ERROR: 부적절한 단어입니다.")
        return False

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

    print(f"Word '{new_word}' added successfully.")
    return True


if __name__ == '__main__':
    if len(sys.argv) > 1:
        word = sys.argv[1]
        add_word(word)
    else:
        print("Usage: python3 check_and_add_word.py <word>")






