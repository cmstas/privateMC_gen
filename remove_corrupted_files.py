import os
import sys
import ROOT as r
from glob import glob

check_dir = '/hadoop/cms/store/user/fsetti/nanoAOD_runII_20UL/GluGluToBulkGravitonToHHTo2G2Tau_M5*v2/*.root'

for ifile in glob(check_dir):
	try:
		rfile = r.TFile(ifile)
		nEvents = rfile.Get("Events").GetEntries()
		rfile.Close()
	except:
		os.system("rm {}".format(ifile))
