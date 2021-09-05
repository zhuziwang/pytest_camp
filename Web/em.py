import smtplib
from email.mime.text import MIMEText
from email.header import Header
import os
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart

def youjian():
    sender = '2693601181@qq.com'  # 发送使用的邮箱
    receivers = ['490644367@qq.com']  # 收件人，可以是多个任意邮箱

    mail_msg = """
    <p>Python 邮件发送测试...</p>
    <p><a href="http://www.baidu.com">测试结果报告</a></p>
    """
    # 邮件正文
    message = MIMEText(mail_msg, 'html', 'utf-8')
    message['From'] = Header("朱秭旺", 'utf-8')  # 发送者
    message['To'] = Header("马鹏鹏", 'utf-8')  # 接收者
    #邮件标题
    subject = '测试报告！标题'
    message['Subject'] = Header(subject, 'utf-8')




    # # 构造附件1，传送当前目录下的 hello.html 文件
    # att1 = MIMEText(open('hello.html','r').read(), 'base64', 'utf-8')
    # att1["Content-Type"] = 'application/octet-stream'
    # # 这里的filename可以任意写，写什么名字，邮件中显示什么名字
    # att1["Content-Disposition"] = 'attachment; filename="测试报告"'
    # message.attach(att1)

    #message['Subject'] = Header(subject, 'utf-8')

    try:
        smtp = smtplib.SMTP_SSL('smtp.qq.com')
          # 登陆qq邮箱，密码需要使用的是授权码
        smtp.login(sender, 'rsqboylrrlizdeaf')
        smtp.sendmail(sender, receivers, message.as_string())
        smtp.quit()
        print("邮件发送成功")
    except smtplib.SMTPException:
        print("Error: 无法发送邮件")





















def youjian111():
    smtpserver = 'smtp.qq.com'
    port = 0
    sender = '100179039@qq.com'
    password = 'w981026..'
    receicer = ['904956147@qq.com' ]

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

