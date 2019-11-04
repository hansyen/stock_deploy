from builtins import type, len, range, int, list
from io import open

import requests
import pandas as pd


from flask import Blueprint, request, flash, redirect, url_for, render_template
from flask_login import login_user, logout_user, current_user, login_required
from bs4 import BeautifulSoup


classstock = Blueprint('classstock', __name__)

# @classstock.context_processor  # 將class丟到前端
# def inject_role():
#     return dict(Role=Role)

@classstock.route("/class_stock")
def class_stock():
    if current_user.is_authenticated:
        return render_template('classstock/classstock.html')
    else:
        flash('You need login!', 'warning')
        return redirect(url_for('main.home'))

@classstock.route("/classstock_a", methods=['GET', 'POST'])
def classstock_a():
    if current_user.is_authenticated:
        src = "https://tw.stock.yahoo.com/s/list.php?c=%A4%F4%AAd&rr=0.60494800%201544016777"
        html = requests.get(src)
        html.encoding = "cp950"

        pdtest = pd.read_html("https://tw.stock.yahoo.com/s/list.php?c=%A4%F4%AAd&rr=0.60494800%201544016777" )
        sp = BeautifulSoup(html.text, "html.parser")

        data1 = sp.find_all("table")

        # datatest = pdtest.find_all("table")
        a = data1[4].text
        # a = datatest[4].table
        # result_list = []
        # for result in a:
        #     result_list.append(result)

        a = a.replace("\n \n\n", "@")
        a = a.replace("\n\n\n\n", "@")
        a = a.replace("\n\n", "\n")
        a = a.replace("\n", ",")
        a = a.replace("@", "\n")
        list_a = a.split("\n")
    else:
        flash('You need login!', 'warning')
        return redirect(url_for('main.home'))

    return render_template('classstock/classstock_a.html', a=a, data1=data1, pdtest=pdtest, list_a=list_a)

@classstock.route("/classstock_a_write", methods=['GET', 'POST'])
def classstock_a_write():
    src = "https://tw.stock.yahoo.com/s/list.php?c=%A4%F4%AAd&rr=0.60494800%201544016777"
    html = requests.get(src)
    html.encoding = "cp950"

    sp = BeautifulSoup(html.text, "html.parser")

    data1 = sp.find_all("table")
    # print('data1[5].text======', data1[5].text)
    a = data1[4].text
    # a = datatest[4].table
    # result_list = []
    # for result in a:
    #     result_list.append(result)

    a = a.replace("\n \n\n", "@")
    a = a.replace("\n\n\n\n", "@")
    a = a.replace("\n\n", "\n")
    a = a.replace("\n", ",")
    a = a.replace("@", "\n")
    # print(pdtest)
    file = open('class a.txt', 'a')
    file.write(a)
    file.close()
    return redirect(url_for('classstock.classstock_a'))


@classstock.route("/classstock_b", methods=['GET', 'POST'])
def classstock_b():
    if current_user.is_authenticated:
        src = "https://tw.stock.yahoo.com/s/list.php?c=%AD%B9%AB%7E&rr=0.35528600%201535770407"
        html = requests.get(src)
        html.encoding = "cp950"

        sp = BeautifulSoup(html.text, "html.parser")

        data2 = sp.find_all("table")

        b = data2[4].text
        b = b.replace("\n \n\n", "@")
        b = b.replace("\n\n\n\n", "@")
        b = b.replace("\n\n", "\n")
        b = b.replace("\n", ",")
        b = b.replace("@", "\n")
        list_b = b.split("\n")
    else:
        flash('You need login!', 'warning')
        return redirect(url_for('main.home'))
    return render_template('classstock/classstock_b.html', list_b=list_b)

@classstock.route("/classstock_c", methods=['GET', 'POST'])
def classstock_c():
    if current_user.is_authenticated:
        src = "https://tw.stock.yahoo.com/s/list.php?c=%B6%EC%BD%A6&rr=0.35528700%201535770407"
        html = requests.get(src)
        html.encoding = "cp950"

        sp = BeautifulSoup(html.text, "html.parser")

        data3 = sp.find_all("table")

        c = data3[4].text
        c = c.replace("\n \n\n", "@")
        c = c.replace("\n\n\n\n", "@")
        c = c.replace("\n\n", "\n")
        c = c.replace("\n", ",")
        c = c.replace("@", "\n")
        list_c = c.split("\n")
    else:
        flash('You need login!', 'warning')
        return redirect(url_for('main.home'))
    return render_template('classstock/classstock_c.html', list_c=list_c)

