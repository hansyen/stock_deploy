from builtins import dict, int

from flask import Blueprint, request, flash, redirect, url_for, render_template

from translate import StatusTranslate
from walletlog.forms import WalletLogSearchForm
from models import WalletLog, Role

walletlog = Blueprint('walletlog', __name__)

@walletlog.context_processor  # 將class丟到前端
def inject_role():
    return dict(Role=Role)

@walletlog.route("/walletlogview", methods=['GET', 'POST'])
def wallet_log_view():
    search = WalletLogSearchForm(request.form)
    results = []
    search_string = search.data['search']
    page = request.args.get('page', 1, type=int)
    if search_string:
        if search.data['select'] == 'uid':   #search
            results = WalletLog.query.filter(WalletLog.uid == search_string) \
                .order_by(WalletLog.uid).paginate(page=page, per_page=20)

        elif search.data['select'] == 'tid':
            results = WalletLog.query.filter(WalletLog.tid == search_string) \
                .order_by(WalletLog.uid).paginate(page=page, per_page=20)

        elif search.data['select'] == 'log_type':
            results = WalletLog.query.filter(WalletLog.log_type == search_string) \
                .order_by(WalletLog.uid).paginate(page=page, per_page=20)

        elif search.data['select'] == 'status':
            results = WalletLog.query.filter(WalletLog.status == search_string) \
                .order_by(WalletLog.uid).paginate(page=page, per_page=20)

    if search.data['search'] == '':
        results = WalletLog.query.order_by(WalletLog.uid).paginate(page=page, per_page=20)

    if not results:
        flash('No results found!')
        return redirect(url_for('wallet_log_view'))
    else:
        for result in results.items:
            status = result.status  # translate
            result.status = StatusTranslate.walletlog_status_translation(status)
            log_type = result.log_type
            result.log_type = StatusTranslate.walletlog_log_type_translation(log_type)
        return render_template('walletlogview.html',
                               page=page,
                               form=search,
                               results=results)

@walletlog.route("/walletlog/detail")
def wallet_log_detail():
    tid = request.args.get('tid', None, type=int)
    results = WalletLog.query.filter_by(tid=tid).first()
    status = results.status  # translate
    results.status = StatusTranslate.walletlog_status_translation(status)
    log_type = results.log_type
    results.log_type = StatusTranslate.walletlog_log_type_translation(log_type)
    return render_template('walletlog_detail.html', user_info=results)