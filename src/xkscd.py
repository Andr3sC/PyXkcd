#!/usr/bin/python3
import requests
import json
from yad import YAD
import tempfile
import urllib.request



##print ("START\n")

json_xkscd_text = requests.get("http://xkcd.com/info.0.json")

json_xkscd = json.loads(json_xkscd_text.text)

yad = YAD()
with tempfile.NamedTemporaryFile() as kscd_img:
##    print("nombre [", kscd_img.name, "]")
    urllib.request.urlretrieve(json_xkscd['img'],kscd_img.name)
    yad_parameters= []
    yad_parameters.append("--image="+kscd_img.name)
    yad_parameters.append("--timeout=30")
    yad_parameters.append("--timeout-indicator=top")
    #yad_parameters.append("--no-buttons")
    yad_parameters.append("--buttons-layout=center")
    yad_parameters.append("--button=gtk-ok:1")
    yad_parameters.append("--undecorated")
    yad.execute(args=yad_parameters)



##print ("END\n")
