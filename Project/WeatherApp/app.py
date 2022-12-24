from os import error
from flask import Flask,render_template ,request
import datetime as dt
from time import strftime
import requests
import math as m

app=Flask(__name__)


# key: 523abac9215bdde4f2c880d58649e38e
# API url: api.openweathermap.org/data/2.5/weather?q={city name}&appid={API key}

def get_weather(city):
    weather_key='523abac9215bdde4f2c880d58649e38e'
    url='https://api.openweathermap.org/data/2.5/weather'
    param={'APPID':weather_key,'q':city,'units':'metric'}
    response=requests.get(url,param)
    weather=response.json()
    return weather

@app.route('/',methods=['GET','POST'])
def index():
    if request.method=='GET':
        return render_template("home.html")
    elif request.method=='POST':
        data=request.form
        error='There is no data to show,Please enter Valid City....!'
        try:
            weather=get_weather(data['city'])
            city=weather['name']
            condition=weather['weather'][0]['description']
            temp=m.ceil(weather['main']['temp'])
            lon=weather['coord']['lon']
            lat=weather['coord']['lat']
            temp_min=round(weather['main']['temp_min'])
            temp_max=round(weather['main']['temp_max'])
            pressure=weather['main']['pressure']
            humidity=weather['main']['humidity']
            wind_speed=(m.floor(weather['wind']['speed']))*3.6
            x=dt.datetime.now()
            time,day=x.strftime("%I:%M %p"),x.strftime("%d %b,%a")
            icon=weather['weather'][0]['icon']
            result_1={
                'city':city,'condition':condition,'temp':temp,'weather':weather,'lon':lon,'lat':lat,'temp_min':temp_min,
                'temp_max':temp_max,'pressure':pressure,'humidity':humidity,'wind_speed':wind_speed}
            result_2={'time':time,'day':day,'icon':icon}

        except:
            return render_template('home.html',error=error)

        return render_template('result.html',result_1=result_1,result_2=result_2)

@app.route('/about')
def about():
    return render_template('about.html')

if __name__ =='__main__':
    app.run(debug=True)