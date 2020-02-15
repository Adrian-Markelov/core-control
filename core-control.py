
from flask import Flask, jsonify, request, Response

import jsonpickle
import numpy as np
import cv2

'''
FLASK IMAGE TRANSER EXAMPLE
- https://gist.github.com/kylehounslow/767fb72fde2ebdd010a0bf4242371594

FLASK GENERAL EXAMPLES
- https://realpython.com/flask-by-example-part-1-project-setup/

'''

app = Flask(__name__)


@app.route('/image_data', methods=['GET', 'POST'])
def image_data():
    r = request
    # convert string of image data to uint8
    nparr = np.fromstring(r.data, np.uint8)
    # decode image
    img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)

    # do some fancy processing here....

    # build a response dict to send back to client
    response = {'message': 'image received. size={}x{}'.format(img.shape[1], img.shape[0])
                }

    print(response)

    # encode response using jsonpickle
    response_pickled = jsonpickle.encode(response)

    return Response(response=response_pickled, status=200, mimetype="application/json")


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
