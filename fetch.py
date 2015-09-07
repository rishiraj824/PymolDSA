import pymol
import urllib

    #retreive file name and url from database when particular Protein is selected

file1 = "3NXY.pdb"	
	
urllib.urlretrieve ("http://www.rcsb.org/pdb/download/downloadFile.do?fileFormat=pdb&compression=NO&structureId=3NXY", "file1")

pymol.finish_launching()

cmd.load("file1")
