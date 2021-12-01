#coding=utf-8
import smtplib
from email.mime.text import MIMEText
from email.header import Header
from email.mime.image import MIMEImage  # 图片类型邮件
import os
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart  # 创建附件类型
from Web.webkeys import WebKey
def youjian():
    W=WebKey()
    picture_name=W.picture()
    str_time=W.str_time()

    sender = '***@qq.com'  # 发送使用的邮箱
    receivers = ['*****@qq.com']  # 收件人，可以是多个任意邮箱
    # < p > Python邮件发送测试... < / p >
    mail_msg = """
    <p><a href="http://ip地址/jenkins/job/SVN/allure/">测试结果报告</a></p>
    <img src="cid:image1" alt="image1">
    """

    # 邮件正文
    message = MIMEText(mail_msg, 'html', 'utf-8')
    msgRoot = MIMEMultipart('related')  # 邮件类型，如果要加图片等附件，就得是这个
    message['From'] = Header("朱**", 'utf-8')  # 发送者
    message['To'] = Header("组长-**", 'utf-8')  # 接收者
    #邮件标题
    subject = ' (%s） 自动化测试结果'%str_time
    msgRoot['Subject'] = Header(subject, 'utf-8')
    msgRoot.attach(message)
    # 添加图片附件
    file_name= 'C:\\Users\\Administrator\\PycharmProjects\\kouyu100\\image\\picture\\%s'%picture_name
    fp = open(file_name, 'rb')
    msgImage = MIMEImage(fp.read())
    fp.close()
    msgImage.add_header('Content-ID', 'image1')  # 这个id用于上面html获取图片
    msgRoot.attach(msgImage)



    try:
        smtp = smtplib.SMTP_SSL('smtp.qq.com')
          # 登陆qq邮箱，密码需要使用的是授权码
        smtp.login(sender, 'rsqboylrrlizdeaf')
        smtp.sendmail(sender, receivers, msgRoot.as_string())
        smtp.quit()
        print("邮件发送成功")
    except smtplib.SMTPException:
        print("Error: 无法发送邮件")



def youjian111():
    smtpserver = 'smtp.qq.com'
    port = 0
    sender = '**@qq.com'
    password = '**'
    receicer = ['**@qq.com' ]

    # ----------------编辑邮件内容----------------
    subject = '发送邮件测试'
    body = '<p>发送邮件测试Test<p>'
    msg = MIMEText(body, 'html', 'UTF-8')
    msg['from'] = sender
    msg['to'] = ';'.join(receicer)
    msg['subject'] = subject

    # 文字部分
    part = MIMEText('TEST!!!')
    msg.attach(part)
    # 附件部分
    # # ---xlsx类型附件---
    # part = MIMEApplication(open('D:\\test.xlsx', 'rb').read())
    # part.add_header('Content-Disposition', 'attachment', filename="test.xlsx")
    # msg.attach(part)
    # # jpg类型附件（png类型和jpg一样）
    # part = MIMEApplication(open('D:\\test.jpg', 'rb').read())
    # part.add_header('Content-Disposition', 'attachment', filename="test.jpg")
    # msg.attach(part)
    # # pdf类型附件
    # part = MIMEApplication(open('D:\\test.pdf', 'rb').read())
    # part.add_header('Content-Disposition', 'attachment', filename="test.pdf")
    # msg.attach(part)
    # # mp3类型附件
    # part = MIMEApplication(open('D:\\test.mp3', 'rb').read())
    # part.add_header('Content-Disposition', 'attachment', filename="test.mp3")
    # msg.attach(part)
    # html类型
    part = MIMEText('<html><h1>test!</h1></html>', 'html', 'utf-8')
    msg.attach(part)

    # ------------------发送邮件-----------------
    try:
        smtp = smtplib.SMTP()
        smtp.connect(smtpserver)
        smtp.login(sender, password)
    except:
        smtp = smtplib.SMTP_SSL(smtpserver, port)
        smtp.login(sender, password)
    smtp.sendmail(sender, receicer, msg.as_string())
    smtp.quit()

if __name__ == '__main__':
    you=youjian()