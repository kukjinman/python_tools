# WordCloud WebApp - PHP 버전 (카페24용)

## 폴더 구조
```
php_version/
├── index.php              ← 메인 진입점 (Flask의 app.route 대체)
├── mainpage.php           ← 템플릿 (templates/mainpage.html 대체)
├── wordcloud_manager.py   ← 워드클라우드 생성 (Python, 재사용)
├── qrcode_manager.py      ← QR코드 생성 (Python, 재사용)
├── requirement.txt        ← Python 패키지 목록
├── static/
│   ├── apple_img.png      ← 마스킹 이미지 (직접 넣어주세요)
│   ├── wordcloud.png      ← 자동 생성됨
│   ├── qrcode.png         ← 자동 생성됨
│   └── words.json         ← 단어 저장 파일 (자동 생성)
└── README.md              ← 현재 파일
```

## 카페24 배포 방법

### 1. Python 패키지 설치 (SSH 접속 후)
```bash
pip install -r requirement.txt
```

### 2. static 폴더에 apple_img.png 업로드
기존 Flask 버전의 `static/apple_img.png`를 그대로 복사

### 3. 파일 업로드
FTP 또는 SSH로 `php_version/` 내 모든 파일을 웹 루트에 업로드

### 4. 권한 설정
```bash
chmod 755 wordcloud_manager.py qrcode_manager.py
chmod 777 static/
```

## Flask → PHP 변환 비교

| Flask (기존) | PHP (카페24) |
|---|---|
| `@app.route('/', methods=['GET','POST'])` | `index.php`의 `$_SERVER['REQUEST_METHOD']` |
| `render_template('mainpage.html', ...)` | `include('mainpage.php')` |
| `url_for('static', filename='...')` | `'static/...'` 직접 경로 |
| `{% if %}...{% endif %}` | `<?php if (): ?>...<?php endif; ?>` |
| `{{ variable }}` | `<?php echo $variable; ?>` |
| `wordcloud_manager.add_word()` | `shell_exec("python3 wordcloud_manager.py ...")` |

## 핵심 차이점
- Flask는 메모리에 단어 리스트를 유지하지만, PHP는 요청마다 프로세스가 새로 시작됨
- 따라서 PHP 버전에서는 `static/words.json`에 단어를 파일로 저장하여 영속성을 유지합니다.