@classstock.route("/classstock_d", methods=['GET', 'POST'])
def classstock_d():
    if current_user.is_authenticated:
        src = "https://tw.stock.yahoo.com/s/list.php?c=%AF%BC%C2%B4&rr=0.35528900%201535770407"
        html = requests.get(src)
        html.encoding = "cp950"

        sp = BeautifulSoup(html.text, "html.parser")

        data4 = sp.find_all("table")

        d = data4[4].text
        d = d.replace("\n \n\n", "@")
        d = d.replace("\n\n\n\n", "@")
        d = d.replace("\n\n", "\n")
        d = d.replace("\n", ",")
        d = d.replace("@", "\n")
        list_d = d.split("\n")
    else:
        flash('You need login!', 'warning')
        return redirect(url_for('main.home'))
    return render_template('classstock/classstock_d.html', list_d=list_d)

@classstock.route("/classstock_e", methods=['GET', 'POST'])
def classstock_e():
    if current_user.is_authenticated:
        src = "https://tw.stock.yahoo.com/s/list.php?c=%B9q%BE%F7&rr=0.35529000%201535770407"
        html = requests.get(src)
        html.encoding = "cp950"

        sp = BeautifulSoup(html.text, "html.parser")

        data5 = sp.find_all("table")

        e = data5[4].text
        e = e.replace("\n \n\n", "@")
        e = e.replace("\n\n\n\n", "@")
        e = e.replace("\n\n", "\n")
        e = e.replace("\n", ",")
        e = e.replace("@", "\n")
        list_e = e.split("\n")
    else:
        flash('You need login!', 'warning')
        return redirect(url_for('main.home'))
    return render_template('classstock/classstock_e.html', list_e=list_e)

@classstock.route("/classstock_f", methods=['GET', 'POST'])
def classstock_f():
    if current_user.is_authenticated:
        src = "https://tw.stock.yahoo.com/s/list.php?c=%B9q%BE%B9%B9q%C6l&rr=0.35529200%201535770407"
        html = requests.get(src)
        html.encoding = "cp950"

        sp = BeautifulSoup(html.text, "html.parser")

        data6 = sp.find_all("table")

        f = data6[4].text
        f = f.replace("\n \n\n", "@")
        f = f.replace("\n\n\n\n", "@")
        f = f.replace("\n\n", "\n")
        f = f.replace("\n", ",")
        f = f.replace("@", "\n")
        list_f = f.split("\n")
    else:
        flash('You need login!', 'warning')
        return redirect(url_for('main.home'))
    return render_template('classstock/classstock_f.html', list_f=list_f)

@classstock.route("/classstock_g", methods=['GET', 'POST'])
def classstock_g():
    if current_user.is_authenticated:
        src = "https://tw.stock.yahoo.com/s/list.php?c=%A4%C6%BE%C7&rr=0.35529300%201535770407"
        html = requests.get(src)
        html.encoding = "cp950"

        sp = BeautifulSoup(html.text, "html.parser")

        data7 = sp.find_all("table")

        g = data7[4].text
        g = g.replace("\n \n\n", "@")
        g = g.replace("\n\n\n\n", "@")
        g = g.replace("\n\n", "\n")
        g = g.replace("\n", ",")
        g = g.replace("@", "\n")
        list_g = g.split("\n")
    else:
        flash('You need login!', 'warning')
        return redirect(url_for('main.home'))
    return render_template('classstock/classstock_g.html', list_g=list_g)

@classstock.route("/classstock_h", methods=['GET', 'POST'])
def classstock_h():
    if current_user.is_authenticated:
        src = "https://tw.stock.yahoo.com/s/list.php?c=%A5%CD%A7%DE%C2%E5%C0%F8&rr=0.35529400%201535770407"
        html = requests.get(src)
        html.encoding = "cp950"

        sp = BeautifulSoup(html.text, "html.parser")

        data8 = sp.find_all("table")

        h = data8[4].text
        h = h.replace("\n \n\n", "@")
        h = h.replace("\n\n\n\n", "@")
        h = h.replace("\n\n", "\n")
        h = h.replace("\n", ",")
        h = h.replace("@", "\n")
        list_h = h.split("\n")
    else:
        flash('You need login!', 'warning')
        return redirect(url_for('main.home'))
    return render_template('classstock/classstock_h.html', list_h=list_h)

