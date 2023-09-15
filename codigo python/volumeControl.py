import serial

from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
devices = AudioUtilities.GetSpeakers()

interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
volume = interface.QueryInterface(IAudioEndpointVolume)

volume.GetMute()
volume.GetMasterVolumeLevel()
volume.GetVolumeRange()

# Python listens on a port
ser = serial.Serial("COM9", 9600)
v = ""
a = 0
b = 0
while True:
	# read in the value from arduino
	response = ser.readline().decode("utf-8").strip()
	# make sure the value isn't null
	if(response):
		# if the response is different
		if(v != response):
			v = response
			a = int(v)
			b = -a
			print(b)
			volume.SetMasterVolumeLevel(b, None)