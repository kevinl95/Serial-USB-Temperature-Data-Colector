# Serial USB Temperature Data Collector

![Icon](https://kevinmichaelloeffler.files.wordpress.com/2018/05/entypo_e7570_1024.png?w=256&h=256)
This is a repository that collects files related to my [tutorial on how to use Python to collect and save data from a microcontroller to your PC.](https://kevinmloeffler.com/2018/05/05/use-python-to-collect-and-save-data-from-microcontrollers-to-your-pc/) This program is available for macOS High Sierra or Windows 10 (see the releases page to download) and can be used to collect temperature data from the Teensy-based temperature collector I outline in my tutorial. It looks like this:
![Wiring diagram](https://kevinmichaelloeffler.files.wordpress.com/2018/05/temp_diagram-001.jpeg)

# Dependencies

You will need to install [PySerial](https://pythonhosted.org/pyserial/) (I recommend using pip) and Python 3 to run this code. [PyInstaller](https://www.pyinstaller.org) was used to create the binaries on the releases page. The [Arduino IDE](https://www.arduino.cc/en/Main/Software) and the [Teensy packages](https://www.pjrc.com/teensy/teensyduino.html) are needed to flash the Teensy with the [serial_temperature_sensor.ino](https://github.com/kevinl95/Serial-USB-Temperature-Data-Collector/blob/master/serial_temperature_sensor.ino "serial_temperature_sensor.ino") sketch, which collects temperature information from the sensor and then prints it to serial in Celsius or Fahrenheit.

# Bill of Materials for the Sensor
1x [Teensy LC](https://www.pjrc.com/teensy/teensyLC.html), $11.65
1x [TMP36 Analog Temperature Sensor](https://www.sparkfun.com/products/10988), $1.50