@classstock.route("/classstock_i", methods=['GET', 'POST'])
def classstock_i():
    if current_user.is_authenticated:
        src = "https://tw.stock.yahoo.com/s/list.php?c=%AC%C1%BC%FE&rr=0.35529600%201535770407"
        html = requests.get(src)
        html.encoding = "cp950"

        sp = BeautifulSoup(html.text, "html.parser")

        data9 = sp.find_all("table")

        i = data9[4].text
        i = i.replace("\n \n\n", "@")
        i = i.replace("\n\n\n\n", "@")
        i = i.replace("\n\n", "\n")
        i = i.replace("\n", ",")
        i = i.replace("@", "\n")
        list_i = i.split("\n")
    else:
        flash('You need login!', 'warning')
        return redirect(url_for('main.home'))
    return render_template('classstock/classstock_i.html', list_i=list_i)

@classstock.route("/classstock_j", methods=['GET', 'POST'])
def classstock_j():
    if current_user.is_authenticated:
        src = "https://tw.stock.yahoo.com/s/list.php?c=%B3y%AF%C8&rr=0.35529700%201535770407"
        html = requests.get(src)
        html.encoding = "cp950"

        sp = BeautifulSoup(html.text, "html.parser")

        data10 = sp.find_all("table")

        j = data10[4].text
        j = j.replace("\n \n\n", "@")
        j = j.replace("\n\n\n\n", "@")
        j = j.replace("\n\n", "\n")
        j = j.replace("\n", ",")
        j = j.replace("@", "\n")
        list_j = j.split("\n")
    else:
        flash('You need login!', 'warning')
        return redirect(url_for('main.home'))
    return render_template('classstock/classstock_j.html', list_j=list_j)

@classstock.route("/classstock_k", methods=['GET', 'POST'])
def classstock_k():
    if current_user.is_authenticated:
        src = "https://tw.stock.yahoo.com/s/list.php?c=%BF%FB%C5K&rr=0.35529800%201535770407"
        html = requests.get(src)
        html.encoding = "cp950"

        sp = BeautifulSoup(html.text, "html.parser")

        data11 = sp.find_all("table")

        k = data11[4].text
        k = k.replace("\n \n\n", "@")
        k = k.replace("\n\n\n\n", "@")
        k = k.replace("\n\n", "\n")
        k = k.replace("\n", ",")
        k = k.replace("@", "\n")
        list_k = k.split("\n")
    else:
        flash('You need login!', 'warning')
        return redirect(url_for('main.home'))
    return render_template('classstock/classstock_k.html', list_k=list_k)

@classstock.route("/classstock_l", methods=['GET', 'POST'])
def classstock_l():
    if current_user.is_authenticated:
        src = "https://tw.stock.yahoo.com/s/list.php?c=%BE%F3%BD%A6&rr=0.35530000%201535770407"
        html = requests.get(src)
        html.encoding = "cp950"

        sp = BeautifulSoup(html.text, "html.parser")

        data12 = sp.find_all("table")

        l = data12[4].text
        l = l.replace("\n \n\n", "@")
        l = l.replace("\n\n\n\n", "@")
        l = l.replace("\n\n", "\n")
        l = l.replace("\n", ",")
        l = l.replace("@", "\n")
        list_l = l.split("\n")
    else:
        flash('You need login!', 'warning')
        return redirect(url_for('main.home'))
    return render_template('classstock/classstock_l.html', list_l=list_l)

