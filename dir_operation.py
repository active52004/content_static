import os
import repeat_count

src_dir = "./tmp"
dst_dir = "./frequency"

#the filename is stored in the variable "filenames"
#for each filename, 
for filenames in os.listdir(src_dir):
	repeat_count.repeat_count(src_dir,filenames,dst_dir,"count_"+filenames)
#print filenames


