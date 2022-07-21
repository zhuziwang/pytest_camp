#基于pytest的关键字驱动自动化测试
##*需要python3 pytest 关键字获取为pymysql*
###目录介绍：
- commmon
- ddt
- image
- lib
- models
- reprot
- Web
- pytest.ini
- requirements.txt
- runner.py 

1. common：   
   1.1 base.log：*记录log日志*    
   1.2 cls：*公共方法* 
   
2. ddt：  
   2.1 app_login_excel.py：*app用例执行*  
   2.2 test_sql_demo.py：*web用例执行*    
   2.3 params.py：*用例执行获取数据*   
   
3. image：   
   3.1 mysql_screenshot：   
    - phone_img_path：*app_public中matching方法中手动截图的第一张*   
    - phone_img_slider_path：*app_public中matching方法中手动截图的第二张*   
   
   3.2 OCR：
    - phone_img_path：*app_public中matching方法中手动截图的第一张*   
    - phone_img_slider_path：*app_public中matching方法中手动截图的第二张*   
    - word_ocr：需要ocr文字识别的图片   
   
   3.3 opencv： 
      
    - get_screenshot_as_file：web端窗口截图
    - web_img_bg_path：web端滑动验证码，背景图片
    - web_img_slider_path：web端滑动验证码，滑块图片  
   
   3.4 picture：allure结果浏览器窗口截图   
   
   3.5 tesseract_image： 需要ocr文字识别的图片      
   
4. lib：      
   4.1 appcase：存放app测试用例（excel格式文件，已废弃）      
   4.2 case：存放web测试用例（excel格式文件，已废弃）      
   
5. model：   
   5.1 app_model_excel.py：从excel中取出app用例（已废弃）   
   5.2 model_excel：  从excel中取出web用例（已废弃）  
   5.3 model_sql： 取出的数据格式转换为list，以数据库为存储关键字与用例的地址  
   5.4 model_sql_app：连接数据库    
   5.5 sql：连接数据库  
   
6. report：存放allure—report中json数据临时存放地址 
   
7. web：  
   7.1 appkeys.py： app下非公共方法  
   7.2 em.py：  发送邮件  
   7.3 request.py：  接口方法   
   7.4 tesseract.py： tesseract本地文字识别OCR   
   7.5 webkeys.py： web下非公共方法     
   
8. pytest.ini：pytest框架配置文件 

9. runner.py：执行文件 
   
10. requirements.txt：需要安装的其他库
