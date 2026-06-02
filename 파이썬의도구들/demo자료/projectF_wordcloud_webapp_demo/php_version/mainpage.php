<?php header("Content-Type: text/html; charset=utf-8"); ?>
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>WordCloud WebApp</title>
    <style>
        body {
            display: flex;
            flex-direction: column;
            align-items: center;
        }
        form, h1, img {
            margin-bottom: 13px;
        }
    </style>
</head>
<body>
    <h1>단어로 구름을 만드는 웹앱</h1>
    <form method="POST">
        <input type="text" name="word_input" placeholder="단어를 입력하세요!" required>
        <button type="submit">제출</button>
    </form>
    <img src="static/qrcode.png" width="200" height="200">

    <?php if ($wordcloud_image): ?>
        <img src="<?php echo $wordcloud_image; ?>" alt="WordCloud 이미지" width="400" height="400">
    <?php endif; ?>
</body>
</html>