@classstock.route("/classstock_m", methods=['GET', 'POST'])
def classstock_m():
    if current_user.is_authenticated:
        src = "https://tw.stock.yahoo.com/s/list.php?c=%A8T%A8%AE&rr=0.35530100%201535770407"
        html = requests.get(src)
        html.encoding = "cp950"

        sp = BeautifulSoup(html.text, "html.parser")

        data13 = sp.find_all("table")

        m = data13[4].text
        m = m.replace("\n \n\n", "@")
        m = m.replace("\n\n\n\n", "@")
        m = m.replace("\n\n", "\n")
        m = m.replace("\n", ",")
        m = m.replace("@", "\n")
        list_m = m.split("\n")
    else:
        flash('You need login!', 'warning')
        return redirect(url_for('main.home'))
    return render_template('classstock/classstock_m.html', list_m=list_m)

@classstock.route("/classstock_n", methods=['GET', 'POST'])
def classstock_n():
    if current_user.is_authenticated:
        src = "https://tw.stock.yahoo.com/s/list.php?c=%A5b%BE%C9%C5%E9&rr=0.35530200%201535770407"
        html = requests.get(src)
        html.encoding = "cp950"

        sp = BeautifulSoup(html.text, "html.parser")

        data14 = sp.find_all("table")

        n = data14[4].text
        n = n.replace("\n \n\n", "@")
        n = n.replace("\n\n\n\n", "@")
        n = n.replace("\n\n", "\n")
        n = n.replace("\n", ",")
        n = n.replace("@", "\n")
        list_n = n.split("\n")
    else:
        flash('You need login!', 'warning')
        return redirect(url_for('main.home'))
    return render_template('classstock/classstock_n.html', list_n=list_n)

@classstock.route("/classstock_o", methods=['GET', 'POST'])
def classstock_o():
    if current_user.is_authenticated:
        src = "https://tw.stock.yahoo.com/s/list.php?c=%B9q%B8%A3%B6g%C3%E4&rr=0.35530300%201535770407"
        html = requests.get(src)
        html.encoding = "cp950"

        sp = BeautifulSoup(html.text, "html.parser")

        data15 = sp.find_all("table")

        o = data15[4].text
        o = o.replace("\n \n\n", "@")
        o = o.replace("\n\n\n\n", "@")
        o = o.replace("\n\n", "\n")
        o = o.replace("\n", ",")
        o = o.replace("@", "\n")
        list_o = o.split("\n")
    else:
        flash('You need login!', 'warning')
        return redirect(url_for('main.home'))
    return render_template('classstock/classstock_o.html', list_o=list_o)

@classstock.route("/classstock_p", methods=['GET', 'POST'])
def classstock_p():
    if current_user.is_authenticated:
        src = "https://tw.stock.yahoo.com/s/list.php?c=%A5%FA%B9q&rr=0.35530500%201535770407"
        html = requests.get(src)
        html.encoding = "cp950"

        sp = BeautifulSoup(html.text, "html.parser")

        data16 = sp.find_all("table")

        p = data16[4].text
        p = p.replace("\n \n\n", "@")
        p = p.replace("\n\n\n\n", "@")
        p = p.replace("\n\n", "\n")
        p = p.replace("\n", ",")
        p = p.replace("@", "\n")
        list_p = p.split("\n")
    else:
        flash('You need login!', 'warning')
        return redirect(url_for('main.home'))
    return render_template('classstock/classstock_p.html', list_p=list_p)

@classstock.route("/classstock_q", methods=['GET', 'POST'])
def classstock_q():
    if current_user.is_authenticated:
        src = "https://tw.stock.yahoo.com/s/list.php?c=%B3q%ABH%BA%F4%B8%F4&rr=0.35530600%201535770407"
        html = requests.get(src)
        html.encoding = "cp950"

        sp = BeautifulSoup(html.text, "html.parser")

        data17 = sp.find_all("table")

        q = data17[4].text
        q = q.replace("\n \n\n", "@")
        q = q.replace("\n\n\n\n", "@")
        q = q.replace("\n\n", "\n")
        q = q.replace("\n", ",")
        q = q.replace("@", "\n")
        list_q = q.split("\n")
    else:
        flash('You need login!', 'warning')
        return redirect(url_for('main.home'))
    return render_template('classstock/classstock_q.html', list_q=list_q)

