{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "e2781dfa",
   "metadata": {},
   "outputs": [],
   "source": [
    "import urllib.request\n",
    "import requests\n",
    "import threading\n",
    "import json\n",
    "\n",
    "import random"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "6e907757",
   "metadata": {},
   "outputs": [
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
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "6cf9d6e7",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.8.8"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
