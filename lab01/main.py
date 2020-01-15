from license import Licenser

def main():
	lic = Licenser()
	if lic.checkLicense('./license.dat'):
		print('Correct license!')
	else:
		print('ERROR! Bad license!')


if __name__ == "__main__":
	main()