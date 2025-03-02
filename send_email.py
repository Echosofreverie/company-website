import smtplib
from email.mime.text import MIMEText



def send_message(message,user_email):
    qq_email = "xxxxxxx@qq.com"#使用你自己的qq邮箱
    auth_code = "xxxxxxxxxxxxxx"#使用你自己的qq邮箱的授权码，登录qq邮箱，设置->账户->开启SMTP服务->获取授权码
    smtp_server = "smtp.qq.com"
    smtp_port = 465
    msg = MIMEText(message)
    msg['Subject'] = f"New Email from {user_email}"
    msg['From'] = qq_email
    msg['To'] = "xxxxx@xxx.com"#目标邮箱
    try:
        # 创建SSL加密连接
        with smtplib.SMTP_SSL(smtp_server, smtp_port) as server:
            server.login(qq_email, auth_code)
            server.send_message(msg)
            print("邮件发送成功！🎉")
    except Exception as e:
        print("邮件发送失败！", e)


#send_message()
