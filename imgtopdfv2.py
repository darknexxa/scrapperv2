import os
import img2pdf
from os.path import isfile, join
import argparse
ap = argparse.ArgumentParser()
ap.add_argument("-pd", "--pd", required = False, help = "pdir")
ap.add_argument("-d", "--d", required = False, help = "dir")
ap.add_argument("-f", "--f", required = False, help = "file")
args = vars(ap.parse_args())
if(args["pd"]):
	for y in next(os.walk(args["pd"]))[1]:
		onlyfiles = [f for f in os.listdir(args["pd"]+y) if isfile(join(args["pd"]+y, f)) and ('.jpg' in f or '.png' in f)]
		onlyfiles.sort()
		onlyfiles = [args["pd"]+y+"/"+f for f in onlyfiles]
		with open(args["pd"]+y+"/"+y+".pdf","wb") as f:
			f.write(img2pdf.convert(onlyfiles))
			print("Completed pdf at:"+args["pd"]+y+"/"+y+".pdf")
elif(args["d"]):
	onlyfiles = [f for f in os.listdir(args["d"]) if isfile(join(args["d"], f)) and ('.jpg' in f or '.png' in f)]
	onlyfiles.sort()
	onlyfiles = [args["d"]+"/"+f for f in onlyfiles]
	with open(args["d"]+"/"+args["d"]+".pdf","wb") as f:
		f.write(img2pdf.convert(onlyfiles))
		print("Completed pdf at:"+args["d"]+"/"+args["d"]+".pdf")
elif(args["f"]):
	with open(args["f"]+".pdf","wb") as f:
		f.write(img2pdf.convert(args["f"]))
	print("Completed pdf at:"+args["f"]+".pdf")
# print (len(next(os.walk("/Volumes/LISA/New Doujin/"))[1]))
# mypath = "/Volumes/LISA/New Doujin/(C94) [Nyuu Koubou (Nyuu)] Oidemase!! 2-jigen Fuuzoku Gakuen Dai 2 Kukaku (Various) [English]"
# onlyfiles = [f for f in os.listdir(mypath) if isfile(join(mypath, f))]
# onlyfiles.remove(".DS_Store")
# onlyfiles.remove("output.pdf")
# onlyfiles.sort()
# onlyfiles = [mypath+"/"+f for f in onlyfiles]
# with open(mypath+"/output.pdf","wb") as f:
# 	for x in onlyfiles:
# 		f.write(img2pdf.convert(onlyfiles))
# 	print("Completed pdf :")