@classstock.route("/classstock_r", methods=['GET', 'POST'])
def classstock_r():
    if current_user.is_authenticated:
        src = "https://tw.stock.yahoo.com/s/list.php?c=%B9q%A4l%B9s%B2%D5%A5%F3&rr=0.35530700%201535770407"
        html = requests.get(src)
        html.encoding = "cp950"

        sp = BeautifulSoup(html.text, "html.parser")

        data18 = sp.find_all("table")

        r = data18[4].text
        r = r.replace("\n \n\n", "@")
        r = r.replace("\n\n\n\n", "@")
        r = r.replace("\n\n", "\n")
        r = r.replace("\n", ",")
        r = r.replace("@", "\n")
        list_r = r.split("\n")
    else:
        flash('You need login!', 'warning')
        return redirect(url_for('main.home'))
    return render_template('classstock/classstock_r.html', list_r=list_r)

@classstock.route("/classstock_s", methods=['GET', 'POST'])
def classstock_s():
    if current_user.is_authenticated:
        src = "https://tw.stock.yahoo.com/s/list.php?c=%B9q%A4l%B3q%B8%F4&rr=0.35530900%201535770407"
        html = requests.get(src)
        html.encoding = "cp950"

        sp = BeautifulSoup(html.text, "html.parser")

        data19 = sp.find_all("table")

        s = data19[4].text
        s = s.replace("\n \n\n", "@")
        s = s.replace("\n\n\n\n", "@")
        s = s.replace("\n\n", "\n")
        s = s.replace("\n", ",")
        s = s.replace("@", "\n")
        list_s = s.split("\n")
    else:
        flash('You need login!', 'warning')
        return redirect(url_for('main.home'))
    return render_template('classstock/classstock_s.html', list_s=list_s)

@classstock.route("/classstock_t", methods=['GET', 'POST'])
def classstock_t():
    if current_user.is_authenticated:
        src = "https://tw.stock.yahoo.com/s/list.php?c=%B8%EA%B0T%AAA%B0%C8&rr=0.35531000%201535770407"
        html = requests.get(src)
        html.encoding = "cp950"

        sp = BeautifulSoup(html.text, "html.parser")

        data20 = sp.find_all("table")

        t = data20[4].text
        t = t.replace("\n \n\n", "@")
        t = t.replace("\n\n\n\n", "@")
        t = t.replace("\n\n", "\n")
        t = t.replace("\n", ",")
        t = t.replace("@", "\n")
        list_t = t.split("\n")
    else:
        flash('You need login!', 'warning')
        return redirect(url_for('main.home'))
    return render_template('classstock/classstock_t.html', list_t=list_t)

@classstock.route("/classstock_u", methods=['GET', 'POST'])
def classstock_u():
    if current_user.is_authenticated:
        src = "https://tw.stock.yahoo.com/s/list.php?c=%A8%E4%A5%A6%B9q%A4l&rr=0.35531100%201535770407"
        html = requests.get(src)
        html.encoding = "cp950"

        sp = BeautifulSoup(html.text, "html.parser")

        data21 = sp.find_all("table")

        u = data21[4].text
        u = u.replace("\n \n\n", "@")
        u = u.replace("\n\n\n\n", "@")
        u = u.replace("\n\n", "\n")
        u = u.replace("\n", ",")
        u = u.replace("@", "\n")
        list_u = u.split("\n")
    else:
        flash('You need login!', 'warning')
        return redirect(url_for('main.home'))
    return render_template('classstock/classstock_u.html', list_u=list_u)

@classstock.route("/classstock_v", methods=['GET', 'POST'])
def classstock_v():
    if current_user.is_authenticated:
        src = "https://tw.stock.yahoo.com/s/list.php?c=%C0%E7%AB%D8&rr=0.35531200%201535770407"
        html = requests.get(src)
        html.encoding = "cp950"

        sp = BeautifulSoup(html.text, "html.parser")

        data22 = sp.find_all("table")

        v = data22[4].text
        v = v.replace("\n \n\n", "@")
        v = v.replace("\n\n\n\n", "@")
        v = v.replace("\n\n", "\n")
        v = v.replace("\n", ",")
        v = v.replace("@", "\n")
        list_v = v.split("\n")
    else:
        flash('You need login!', 'warning')
        return redirect(url_for('main.home'))
    return render_template('classstock/classstock_v.html', list_v=list_v)

