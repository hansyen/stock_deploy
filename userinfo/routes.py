from builtins import dict, int

from flask import Blueprint, request, flash, redirect, url_for, render_template

from models import UserInfo, Role
from userinfo.forms import UserInfoSearchForm

userinfo = Blueprint('userinfo', __name__)

@userinfo.context_processor  # 將class丟到前端
def inject_role():
    return dict(Role=Role)

@userinfo.route("/userinfoview", methods=['GET', 'POST'])
def userinfo_view():
    search = UserInfoSearchForm(request.form)
    results = []
    search_string = search.data['search']
    page = request.args.get('page', 1, type=int)

    if search_string:
        if search.data['select'] == 'uid':    #search
            results = UserInfo.query.filter(UserInfo.uid == search_string) \
                .order_by(UserInfo.uid).paginate(page=page, per_page=20)

        elif search.data['select'] == 'country':
            results = UserInfo.query.filter(UserInfo.country == search_string) \
                .order_by(UserInfo.uid).paginate(page=page, per_page=20)

        elif search.data['select'] == 'nationality':
            results = UserInfo.query.filter(UserInfo.nationality == search_string) \
                .order_by(UserInfo.uid).paginate(page=page, per_page=20)

        elif search.data['select'] == 'phone':
            results = UserInfo.query.filter(UserInfo.phone == search_string) \
                .order_by(UserInfo.uid).paginate(page=page, per_page=20)

        elif search.data['select'] == 'family_name':
            results = UserInfo.query.filter(UserInfo.family_name == search_string) \
                .order_by(UserInfo.uid).paginate(page=page, per_page=20)

        elif search.data['select'] == 'first_name':
            results = UserInfo.query.filter(UserInfo.first_name == search_string) \
                .order_by(UserInfo.uid).paginate(page=page, per_page=20)

        elif search.data['select'] == 'sex':
            results = UserInfo.query.filter(UserInfo.sex == search_string) \
                .order_by(UserInfo.uid).paginate(page=page, per_page=20)

    if search.data['search'] == '':
        results = UserInfo.query.order_by(UserInfo.uid).paginate(page=page, per_page=20)

    if not results:
        flash('No results found!')
        return redirect(url_for('userinfo.userinfo_view'))
    else:
        return render_template('userinfoview.html',
                               page=page,
                               form=search,
                               results=results)

@userinfo.route("/userinfo/detail")
def userinfo_detail():
    uid = request.args.get('uid', None, type=int)
    results = UserInfo.query.filter_by(uid=uid).first()
    return render_template('userinfo_detail.html', user_info=results)