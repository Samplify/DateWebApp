from flask import Flask
from datetime import datetime
import json
import pprint

app = Flask(__name__)

@app.route('/')
def dateroute():
    now = datetime.utcnow()
    year = now.strftime("%Y")
    month = now.strftime("%m")
    day = now.strftime("%d")
    hour = now.strftime("%H")
    minute = now.strftime("%M")
    second = now.strftime("%S")
    microsecond = now.strftime("%f")

    datedict = {
        "year": year,
        "month": month,
        "day": day,
        "hour": hour,
        "minute": minute,
        "second": second,
        "microsecond": microsecond
        }

    jsondate = json.dumps(datedict)

    return jsondate

if __name__ == '__main__':
    app.run(host="0.0.0.0", port="5000")