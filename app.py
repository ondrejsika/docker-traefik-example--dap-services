import os
from flask import Flask
from redis import Redis

app = Flask(__name__)
hostname = os.environ['HOSTNAME']

@app.route("/")
def index():
    redis = Redis(os.environ.get('REDIS', 'redis'))
    counter = redis.incr('counter')
    return "%s %d" % (hostname, counter)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port='80')
