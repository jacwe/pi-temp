#!/usr/bin/python

from flask import Flask, render_template
import datetime
app = Flask(__name__)

@app.route("/")
def hello():
   now = datetime.datetime.now()
   timeString = now.strftime("%H:%M:%S")
   dateString = now.strftime("%Y-%m-%d")
   templateData = {
      'title' : 'HELLO!',
      'time': timeString,
      'date': dateString,
      'temp' : getTemp()
      }
   return render_template('index.html', **templateData)

def getTemp():
	tfile = open('/sys/class/thermal/thermal_zone0/temp')
	text = tfile.read()
	tfile.close()
	temperature_data = text.split()[-1]
	temperature = float(temperature_data[2:])
	return ((temperature / 10) * 1.8) + 32


if __name__ == "__main__":
	app.run(host='0.0.0.0')

