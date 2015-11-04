# pyramid
Siyavula - Pyramid

This program welcomes any user to the Home page and request a Wikipedia link (url) from a user. If the you omit the the url or enter a url that is not from wikipedia, a pop up alert will remind a user to enter a valid url (From wikipedia). Once the user enter the Wikipedia url, that Wikipedia page will be download in html format then displayed to the new page. From the new page, the user might decide to restart the process and this can be done by clicking on the "Home" (Top left).

To use this program, just clone this repository and you can run these command on any Linux - Ubuntu machine:
$ sudo apt-get install git
$ git clone .... && cd pyramid 
$ sudo apt-get install python-virtualenv
$ virtualenv pyramid
$ source pyramid/bin/activate
$ python run.py
Then browse your localhost or IP at port 8080

Here are the requirements for setting up the pyramid framework virtual environment for this project:
$ mkdir pyramid && cd pyramid
$ sudo apt-get install python-virtualenv
$ sudo apt-get install python-pip
$ sudo pip install virtualenv
$ sudo virtualenv pyramid
$ sudo pyramid/bin/pip install "pyramid==1.5.7"
$ touch run.py
$ sudo chmod +x run.py
$ mkdir app && cd app
$ mkdir templates
$ touch __init__.py
$ touch views.py
$ source pyramid/bin/activate
$ sudo pyramid/bin/pip install pyramid_jinja2
$ sudo pyramid/bin/pip install BeautifulSoup
