import pytz
from datetime import datetime

from flask_login import current_user


class TraceLog():
    def userverify_before_log(self):
        localtime = pytz.timezone('Asia/Taipei')  # 調整時區
        localtime_now = datetime.now(localtime)
        fmt = '%Y-%m-%d %H'  # 設定時間格式
        localtime_hour = datetime.now(localtime)
        file = open('auth_server/static/log/userverifylog_' + str(localtime_hour.strftime(fmt)) + '點' + '.txt', 'a')  # 以小時為單位存檔
        file.write('Table Name: UserVerify' + '\n')
        file.write('User ID: ' + str(self.uid) + '\n')
        file.write('User: ' + str(current_user.username) + '\n')
        file.write('ID_card status before update(0=Unverify, 1=Verify): ' + str(self.id_card) + '\n')
        file.write('Bill status before update(0=Unverify, 1=Verify): ' + str(self.bill) + '\n')
        file.write('E-mail status before update(0=Unverify, 1=Verify): ' + str(self.email) + '\n')
        file.write('Phone status before update(0=Unverify, 1=Verify): ' + str(self.phone) + '\n')
        file.write('Update Time: ' + str(localtime_now) + '\n')
        file.close()

    def userverify_after_log(self):
        localtime = pytz.timezone('Asia/Taipei')  # 調整時區
        localtime_now = datetime.now(localtime)
        fmt = '%Y-%m-%d %H'  # 設定時間格式
        localtime_hour = datetime.now(localtime)
        file = open('auth_server/static/log/userverifylog_' + str(localtime_hour.strftime(fmt)) + '點' + '.txt', 'a')  # 以小時為單位存檔
        file.write('Table Name: UserVerify' + '\n')
        file.write('User ID: ' + str(self.uid) + '\n')
        file.write('User: ' + str(current_user.username) + '\n')
        file.write('ID_card status after update(0=Unverify, 1=Verify): ' + str(self.id_card) + '\n')
        file.write('Bill status after update(0=Unverify, 1=Verify): ' + str(self.bill) + '\n')
        file.write('E-mail status after update(0=Unverify, 1=Verify): ' + str(self.email) + '\n')
        file.write('Phone status after update(0=Unverify, 1=Verify): ' + str(self.phone) + '\n')
        file.write('Update Time: ' + str(localtime_now) + '\n')
        file.close()

    def withdraw_before_log(self):
        localtime = pytz.timezone('Asia/Taipei')  # 調整時區
        localtime_now = datetime.now(localtime)
        fmt = '%Y-%m-%d %H'  # 設定時間格式
        localtime_hour = datetime.now(localtime)
        file = open('auth_server/static/log/withdrawticketlog_' + str(localtime_hour.strftime(fmt)) + '點' + '.txt', 'a')  # 以小時為單位存檔
        file.write('Table Name: WithDrawTicket' + '\n')
        file.write('Ticket NO.: ' + str(self.td) + '\n')
        file.write('User: ' + str(current_user.username) + '\n')
        file.write('Ticket status before update(0:Success, 1:Create, 2:Pending, 3:Cancel, 4:In Process, 5:Fail): ' + str(self.status) + '\n')
        file.write('Update Time: ' + str(localtime_now) + '\n')
        file.close()

    def withdraw_after_log(self):
        localtime = pytz.timezone('Asia/Taipei')  # 調整時區
        localtime_now = datetime.now(localtime)
        fmt = '%Y-%m-%d %H'  # 設定時間格式
        localtime_hour = datetime.now(localtime)
        file = open('auth_server/static/log/withdrawticketlog_' + str(localtime_hour.strftime(fmt)) + '點' + '.txt', 'a')  # 以小時為單位存檔
        file.write('Table Name: WithDrawTicket' + '\n')
        file.write('Ticket NO.: ' + str(self.td) + '\n')
        file.write('User: ' + str(current_user.username) + '\n')
        file.write('Ticket status after update(0:Success, 1:Create, 2:Pending, 3:Cancel, 4:In Process, 5:Fail): ' + str(self.status) + '\n')
        file.write('Update Time: ' + str(localtime_now) + '\n')
        file.close()