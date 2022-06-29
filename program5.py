def squareRoot(n, l) :
	x = n
	count = 0
	while (1) :
		count += 1
		root = 0.5 * (x + (n / x))
		if (abs(root - x) < l) :
			break
		x = root
	return root




num1=int(input("Enter the number:"))
tol=float(input("Enter the tollerance:"))
print("The square root of the number is",squareRoot(num1,tol))
print("***Avishkar Gautam_33***")

