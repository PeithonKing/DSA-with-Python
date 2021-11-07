def HCFandLCM(a, b):
	p = a*b
	while a > 0:
		a, b = b%a, a
	hcf = b
	lcm = p/hcf
	print(f"HCF and LCM is {hcf} and {lcm} respectively!")
	
HCFandLCM(95,20)
