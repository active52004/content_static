#count the No. of distinct values in a file, store the result to a csv file
#count the No. of each distinct value
import csv

#src_dir: ./short , src_file: test_1
#dst_dir: ./frequence, dst_dir: count_test_1
def repeat_count(src_dir,src_file, dst_dir, dst_file):
	f = file(src+"/"+src_file,"r")
	data_list = []
	data_list = f.readlines()
	print len(data_list)
	
	#my_set contains the distinct values in data_list
	my_set = set(data_list)
	
	#static is a dict, the element is 'value:No. of value'
	static = {}
	for item in my_set:
		static[item]  = data_list.count(item)
	
	result_file = dst_dir+"/"+dst_file
	csvFile = open(result_file,'wb')
	writer = csv.writer(csvFile, dialect='excel')
	
	#writer.writerow(['col1','col2'])#write a head for each column
	for key in static:
		writer.writerow([key,static[key]])



#for i in len(data_list):

