<?php
header('Content-Type: text/html; charset=utf-8');
header('Cache-Control: no-store, no-cache, must-revalidate, max-age=0');
header('Pragma: no-cache');
header('Expires: Thu, 01 Jan 1970 00:00:00 GMT');
$static_dir = __DIR__ . '/static';
$wordcloud_image = null;
$error_message = null;
if (!is_dir($static_dir)) {
    mkdir($static_dir, 0755, true);
}
if (!file_exists($static_dir . '/qrcode.png')) {
    $site_url = "https://" . $_SERVER['HTTP_HOST'] . "/";
    shell_exec("python3 qrcode_manager.py " . escapeshellarg($site_url));
}
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    $word_input = isset($_POST['word_input']) ? trim($_POST['word_input']) : '';
    if (!empty($word_input)) {
        // korcen을 사용한 비속어 검증 및 WordCloud 생성
        $output = shell_exec("python3 check_and_add_word.py " . escapeshellarg($word_input) . " 2>&1");

        if (strpos($output, 'ERROR:') !== false) {
            $error_message = "❌ 부적절한 단어입니다. 다른 단어를 입력해주세요.";
        } else {
            $wordcloud_image = 'static/wordcloud.png?' . time();
        }
    }
}
if (file_exists($static_dir . '/wordcloud.png') && !$wordcloud_image) {
    $wordcloud_image = 'static/wordcloud.png?' . time();
}
include('mainpage.php');
?>
