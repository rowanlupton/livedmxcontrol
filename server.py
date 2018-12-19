import sys
from flask import abort, Flask, render_template, request, Response
sys.path.insert(0, 'pyenttec/')
import pyenttec

app = Flask(__name__)
dmx = pyenttec.select_port()

# {
#   "channels_list": [
#     {"channel": 50, "value": 255},
#     {"channel": 51, "value": 0},
#     {"channel": 52, "value": 0}
#   ]
# }

@app.route('/', methods=['POST'])
def jsonHandler():
    try:
        contents = request.get_json()['channels_list']
        for content in contents:
            # print(content['channel'],': ',content['value'])
            dmx.dmx_frame[content['channel']] = content['value']

        dmx.render()
        return Response(status=204, mimetype='application/json')
    except TypeError:
        abort(400)
