import math

def distance(lat1, long1, lat2, long2):
	
	# Coefficient to convert degrees to radians
	deg2rad = math.pi/180.0
	 
	# Calculate phi in rads
	phi1 = (90.0 - lat1)*deg2rad
	phi2 = (90.0 - lat2)*deg2rad
	 
	# convert theta to rads
	theta1 = long1*deg2rad
	theta2 = long2*deg2rad
	 
	# Compute spherical distance from spherical coordinates.
	
	# cos(arc length) = sin phi1 sin phi2 cos(theta1-theta2) + cos phi1 cos phi2
	# distance = rho * arc length
	 
	cos = (math.sin(phi1)*math.sin(phi2)*math.cos(theta1 - theta2) +
	math.cos(phi1)*math.cos(phi2))
	arc = math.acos( cos )
	 
	#multiply arc lenght by earth radius to get the distance.
	return arc * 3959
	
print(distance(40.7128,74.0059,19.076,72.8777))
