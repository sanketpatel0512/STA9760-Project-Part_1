from sodapy import Socrata

#Define Main Function For NYC Parking Violation Data Collection & Output
def main(page_size,num_pages,output):
	client = Socrata("data.cityofnewyork.us",APP_KEY) #APP_KEY is APP_TOKEN from Socrata
	offset = 0

	# Open Output file provided by user		
	if output != False:
		outfile = open(output, 'w')

	#For loop to Call Data from NYC Open Data
	for i in range(num_pages):
		d = client.get("nc67-uf89",limit=page_size,offset = off_set)
		# Output data based on user's choice
		# Print Data In Stdout
		if output == False:
			for i in d:
				print(i)
		# Save data to output file
		else:
			for i in d:
				json.dump(i, outfile)
				outfile.write('\n')
		off_set += page_size
		print(d)

if __name__ == '__main__':
	p = 10
	n = 5
	o = "results.json"
	main(p,n,o)