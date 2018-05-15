# Raspberry Pi SQLite Sensors 



## Setup

First make sure you have Python  and a few dependencies installed on the Pi by running :

```
sudo apt-get update
sudo apt-get install -y python python-dev python-pip git sqlite
```
Next install the DHT sensor Python library:

```
git clone https://github.com/adafruit/Adafruit_Python_DHT.git
cd Adafruit_Python_DHT
sudo python3 setup.py install
```

Using an ORM can simplify your code to talk to
databases and even remove much of the need to manually write and run SQL queries.
Issue the following command to install the flask web framework
```
sudo pip3 install peewee
```


and flask-admin plugin:

    sudo pip3 install flask flask-admin wtf-peewee
    
## Database Setup

Use SQLite to create a database called dht.db:

    sqlite dht.db

At the SQL prompt issues the following create statements to create a table for
sensor readings, and a table for sensor configuration:

    CREATE TABLE readings (time DATETIME, name TEXT, value REAL);
    CREATE TABLE sensors (name TEXT, type TEXT, pin INTEGER);

Add a configured DHT sensor to the sensors table with an insert command (note
you can do this multiple times for multiple sensors):

    INSERT INTO sensors VALUES ('DHT1', 'DHT22', 18);

Change the values inside the parenthesis to the desird name (any string), the type
of DHT sensor (either 'DHT22' or 'DHT11' exactly), and the pin connected to the
sensor output.

## Usage

Modify dht_read.py to define the DHT sensors you have connected to your hardware
(i.e. change the data.define_sensor function calls as appropriate).  Then run
the dht_read.py as root and it will automatically create the dht.db database,
populate it with the defined sensors, and then loop taking sensor readings every
two seconds.  For example run with:

    sudo python3 dht_read.py

Next to run the web application (you can open a new connection to the Pi so the
dht_read.py scripts keeps running in the background) run the following command:

    FLASK_APP=webapp.py flask run --host=0.0.0.0

NOTE: The above assumes you are using the very latest version of flask, if you
aren't then run the following to upgrade flask:

    sudo pip3 install flask --upgrade

You should see something like the following to indicate the web app is running
on port 5000:

    * Serving Flask app "webapp"
    * Forcing debug mode on
    * Running on http://0.0.0.0:5000/ (Press CTRL+C to quit)

Open a browser and navigate to http://raspberrypi:5000/ (note you might need to
use the IP address of your pi if your router doesn't resolve the hostname automatically).