@classstock.route("/classstock_w", methods=['GET', 'POST'])
def classstock_w():
    if current_user.is_authenticated:
        src = "https://tw.stock.yahoo.com/s/list.php?c=%AF%E8%B9B&rr=0.35531400%201535770407"
        html = requests.get(src)
        html.encoding = "cp950"

        sp = BeautifulSoup(html.text, "html.parser")

        data23 = sp.find_all("table")

        w = data23[4].text
        w = w.replace("\n \n\n", "@")
        w = w.replace("\n\n\n\n", "@")
        w = w.replace("\n\n", "\n")
        w = w.replace("\n", ",")
        w = w.replace("@", "\n")
        list_w = w.split("\n")
    else:
        flash('You need login!', 'warning')
        return redirect(url_for('main.home'))
    return render_template('classstock/classstock_w.html', list_w=list_w)

@classstock.route("/classstock_x", methods=['GET', 'POST'])
def classstock_x():
    if current_user.is_authenticated:
        src = "https://tw.stock.yahoo.com/s/list.php?c=%C6%5B%A5%FA&rr=0.35531500%201535770407"
        html = requests.get(src)
        html.encoding = "cp950"

        sp = BeautifulSoup(html.text, "html.parser")

        data24 = sp.find_all("table")

        x = data24[4].text
        x = x.replace("\n \n\n", "@")
        x = x.replace("\n\n\n\n", "@")
        x = x.replace("\n\n", "\n")
        x = x.replace("\n", ",")
        x = x.replace("@", "\n")
        list_x = x.split("\n")
    else:
        flash('You need login!', 'warning')
        return redirect(url_for('main.home'))
    return render_template('classstock/classstock_x.html', list_x=list_x)

@classstock.route("/classstock_y", methods=['GET', 'POST'])
def classstock_y():
    if current_user.is_authenticated:
        src = "https://tw.stock.yahoo.com/s/list.php?c=%AA%F7%BF%C4&rr=0.35531600%201535770407"
        html = requests.get(src)
        html.encoding = "cp950"

        sp = BeautifulSoup(html.text, "html.parser")

        data25 = sp.find_all("table")

        y = data25[4].text
        y = y.replace("\n \n\n", "@")
        y = y.replace("\n\n\n\n", "@")
        y = y.replace("\n\n", "\n")
        y = y.replace("\n", ",")
        y = y.replace("@", "\n")
        list_y = y.split("\n")
    else:
        flash('You need login!', 'warning')
        return redirect(url_for('main.home'))
    return render_template('classstock/classstock_y.html', list_y=list_y)

@classstock.route("/classstock_z", methods=['GET', 'POST'])
def classstock_z():
    if current_user.is_authenticated:
        src = "https://tw.stock.yahoo.com/s/list.php?c=%B6T%A9%F6%A6%CA%B3f&rr=0.35531700%201535770407"
        html = requests.get(src)
        html.encoding = "cp950"

        sp = BeautifulSoup(html.text, "html.parser")

        data26 = sp.find_all("table")

        z = data26[4].text
        z = z.replace("\n \n\n", "@")
        z = z.replace("\n\n\n\n", "@")
        z = z.replace("\n\n", "\n")
        z = z.replace("\n", ",")
        z = z.replace("@", "\n")
        list_z = z.split("\n")
    else:
        flash('You need login!', 'warning')
        return redirect(url_for('main.home'))
    return render_template('classstock/classstock_z.html', list_z=list_z)

@classstock.route("/classstock_A", methods=['GET', 'POST'])
def classstock_A():
    if current_user.is_authenticated:
        src = "https://tw.stock.yahoo.com/s/list.php?c=%AAo%B9q%BFU%AE%F0&rr=0.35531800%201535770407h"
        html = requests.get(src)
        html.encoding = "cp950"

        sp = BeautifulSoup(html.text, "html.parser")

        data27 = sp.find_all("table")

        A = data27[4].text
        A = A.replace("\n \n\n", "@")
        A = A.replace("\n\n\n\n", "@")
        A = A.replace("\n\n", "\n")
        A = A.replace("\n", ",")
        A = A.replace("@", "\n")
        list_A = A.split("\n")
    else:
        flash('You need login!', 'warning')
        return redirect(url_for('main.home'))
    return render_template('classstock/classstock_aa.html', list_A=list_A)

