# 定义HTML内容
code = [
    "<!DOCTYPE html>",
    "<html>",
    "<head>",
    "<meta charset=\"utf-8\">",
    "<title>2017年海南红树林分类结果</title>",
    "<style>",
    "body {",
    "  background-image: url('background.png');",  # 设置背景图片
    "  background-size: cover;",
    "  font-family: Arial, sans-serif;",
    "}",
    "h1 {",
    "  text-align: center;",
    "  color: #fff;",
    "}",
    "h2 {",
    "  text-align: center;",
    "  color: #ff0;",
    "  cursor: pointer;",
    "}",
    "</style>",
    "</head>",
    "<body>",
    "<h1>2017年海南红树林分类结果</h1>",
    "<h2 onclick=\"window.location.href='dongzhai.html';\">东寨港</h2>",
    "<h2 onclick=\"window.location.href='huachangwan.html';\">花场湾</h2>",
    "</body>",
    "</html>"
]

# 写入HTML文件
with open("index.html", "w", encoding="utf-8") as outfile:
    for line in code:
        outfile.write(line + '\n')

# 打开HTML文件
import webbrowser
webbrowser.open("index.html")
