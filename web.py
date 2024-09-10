# 定义HTML内容
code = [
    "<!DOCTYPE html>"
    "<html>"
    "<head>"
   "<meta charset='utf-8'>"
    "<title>红树林分类结果</title>"
    "<style>"
    "  body {"
    "    background-image: url('background3.jpg'); /* 更新背景图片路径 */"
    "    background-size: cover;"
    "    font-family: Arial, sans-serif;"
    "    color: #fff;"
    "    margin: 0;"
    "    padding: 0;"
    "    display: flex;"
    "  }"
    ""
    
    
    "  .side-menu {"
    "    width: 300px;"
    "    padding: 50px 0;"
    "    background: rgba(0, 0, 0, 0.6);"
    "    position: fixed;"
    "    left: 0;"
    "    top: 0;"
    "    height: 100%;"
    "    overflow: auto;"
    "  }"
    
    
    ""
    "  .side-menu h2 {"
    "    color: #fff; /* 更新标题颜色 */"
    "    cursor: pointer;"
    "    margin:0 0 80px 100px; /* 左边距100px, 上下边距50px */"
    "    display: inline-block;"
    "  }"
    
    

   "  .header {"
    "    text-align: center;"
    "margin-left: 300px; "
    "padding: 20px;"

  
   
   "  }"
  
   "  .content-area {"
   "    color: #000; /* 更新标题颜色 */"
    "    font-size: 20px; /* 仿宋小二字体大小 */"
    "line-height: 1.8;"
    "background: rgba(255, 255, 255, 0.6);"
   "padding-top: 20px; /* 上内边距 */"
    "padding-right: 20px;  /* 右内边距 */"
    "padding-bottom: 20px; /* 下内边距 */"
    "padding-left: 20px;  /* 左内边距 */"




   "    margin-top: 50px;"
   "    margin-left:310px"
 

    

   
   "  }"
    
    
   "  .main-title {"
   "    font-family: Arial, sans-serif;"
   "    font-size: 12px; /* 仿宋小二字体大小 */"
   
    "    margin-bottom: 20px;"
   "  }"

   "  .image-gallery {"
   "    display: flex;"
   "    gap: 80px;"
   "    margin-top: 20px;"
   "  }"
   "  .image-gallery img {"
   "    width: 260px;"
   "    height: 210px;"
   "  }"

    "  .download-link {"
    "    margin-top: 20px;"
    "    display: block;"
    "    color: #ff0;"
    "  }"
    "</style>"
    "</head>"
    "<body>"
    "<div class='side-menu'>"
    "  <h2 onclick='loadContent(\"2019 新盈港\")'>2019 新盈港</h2>"
    "  <h2 onclick='loadContent(\"2019 花场湾\")'>2019 花场湾</h2>"
    "  <h2 onclick='loadContent(\"2022 新盈港\")'>2022 新盈港</h2>"
    "  <h2 onclick='loadContent(\"2023 花场湾\")'>2023 花场湾</h2>"
    "</div>"
    "<div class='content'>"
    "  <div class='header'>"
    "    <h1>花场湾与新盈港红树林破坏与修复</h1>"
    "  </div>"
    "  <div class='content-area' id='content-area'>"
    "    <p>      红树林作为热带和亚热带海岸潮间带的特殊湿地生态系统，对生态平衡和生物多样性保护具有重要价值。海南红树林是我国红树林中连片面积最大、树种最多、林分质量最好、生物多样性最丰富的区域。近年来，国家以及海南对红树林保护措施加大，但仍然存在一定的疏漏。遥感技术因其覆盖范围广、数据量大、更新周期短等优势已成为监测红树林的关键工具遥感技术实现对于红树林信息提取的研究可以分为三个方面，分别是结合多种指数及物候信息的随机森林RF分类、多尺度分割、利用深度学习方法的语义分割。产品元数据为融合了NDVI，NDWI，SAVI和MVI四种指数的经过预处理的哨兵二号数据，同时，红树林分布地区多云雨天气，对光学遥感图像分割和分类有较大影响。因此在源数据上首先实现了Sentinel-1的VV极化和VH极化图像与Sentinel-2融合。</p>"
     "   <p>      本网站公布了2019年和2022年新盈港以及2019年花场和2023年花场湾基于上述三种方法得到的红树林分类结果图、对应的分类TIFF影像下载和相应全部红树林的人工勾勒样本shp文件下载（数据集参照GMV-2019）。欢迎广大读者讨论交流。</p>"
    "  </div>"
    "</div>"
 
    "<script>"
    "  const contentData = {"
    "    '2019 新盈港': {"
    "      description: '根据无人机拍摄发现儋州市光村镇位于生态保护红线内21.9亩红树林被陆续砍伐.寻找多年遥感影像数据发现2019年仍然未被破环，对数据进行下载分析。从左至右依次为SVM分类结果红树林矢量原图像叠加、面向对象分类结果红树林矢量原图像叠加、U-net分类结果红树林矢量原图像叠加。',"
    "      images: ['1901001.jpg', '1901002.jpg', '1901003.jpg'],"
    "      shpLink: '201901.zip'"

    "    },"
    "    '2019 花场湾': {"
    "      description: '2019年8月，澄迈县肆意围填海、破坏红树林作为中央生态环境保护督察典型案例被生态环境部在全国进行通报。面对压力，澄迈县以实事求是、照单全收的态度和痛定思痛、知耻后勇的勇气抓整改、抓落实，在不到一年的时间里，严格按照中央第三生态环境保护督察组的要求，完成红树湾项目内9.69亩枯死红树林和红树林保护区92亩被填埋鱼塘等区域的修复工作，让遭到破坏的红树林再次恢复郁郁葱葱，努力把反面典型变为自我革命、纠正错误、改正错误的正面典型，成为直面问题、主动践行“绿水青山就是金山银山”理念的范例。从左至右依次为SVM分类结果红树林矢量原图像叠加、面向对象分类结果红树林矢量原图像叠加、U-net分类结果红树林矢量原图像叠加。',"
    "      images: ['1902001.jpg', '1902002.jpg', '1902003.jpg'],"
    "      shpLink: '201902.zip'"
    "    },"
    "    '2022 新盈港': {"
    "      description: '2022 新盈港红树林被破环，对数据进行下载分析。从左至右依次为SVM分类结果红树林矢量原图像叠加、面向对象分类结果红树林矢量原图像叠加、U-net分类结果红树林矢量原图像叠加。',"
    "      images: ['2201001.jpg', '2201002.jpg', '2201003.jpg'],"
    "      shpLink: '202201.zip'"
    "    },"
    "    '2023 花场湾': {"
    "      description: '2023 花场湾红树林状况有所好转。对数据进行下载分析。从左至右依次为SVM分类结果红树林矢量原图像叠加、面向对象分类结果红树林矢量原图像叠加、U-net分类结果红树林矢量原图像叠加。',"
    "      images: ['2302001.jpg', '2302002.jpg', '2302003.jpg'],"
    "      shpLink: '202302.zip'"
    "    }"
    "  };"
    ""
    "  function loadContent(title) {"
    "    const data = contentData[title];"
    "    if (data) {"
    "      let imagesHtml = data.images.map(img => `<img src=\"${img}\" alt=\"${title} Image\">`).join('');"
    #"      const tiffHtml = data.tiffLink ? `<a href=\"${data.tiffLink}\" class='download-link' download>下载TIFF影像</a>` : '';"
   
    "      document.getElementById('content-area').innerHTML = `"
    "        <h2>${title}</h2>"
    "        <p>${data.description}</p>"
    "        <div class='image-gallery'>${imagesHtml}</div>"
    
    "        <a href=\"${data.shpLink}\" class='download-link' download>shp文件与tiff影像下载</a>"
    #"        ${tiffHtml}"
    "      `;"
    "    } else {"
    "      document.getElementById('content-area').innerHTML = '<p>内容加载失败。</p>';"
    "    }"
    "  }"
    "</script>"
    "</body>"
    "</html>"

]

# 写入HTML文件
with open("index.html", "w", encoding="utf-8") as outfile:
    for line in code:
        outfile.write(line + '\n')

# 打开HTML文件
import webbrowser

webbrowser.open("index.html")