@classstock.route("/classstock_B", methods=['GET', 'POST'])
def classstock_B():
    if current_user.is_authenticated:
        src = "https://tw.stock.yahoo.com/s/list.php?c=%A8%E4%A5L&rr=0.35532000%201535770407"
        html = requests.get(src)
        html.encoding = "cp950"

        sp = BeautifulSoup(html.text, "html.parser")

        data28 = sp.find_all("table")

        B = data28[4].text
        B = B.replace("\n \n\n", "@")
        B = B.replace("\n\n\n\n", "@")
        B = B.replace("\n\n", "\n")
        B = B.replace("\n", ",")
        B = B.replace("@", "\n")
        list_B = B.split("\n")
    else:
        flash('You need login!', 'warning')
        return redirect(url_for('main.home'))
    return render_template('classstock/classstock_bb.html', list_B=list_B)

@classstock.route("/classstock_C", methods=['GET', 'POST'])
def classstock_C():
    if current_user.is_authenticated:
        src = "https://tw.stock.yahoo.com/s/list.php?c=%A6s%B0U%BE%CC%C3%D2&rr=0.35532100%201535770407"
        html = requests.get(src)
        html.encoding = "cp950"

        sp = BeautifulSoup(html.text, "html.parser")

        data29 = sp.find_all("table")

        C = data29[4].text
        C = C.replace("\n \n\n", "@")
        C = C.replace("\n\n\n\n", "@")
        C = C.replace("\n\n", "\n")
        C = C.replace("\n", ",")
        C = C.replace("@", "\n")
        list_C = C.split("\n")
    else:
        flash('You need login!', 'warning')
        return redirect(url_for('main.home'))
    return render_template('classstock/classstock_cc.html', list_C=list_C)

@classstock.route("/classstock_F", methods=['GET', 'POST'])
def classstock_F():
    if current_user.is_authenticated:
        src = "https://tw.stock.yahoo.com/s/list.php?c=%AB%FC%BC%C6%C3%FE&rr=0.35532500%201535770407"
        html = requests.get(src)
        html.encoding = "cp950"

        sp = BeautifulSoup(html.text, "html.parser")

        data32 = sp.find_all("table")

        F = data32[4].text
        F = F.replace("\n \n\n", "@")
        F = F.replace("\n\n\n\n", "@")
        F = F.replace("\n\n", "\n")
        F = F.replace("\n", ",")
        F = F.replace("@", "\n")
        list_F = F.split("\n")
    else:
        flash('You need login!', 'warning')
        return redirect(url_for('main.home'))
    return render_template('classstock/classstock_ff.html', list_F=list_F)

@classstock.route("/classstock_G", methods=['GET', 'POST'])
def classstock_G():
    if current_user.is_authenticated:
        src = "https://tw.stock.yahoo.com/s/list.php?c=ETF&rr=0.35532600%201535770407"
        html = requests.get(src)
        html.encoding = "cp950"

        sp = BeautifulSoup(html.text, "html.parser")

        data33 = sp.find_all("table")

        G = data33[4].text
        G = G.replace("\n \n\n", "@")
        G = G.replace("\n\n\n\n", "@")
        G = G.replace("\n\n", "\n")
        G = G.replace("\n", ",")
        G = G.replace("@", "\n")
        list_G = G.split("\n")
    else:
        flash('You need login!', 'warning')
        return redirect(url_for('main.home'))
    return render_template('classstock/classstock_gg.html', list_G=list_G)

@classstock.route("/classstock_H", methods=['GET', 'POST'])
def classstock_H():
    if current_user.is_authenticated:
        src = "https://tw.stock.yahoo.com/s/list.php?c=%A8%FC%AFq%C3%D2%A8%E9&rr=0.35532700%201535770407"
        html = requests.get(src)
        html.encoding = "cp950"

        sp = BeautifulSoup(html.text, "html.parser")

        data34 = sp.find_all("table")

        H = data34[4].text
        H = H.replace("\n \n\n", "@")
        H = H.replace("\n\n\n\n", "@")
        H = H.replace("\n\n", "\n")
        H = H.replace("\n", ",")
        H = H.replace("@", "\n")
        list_H = H.split("\n")
    else:
        flash('You need login!', 'warning')
        return redirect(url_for('main.home'))
    return render_template('classstock/classstock_hh.html', list_H=list_H)