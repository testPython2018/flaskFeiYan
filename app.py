from flask import Flask,render_template,jsonify
import requests

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_data/')
def get_data():
    total_list = []
    today_list = []
    totalSuspect_list=[]
    todaySuspect_list=[]

    totalHeal_list=[]
    todayHeal_list=[]

    ncov_data = {}
    headers = {
        'user-agent': '',
        'accept': ''
    }
    url = 'https://c.m.163.com/ug/api/wuhan/app/data/list-total'
    res = requests.get(url, headers=headers)
    data = res.json()['data']['chinaDayList']
    for i in data:
        date = i['date']
        today = i['today']['confirm']
        total = i['total']['confirm']

        todaySuspect=i['today']['suspect']
        totalSuspect=i['total']['suspect']

        todayHeal=i['today']['heal']
        totalHeal=i['total']['heal']


        today_list.append({'name': date, 'y': today})
        total_list.append({'name': date, 'y': total})
        todaySuspect_list.append({'name': date, 'y': todaySuspect})
        totalSuspect_list.append({'name': date, 'y': totalSuspect})
        todayHeal_list.append({'name': date, 'y': todayHeal})
        totalHeal_list.append({'name': date, 'y': totalHeal})


    ncov_data['today'] = today_list[:]
    ncov_data['total'] = total_list[:]
    ncov_data['total_sus'] = totalSuspect_list[:]
    ncov_data['total_heal'] = totalHeal_list[:]

    return jsonify(ncov_data)

if __name__ == '__main__':
    app.run()
