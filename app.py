from chalice import Chalice
from chalicelib.redis_publisher import publisher, redis_connection

app = Chalice(app_name='serverless-example')


@app.route('/', methods=["POST", "GET"])
@publisher(channel="hakanTV")
def index():
    request = app.current_request
    if request.method == 'POST':
        return request.json_body

    elif request.method == 'GET':
        return {"redis_status": redis_connection().ping()}
