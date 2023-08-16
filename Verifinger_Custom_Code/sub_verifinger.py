#Extract File Source: "/home/jupyter/Notebooks/philip/MasterPrint/spoof_print_hidden2_1200.png"
#
#Optical Thresholds: 1, .1, .01 : 18, 30, 40
#Optical Dataset: "/home/jupyter/Notebooks/philip/MasterPrint/Verifinger/Db1_a_optical/"
#Template: "/home/jupyter/Notebooks/philip/MasterPrint/spoof_print_hidden2_1200.png_featurelarge.dat"
#
#Capacitive Thresholds: 1, .1, .01 : 35, 50, 65
#Capacitive Dataset: "/home/jupyter/Notebooks/philip/MasterPrint/Verifinger/DB7AuthentecCapacitivePress/"
#Template: "/home/jupyter/Notebooks/philip/MasterPrint/spoof_print_hidden2_1200.png_featurelarge.dat"


#MILK'S VERIFINGER WRAPPER - RETURNS USER MATCHES ONLY

import subprocess as sp
from PIL import Image
import numpy as np
import os
import time

# VERI_DIR = "Verifinger_12"
# #VERI_DIR = "MOD-Verifinger_SDK"
# #VERI_DIR = "Verifinger_NEW"

# #C++ build locations
# extractLoc = f"/home/jupyter/Notebooks/Milk/DeepPrint2/Verifinger_SDK_Code/{VERI_DIR}/Tutorials/Biometrics/CPP/MilkExtractMinutia/"
# capacitiveLoc = f"/home/jupyter/Notebooks/Milk/DeepPrint2/Verifinger_SDK_Code/{VERI_DIR}/Tutorials/Biometrics/CPP/MilkCapacitive/" 
# opticalLoc = f"/home/jupyter/Notebooks/Milk/DeepPrint2/Verifinger_SDK_Code/{VERI_DIR}/Tutorials/Biometrics/CPP/MilkOptical/"

# #C++ builds
# extractProgram = "./ExtractTemplateFromImage"
# opticalProgram = "./MasterPrintMatchImageFVC"
# capacitiveProgram = "./MasterPrintSubjectMatcher_MILK"

# capTrainProgram = "train"
# capTestProgram = "test"

# #Data Locations
# capacitiveData = "/home/jupyter/Notebooks/Milk/DeepPrint2/Verifinger_SDK_Code/FINGERPRINT_DATASETS/DB7AuthentecCapacitivePress/"
# opticalData = "/home/jupyter/Notebooks/Milk/DeepPrint2/Verifinger_SDK_Code/FINGERPRINT_DATASETS/Db1_a_optical/"

#C++ build locations
extractLoc = "/home/jupyter/Notebooks/Milk/DeepPrint2/Verifinger_SDK_Code/Verifinger_12/Tutorials/Biometrics/CPP/MilkExtractMinutia"
capacitiveLoc = "/home/jupyter/Notebooks/Milk/DeepPrint2/Verifinger_SDK_Code/Verifinger_12/Tutorials/Biometrics/CPP/MilkCapacitive" 
# opticalLoc = "/home/jupyter/Notebooks/philip/MasterPrint/Verifinger/Tutorials/Biometrics/CPP/PhilipOptical/"

#C++ builds
extractProgram = "./ExtractTemplateFromImage"
opticalProgram = "./MasterPrintMatchImageFVC"
capacitiveProgram = "./MasterPrintMatchImageCapacitive"

#Data Locations
capacitiveData = "/home/jupyter/Notebooks/Milk/DeepPrint2/Verifinger_SDK_Code/FINGERPRINT_DATASETS/DB7AuthentecCapacitivePress/"
opticalData = "/home/jupyter/Notebooks/Milk/DeepPrint2/Verifinger_SDK_Code/FINGERPRINT_DATASETS/Db1_a_optical/"


#Global variables
minutiaExtension = "_featurelarge.dat"


#Global variables
minutiaExtension = "_featurelarge.dat"


