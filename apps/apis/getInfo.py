from . import api
from flask import render_template, request, jsonify
from apps.common import getInfo_common



@api.route('/index', methods = ['GET'])
def index():
    try:
        total100 = getInfo_common.getListInfo()
    except Exception as e:
        return jsonify(msg = str(e))

    return render_template('/index.html', data = total100)


@api.route('/config', methods = ['GET'])
def config():
    deviceId = request.args.get("device")
    token = request.args.get("token")

    strr = '''DEVICEID = '{}'\nTOKEN = '{}' '''.format(deviceId, token)
    with open('./apps/constance.py', 'w') as f:
        f.write(strr)

    return jsonify(code = '100')




