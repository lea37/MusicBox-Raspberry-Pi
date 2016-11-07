### Python script for Capacitive Touch HAT for Raspberry Pi - MPR121

Because i couldn't found one and that everything was based either on Arduino or other boards. I've came up with this script after doing raspberry GPIO's tutorial ([music box tutorial](https://www.raspberrypi.org/learning/gpio-music-box/worksheet/) helped me a lot), and 
based on the [old tutorial for the MPR121 Capacitive Sensor x5](https://learn.adafruit.com/mpr121-capacitive-touch-sensor-on-raspberry-pi-and-beaglebone-black/hardware). It is my first python script so feel free to test/change, or tell me how to make it better, even if of course you'll have to deal with your own installation i guess. You will find 2 files. One simple script (simple-music-box.py) that detect if the pin is touched, that's all ,so the sound will have some echos but i kind of like this little sound imperfections. The other one detect the current and the last touch and add a delay before re-playing it if it's still touched. Enjoy !

#### What you need ?
* [Raspberry Pi model B](https://www.adafruit.com/products/3055) 
* [A Capactivie Touch Sensor HAT x12](https://www.adafruit.com/product/2340)
* Cables or [Alligator clips](https://www.adafruit.com/product/1008)
* Speakers
* Anything to clip on (fruits, aluminium, potatoes ...) that conduct electricity

For this little tutorial, i'm assuming that you already have setting up your Raspberry Pi audio. If not, you can follow [this easy tutorial](http://www.raspberrypi-spy.co.uk/2012/06/raspberry-pi-speakers-analog-sound-test/) to setup and test audio on your Raspberry Pi.

**#1** First you have to weld Capacitive Touch HAT with the 2x20 socket header that comes with it. 

**#2** Second you have to [configure I2C](https://learn.adafruit.com/adafruits-raspberry-pi-lesson-4-gpio-setup/configuring-i2c) so it will detect the Capacitive Hat when it's clip on the Raspberry Pi.

**#3** You have to update and download some softwares on your Raspberry Pi. Make sure it is plugged and connected to internet, then you can apply this command lines :
```
sudo apt-get update
sudo apt-get install build-essential python-dev python-smbus python-pip git
```

Everything is ready ! Then run the script :
```
git clone /this repository/
cd Music-touch
sudo python simple-music-touch.py 
```

Then touched any of the cable/fruit/potatoes. Can you here it ?! :D Yeahhh 
You can easily change the sounds that are in sounds folder. 
***Additionnal Note !*** If you play your own sounds and don't hear anything or juste a buzz note even if your audio test works perfectly that means that the sound that you've choose don't have the right configuration. It needs to be in 16Bits and 44100Hrz. Please be sure of that.  