def extractMinutia(filename):
	sp.run([extractProgram, filename], cwd=extractLoc, stdout=sp.DEVNULL)

def deleteMinutia(filename):
	template = filename + minutiaExtension
	if os.path.exists(template):
		os.remove(template)

def inverseRescale(X):
	return ((X * 0.5 + 0.5) * 255.).astype(np.uint8)

def inverseRescale2(X):
	return (X*255.).astype(np.uint8)

def plotGeneratedImg(npImg, scale = -1, name=""):
	
	#outImg = generatorModel.predict(z.reshape([1,100]))
	outImg = npImg.squeeze()
	
	#normalize from [-1,1] or [0,1] to [0,255]
	if((np.amin(outImg) < 0) and (np.amax(outImg) <= 1)):
		outImg = inverseRescale(outImg)
	elif((np.amin(outImg) >= 0) and (np.amax(outImg) <= 1)):
		outImg = inverseRescale2(outImg)
		
	#print(outImg.shape)
	#print(f'img range = {np.amin(outImg)} - {np.amax(outImg)}')
	
	im = Image.fromarray(255-outImg, mode="L")
	
	#Scale
	if(scale > -1):
		#wpercent = (scale/float(out_img.size[0]))
		#hsize = int((float(out_img.size[1])*float(wpercent)))
		im = im.resize((scale, scale), Image.ANTIALIAS)
		
	name = os.getcwd() + "/spoof_print_"+ name +".png"
	im.save(name)
	return name

#Image Number = %d, Subject Number = %d, Match Score = %d, Total Match Count = %d
#data: optical or capacitive
def matchResults(filename, data, threshold,ttype='full'):
	print("Match results!")
	template = filename + minutiaExtension
	
	ttk={"full":0,"train":1,"test":2}
	ttype_num=ttk[ttype]
	#print(f"ttype: {ttype} | ttype num: {ttype_num}")
	
	if(data == 'optical'):
		program = [opticalProgram, opticalData, template, str(threshold),str(ttype_num)]
		loc = opticalLoc
	elif(data == 'capacitive'):
		program = [capacitiveProgram, capacitiveData, template, str(threshold),str(ttype_num)]
		#print(program)
		loc = capacitiveLoc
		#print(loc)
	out = sp.run(program, cwd=loc, stdout=sp.PIPE, universal_newlines = True, stderr = sp.DEVNULL)
	results = out.stdout.split(';')[:-1]
	print(f"PROGRAM OUTPUT: {out}")
	return results

def usersMatched(img, dataset, threshold, name= "temp", ttype='full'):
	if(type(img) == str):
		fileName = img
	else:
		fileName = plotGeneratedImg(img, 150, name)
		
	#print(fileName)
	extractMinutia(fileName)
	st = time.time()
	data = matchResults(fileName, dataset, threshold,ttype)
	data = [str(int(x)-1) for x in data]
	
	#print(time.time()-st)
	deleteMinutia(fileName)
	if(type(img) != str):
		os.remove(fileName)
	
	if(len(data) == 0):
		return []
		
	return np.array(data)


def score(img, dataset, threshold,name='temp'):
	t = time.time()
	
	img2 = np.array(img)
	if(type(img) == str):
		fileName = img
	else:
		#img2 *= -1.0
		fileName = plotGeneratedImg(img2, 150, name)
		#print(f"Min:{np.amin(img2)} | Max:{np.amax(img2)}")
	extractMinutia(fileName)
	print(f"minutia time: {time.time()-t}")
	
	t = time.time()
	data = matchResults(fileName, dataset, threshold)
	print(f"match results: {time.time()-t}")
	
	
	deleteMinutia(fileName)
	if(type(img2) != str):
		os.remove(fileName)

	subjects = {}
	for i in data:
		subject = i[1]
		if(subject in subjects):
			subjects[subject] = max(i[2], subjects[subject])
		else:
			subjects[subject] = i[2]

	return sum(subjects.values())


#print(score('/home/jupyter/Notebooks/philip/MasterPrint/spoof_print_hidden2_1200.png', 'optical', 30))