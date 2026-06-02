<?php
header('Content-Type: text/html; charset=utf-8');
header('Cache-Control: no-store, no-cache, must-revalidate, max-age=0');
header('Pragma: no-cache');
header('Expires: Thu, 01 Jan 1970 00:00:00 GMT');
$static_dir = __DIR__ . '/static';
$wordcloud_image = null;
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
        shell_exec("python3 wordcloud_manager.py " . escapeshellarg($word_input));
        $wordcloud_image = 'static/wordcloud.png';
    }
}
if (file_exists($static_dir . '/wordcloud.png')) {
    $wordcloud_image = 'static/wordcloud.png?' . time();
}
include('mainpage.php');
?>
