import hashlib
import os, sys
from subprocess import check_output


class Licenser():
	def __init__(self):
		self.os_type = sys.platform.lower()

		if "windows" in self.os_type:
				self.command_serial_num = "wmic csproduct get IdentifyingNumber"
				self.command_hardw_uuid = "wmic csproduct get UUID"
		elif "linux" in self.os_type:
				self.command_serial_num = "dmidecode -s system-serial-number"
				self.command_hardw_uuid = "dmidecode -s system-uuid"
		elif "darwin" in self.os_type:
				self.command_serial_num = "system_profiler SPHardwareDataType | grep Serial"
				self.command_hardw_uuid = "system_profiler SPHardwareDataType | grep UUID"


	def __getLicenseSum(self):
		serial_num = os.popen(self.command_serial_num).read() \
						.replace("\n","") \
						.replace(' ','')  \
						.replace('"', "")
		
		hardw_uuid = os.popen(self.command_hardw_uuid).read() \
						.replace("\n","") \
						.replace(' ','')  \
						.replace('"', "")

		serial_num = serial_num[serial_num.find(':') + 1:]
		hardw_uuid = hardw_uuid[hardw_uuid.find(':') + 1:]

		key_string = serial_num + ':' + hardw_uuid

		return hashlib.sha256(key_string.encode('utf-8')).hexdigest()


	def genLicense(self):
		file = open('license.dat', 'w')
		file.write(self.__getLicenseSum())
		file.close()


	def checkLicense(self, path_to_file):
		try:
			file = open(path_to_file, 'r')
		except:
			print('FileNotFound error...')
			return False

		license_string = file.read()
		if license_string == self.__getLicenseSum():
			return True
		else:
			return False
