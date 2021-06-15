
    "import urllib.request\n",
    "import requests\n",
    "import threading\n",
    "import json\n",
    "\n",
    "import random"
   
     {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "https://api.thingspeak.com/update?api_key=98EQEIARXL1TDRMA&field1=8&field2=8\n",
      "<http.client.HTTPResponse object at 0x00000000069ED610>\n"
     ]
    }
   ],
   "source": [
    "def thingspeak_post():\n",
    "    threading.Timer(60,thingspeak_post).start()\n",
    "    val=random.randint(1,30)\n",
    "    URl='https://api.thingspeak.com/update?api_key='\n",
    "    KEY='98EQEIARXL1TDRMA'\n",
    "    HEADER='&field1={}&field2={}'.format(val,val)\n",
    "    NEW_URL = URl+KEY+HEADER\n",
    "    print(NEW_URL)\n",
    "    data=urllib.request.urlopen(NEW_URL)\n",
    "    print(data)\n",
    "    \n",
    "if __name__ == '__main__':\n",
    "    thingspeak_post()"
  

import urllib.request
import requests
import threading
import json

import random

def thingspeak_post():
    threading.Timer(60,thingspeak_post).start()
    val=random.randint(1,30)
    URl='https://api.thingspeak.com/update?api_key='
    KEY='98EQEIARXL1TDRMA'
    HEADER='&field1={}&field2={}'.format(val,val)
    NEW_URL = URl+KEY+HEADER
    print(NEW_URL)
    data=urllib.request.urlopen(NEW_URL)
    print(data)
    
if __name__ == '__main__':
    thingspeak_post()
