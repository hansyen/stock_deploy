
class StatusTranslate():
    def userverify_bill_status_translation(self):
        if self == False:
            status = 'Unverify'
            self = status
            return self
        if self == True:
            status = 'Verify'
            self = status
            return self

    def userverify_email_status_translation(self):
        if self == False:
            status = 'Unverify'
            self = status
            return self
        if self == True:
            status = 'Verify'
            self = status
            return self

    def userverify_phone_status_translation(self):
        if self == False:
            status = 'Unverify'
            self = status
            return self
        if self == True:
            status = 'Verify'
            self = status
            return self

    def userverify_id_card_status_translation(self):
        if self == False:
            status = 'Unverify'
            self = status
            return self
        if self == True:
            status = 'Verify'
            self = status
            return self

    # 訂單狀態 0:create, 1:pedding, 2:success, 3:fail
    def billing_status_translation(self):
        if self == 0:
            status = 'Create'
            self = status
            return self
        if self == 1:
            status = 'Pending'
            self = status
            return self
        if self == 2:
            status = 'Success'
            self = status
            return self
        if self == 3:
            status = 'Fail'
            self = status
            return self

    def walletlog_status_translation(self):
        if self == 0:
            status = 'Synchronize complete'
            self = status
            return self
        if self == 200:
            status = 'Wait Synchronize'
            self = status
            return self

    def walletlog_log_type_translation(self):
        if self == 100:
            log_type = 'Deposit'
            self = log_type
            return self
        if self == 200:
            log_type = 'Withdraw'
            self = log_type
            return self
        if self == 250:
            log_type = 'Transfer'
            self = log_type
            return self
        if self == 300:
            log_type = 'Commission'
            self = log_type
            return self
        if self == 500:
            log_type = 'Handling Fee'
            self = log_type
            return self
        if self == 600:
            log_type = 'Profit'
            self = log_type
            return self
        if self == 700:
            log_type = 'Return Guarantee Deposit'
            self = log_type
            return self
        if self == 400:
            log_type = 'Kick Back Fee'
            self = log_type
            return self
        if self == 900:
            log_type = 'Vote Deduct'
            self = log_type
            return self
        if self == 999:
            log_type = 'Cancel'
            self = log_type
            return self

    def withdraw_status_translation(self):
        if self == 0:
            status = 'Success'
            self = status
            return self
        if self == 1:
            status = 'Create'
            self = status
            return self
        if self == 2:
            status = 'Pending'
            self = status
            return self
        if self == 3:
            status = 'Cancel'
            self = status
            return self
        if self == 4:
            status = 'In Process'
            self = status
            return self
        if self == 5:
            status = 'Fail'
            self = status
            return self












