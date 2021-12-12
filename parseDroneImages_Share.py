import os, sys, time, math, shutil, pprint;



dir = sys.argv[1];

dry_run = False;
dry_run_initialtypesmove = False;

parentdir = "/".join(dir.split("/")[:len(dir.split("/"))-2]) + "/";


foundBadFileTypes = False;
files = [x for x in os.listdir(dir) if not x.startswith(".") and os.path.isfile(dir+x)];
files = sorted(files);
#pprint.pprint(files);
#sys.exit();

for file in files:
	if not file.lower().endswith(".dng") and not file.lower().endswith(".jpg") and not file.lower().endswith(".arw"):
		print "BAD FILE TYPES", file;
		foundBadFileTypes = True;
		if not dry_run_initialtypesmove:
			
			#print parentdir;
			#sys.exit();
			shutil.move(dir+file, parentdir+file);
			print "moving bad file type up one..";
		else:
			sys.exit();
			
if foundBadFileTypes:
	print "FOUND BAD FILE TYPES";
	print "TRY RUNNING AGAIN";
	sys.exit();
		
		
files_jpg = [x for x in files if x.lower().endswith(".jpg")];
files_jpg = sorted(files_jpg);

dng_not_found_from_jpg = [];
for file_jpg in files_jpg:
	file_dng = file_jpg.replace(".jpg",".DNG").replace(".JPG",".DNG");
	#print "checking dng";
	if not os.path.isfile(dir+file_dng):
		print "[ERROR] dng not found from jpg ", file_jpg;
		dng_not_found_from_jpg.append(file_jpg);

if len(dng_not_found_from_jpg) > 0:
	pprint.pprint(dng_not_found_from_jpg);
	
	if not dry_run_initialtypesmove:
		for dngless_jpg in dng_not_found_from_jpg: 
			print "MOVING FROM ";
			print dir+dngless_jpg;
			print "TO";
			print parentdir+dngless_jpg;
			shutil.move(dir+dngless_jpg, parentdir+dngless_jpg);
		print "TRY RUNNING AGAIN";
		sys.exit();
	else:
		sys.exit();

if len(files) % 5 != 0:
	print "Not / 5", len(files), len(files) % 5;
	sys.exit();
	
if len(files) % 10 != 0:
	print "Not / 10";
	sys.exit();
	
	
i=0;	
while i < len(files):
	file = files[i];
	file_name = file.replace(".JPG","").replace(".DNG","").replace(".ARW","");
	print file_name;
	
	if not dry_run:
		shutil.copy(dir+files[i+1],dir+file_name+"_PREVIEW.JPG");
		shutil.copy(dir+files[i],dir+file_name+"_MASTER.ARW");
		
		if not os.path.isdir(dir+file_name+"/"):
			os.mkdir(dir+file_name+"/");
		else:
			print "[WARN] folder already existed";
		if not os.path.isdir(dir+file_name+"/JPG/"):
			os.mkdir(dir+file_name+"/JPG/");
		for j in range(0,10):
			if ".jpg" in dir+files[i+j].lower():
				shutil.move(dir+files[i+j],dir+file_name+"/JPG/"+files[i+j]);
			else:
				shutil.move(dir+files[i+j],dir+file_name+"/"+files[i+j]);
	i+=10;
	
	
