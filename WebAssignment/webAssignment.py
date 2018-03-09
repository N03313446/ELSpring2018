from flask import Flask, render_template, request
from datetime import datetime
import sqlite3


app = Flask(__name__)
@app.route('/')
def hello():
     return render_template('Temp.html')

@app.route('/',methods=['POST'])
def PrintData():
     if request.method=='POST':
         upperDate=request.form['upperDate']
         lowerDate=request.form['lowerDate']
         
         tempDateUpper = datetime.strptime(upperDate,'%Y-%m-%d')
         tempDateLower = datetime.strptime(lowerDate,'%Y-%m-%d')
         
         upperDate2 = tempDateUpper.strftime('%m/%d/%Y')
         lowerDate2 = tempDateLower.strftime('%m/%d/%Y')
         
         conn = sqlite3.connect('/home/pi/ELSpring2018/WebAssignment/temp.db')
         cursor = conn.cursor()
         cursor.execute('SELECT * FROM temp WHERE date_time BETWEEN ? AND ?', (upperDate2, lowerDate2,))
        
     return render_template('Temp.html', data=cursor.fetchall(),upperDate=upperDate, lowerDate=lowerDate)




if __name__ == "__main__":
     app.run(host='0.0.0.0', port=300, debug=True)
