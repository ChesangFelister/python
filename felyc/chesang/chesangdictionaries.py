        Python 3.7.2 (tags/v3.7.2:9a3ffc0492, Dec 23 2018, 22:20:52) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> v=range(2019,2119);
>>> for x in v:
	if x%4==0:
		print(x)

		
2020
2024
2028
2032
2036
2040
2044
2048
2052
2056
2060
2064
2068
2072
2076
2080
2084
2088
2092
2096
2100
2104
2108
2112
2116
>>> student1={"name":"mambo bado","Y.O.B":1960}
>>> student2={"name":"Dunia kubwa","Y.O.B":1965}
>>> student3={"name":"Pole Pole","Y.O.B":1970}
>>> student4={"name":"Vidude dude","Y.O.B":1980}
>>> student5={"name":"Kidude de","Y.O.B":1990}
>>> students=[student1,student2,student3,student4,student5]
>>> for student in students:
	days=(2019-student["Y.O.B"])*365
	print ("Hello {}, you are {} days old.".format (student["name"], days))

	
Hello mambo bado, you are 21535 days old.
Hello Dunia kubwa, you are 19710 days old.
Hello Pole Pole, you are 17885 days old.
Hello Vidude dude, you are 14235 days old.
Hello Kidude de, you are 10585 days old.
>>> 
