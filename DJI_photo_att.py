import PhotoScan
from xml.dom import minidom

elements = ["drone-dji:AbsoluteAltitude=", 
			"drone-dji:RelativeAltitude=", 
			"drone-dji:GimbalRollDegree=", 
			"drone-dji:GimbalYawDegree=",
			"drone-dji:GimbalPitchDegree=", 
			"drone-dji:FlightRollDegree=", 
			"drone-dji:FlightYawDegree=", 
			"drone-dji:FlightPitchDegree="]

chunk = PhotoScan.app.document.chunk

# for camera in chunk.cameras:

	# path = camera.photo.path	
	# with open(path, "rb") as file:
		# image = file.read()
	# string = str(image)
	# xmp_start = string.find('<x:xmpmeta')
	# xmp_end = string.find('</x:xmpmeta')
	# file.close()
	
	# if xmp_start != xmp_end:
		# xmpString = string[xmp_start : xmp_end + 12]

		# print(camera.label)
		# for element in elements:
			# value = string[string.find(element) + len(element) : string.find(element) + len(element) + 10]
			# value = float(value.split('\"',3)[1])
			# print(element, value)
            
            
for camera in chunk.cameras:
   yaw = float(camera.photo.meta["DJI/FlightYawDegree"])
   pitch = float(camera.photo.meta["DJI/GimbalPitchDegree"])
   roll = float(camera.photo.meta["DJI/GimbalRollDegree"])
   camera.reference.rotation = PhotoScan.Vector([camera.reference.rotation.x, 0, 0])
print("\nScript finished")