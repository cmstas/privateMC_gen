import sys, os
import time
import itertools
import numpy
import json

from metis.Sample import DBSSample, DirectorySample, Sample
from metis.CondorTask import CondorTask
from metis.StatsParser import StatsParser

import argparse
parser = argparse.ArgumentParser()
parser.add_argument("--tag", help = "tag to identify this set of babies", type=str)
parser.add_argument("--filter", help = "only process mc/data with some requirement (e.g. 2016MC, 2017Data)", default="", type=str)
parser.add_argument("--dsfilter", help = "only process mc/data with some name pattern(e.g. DY***)", default="", type=str)
parser.add_argument("--soft_rerun", help = "don't remake tarball", action="store_true")
parser.add_argument("--skip_local", help = "don't submit jobs for local samples", action = "store_true")
parser.add_argument("--skip_central", help = "don't submit jobs for central samples", action = "store_true")
args = parser.parse_args()

# for central inputs
#dsdefs = []
## datasetname, filesPerOutput, filtername
from dsdefs_centralminiaod_UL import dsdefs
# for local inputs
local_sets = []


if not args.skip_local:
    local_sets = [
#        ("HHggtautau_Era2018_private", "/hadoop/cms/store/user/hmei/miniaod_runII/HHggtautau_2018_20201002_v1_STEP4_v1/", 10, "2018MC"),
#        ("HHggtautau_Era2017_private", "/hadoop/cms/store/user/hmei/miniaod_runII/HHggtautau_2017_20201025_v1_STEP4_v1/", 10, "2017MC")
#        ("HHggtautau_Era2016_private", "/hadoop/cms/store/user/hmei/miniaod_runII/HHggtautau_2016_20201124_v1_STEP4_v1/", 10, "2016MC")
#        ("HHggZZ_Era2016_private", "/hadoop/cms/store/user/hmei/miniaod_runII/HHggZZ_2016_20210209_v1_STEP4_v1/", 10, "2016MC"),
#        ("HHggZZ_Era2017_private", "/hadoop/cms/store/user/hmei/miniaod_runII/HHggZZ_2017_20210209_v1_STEP4_v1/", 10, "2017MC"),
#        ("HHggZZ_Era2018_private", "/hadoop/cms/store/user/hmei/miniaod_runII/HHggZZ_2018_20210209_v1_STEP4_v1/", 10, "2018MC")
        # vbf
        ("VBF_CV_0_5_C2V_1_C3_1_HHggtautau_Era2016_private", "/hadoop/cms/store/user/fsetti/nanoAOD_runII/VBF_CV_0_5_C2V_1_C3_1_HHggtautau_2016_20210425_v1_STEP4_v1/", 10, "2016MC"),
        ("VBF_CV_1_5_C2V_1_C3_1_HHggtautau_Era2016_private", "/hadoop/cms/store/user/fsetti/nanoAOD_runII/VBF_CV_1_5_C2V_1_C3_1_HHggtautau_2016_20210420_v1_STEP4_v1/", 10, "2016MC"),
        ("VBF_CV_1_C2V_1_C3_0_HHggtautau_Era2016_private", "/hadoop/cms/store/user/fsetti/nanoAOD_runII/VBF_CV_1_C2V_1_C3_0_HHggtautau_2016_20210425_v1_STEP4_v1/", 10, "2016MC"),
        ("VBF_CV_1_C2V_1_C3_2_HHggtautau_Era2016_private", "/hadoop/cms/store/user/fsetti/nanoAOD_runII/VBF_CV_1_C2V_1_C3_2_HHggtautau_2016_20210425_v1_STEP4_v1/", 10, "2016MC"),
        ("VBF_CV_1_C2V_1_C3_1_HHggtautau_Era2016_private", "/hadoop/cms/store/user/fsetti/nanoAOD_runII/VBF_CV_1_C2V_1_C3_1_HHggtautau_2016_20210420_v1_STEP4_v1/", 10, "2016MC"),
        ("VBF_CV_1_C2V_1_C3_1_HHggtautau_Era2016_private", "/hadoop/cms/store/user/fsetti/nanoAOD_runII/VBF_CV_1_C2V_0_C3_1_HHggtautau_2016_20210420_v1_STEP4_v1/", 10, "2016MC"),
        ("VBF_CV_1_C2V_1_C3_1_HHggtautau_Era2016_private", "/hadoop/cms/store/user/fsetti/nanoAOD_runII/VBF_CV_1_C2V_2_C3_1_HHggtautau_2016_20210420_v1_STEP4_v1/", 10, "2016MC"),
        ("VBF_CV_0_5_C2V_1_C3_1_HHggtautau_Era2017_private", "/hadoop/cms/store/user/fsetti/nanoAOD_runII/VBF_CV_0_5_C2V_1_C3_1_HHggtautau_2017_20210425_v1_STEP4_v1/", 10, "2017MC"),
        ("VBF_CV_1_5_C2V_1_C3_1_HHggtautau_Era2017_private", "/hadoop/cms/store/user/fsetti/nanoAOD_runII/VBF_CV_1_5_C2V_1_C3_1_HHggtautau_2017_20210420_v1_STEP4_v1/", 10, "2017MC"),
        ("VBF_CV_1_C2V_1_C3_0_HHggtautau_Era2017_private", "/hadoop/cms/store/user/fsetti/nanoAOD_runII/VBF_CV_1_C2V_1_C3_0_HHggtautau_2017_20210425_v1_STEP4_v1/", 10, "2017MC"),
        ("VBF_CV_1_C2V_1_C3_2_HHggtautau_Era2017_private", "/hadoop/cms/store/user/fsetti/nanoAOD_runII/VBF_CV_1_C2V_1_C3_2_HHggtautau_2017_20210425_v1_STEP4_v1/", 10, "2017MC"),
        ("VBF_CV_1_C2V_1_C3_1_HHggtautau_Era2017_private", "/hadoop/cms/store/user/fsetti/nanoAOD_runII/VBF_CV_1_C2V_1_C3_1_HHggtautau_2017_20210420_v1_STEP4_v1/", 10, "2017MC"),
        ("VBF_CV_1_C2V_1_C3_1_HHggtautau_Era2017_private", "/hadoop/cms/store/user/fsetti/nanoAOD_runII/VBF_CV_1_C2V_0_C3_1_HHggtautau_2017_20210420_v1_STEP4_v1/", 10, "2017MC"),
        ("VBF_CV_1_C2V_1_C3_1_HHggtautau_Era2017_private", "/hadoop/cms/store/user/fsetti/nanoAOD_runII/VBF_CV_1_C2V_2_C3_1_HHggtautau_2017_20210420_v1_STEP4_v1/", 10, "2017MC"),
        ("VBF_CV_0_5_C2V_1_C3_1_HHggtautau_Era2018_private", "/hadoop/cms/store/user/fsetti/nanoAOD_runII/VBF_CV_0_5_C2V_1_C3_1_HHggtautau_2018_20210425_v1_STEP4_v1/", 10, "2018MC"),
        ("VBF_CV_1_5_C2V_1_C3_1_HHggtautau_Era2018_private", "/hadoop/cms/store/user/fsetti/nanoAOD_runII/VBF_CV_1_5_C2V_1_C3_1_HHggtautau_2018_20210420_v1_STEP4_v1/", 10, "2018MC"),
        ("VBF_CV_1_C2V_1_C3_0_HHggtautau_Era2018_private", "/hadoop/cms/store/user/fsetti/nanoAOD_runII/VBF_CV_1_C2V_1_C3_0_HHggtautau_2018_20210425_v1_STEP4_v1/", 10, "2018MC"),
        ("VBF_CV_1_C2V_1_C3_2_HHggtautau_Era2018_private", "/hadoop/cms/store/user/fsetti/nanoAOD_runII/VBF_CV_1_C2V_1_C3_2_HHggtautau_2018_20210425_v1_STEP4_v1/", 10, "2018MC"),
        ("VBF_CV_1_C2V_1_C3_1_HHggtautau_Era2018_private", "/hadoop/cms/store/user/fsetti/nanoAOD_runII/VBF_CV_1_C2V_1_C3_1_HHggtautau_2018_20210420_v1_STEP4_v1/", 10, "2018MC"),
        ("VBF_CV_1_C2V_1_C3_1_HHggtautau_Era2018_private", "/hadoop/cms/store/user/fsetti/nanoAOD_runII/VBF_CV_1_C2V_2_C3_1_HHggtautau_2018_20210420_v1_STEP4_v1/", 10, "2018MC"),
        ("VBF_CV_1_C2V_1_C3_1_HHggtautau_Era2018_private", "/hadoop/cms/store/user/fsetti/nanoAOD_runII/VBF_CV_1_C2V_0_C3_1_HHggtautau_2018_20210420_v1_STEP4_v1/", 10, "2018MC"),
        ## resonant
        ("radionM300_HHggtautau_Era2017_private", "/hadoop/cms/store/user/hmei/nanoAOD_runII/res_Radion_M300_HHggtautau_2017_20210422_v1_STEP4_v1/", 10, "2017MC"),
        ("radionM400_HHggtautau_Era2017_private", "/hadoop/cms/store/user/hmei/nanoAOD_runII/res_Radion_M400_HHggtautau_2017_20210422_v1_STEP4_v1/", 10, "2017MC"),
        ("radionM500_HHggtautau_Era2017_private", "/hadoop/cms/store/user/hmei/nanoAOD_runII/res_Radion_M500_HHggtautau_2017_20210422_v1_STEP4_v1/", 10, "2017MC"),
        ("radionM800_HHggtautau_Era2017_private", "/hadoop/cms/store/user/hmei/nanoAOD_runII/res_Radion_M800_HHggtautau_2017_20210422_v1_STEP4_v1/", 10, "2017MC"),
        ("radionM1000_HHggtautau_Era2017_private", "/hadoop/cms/store/user/hmei/nanoAOD_runII/res_Radion_M1000_HHggtautau_2017_20210422_v1_STEP4_v1/", 10, "2017MC"),
        ("radionM300_HHggtautau_Era2018_private", "/hadoop/cms/store/user/hmei/nanoAOD_runII/res_Radion_M300_HHggtautau_2018_20210422_v1_STEP4_v1/", 10, "2018MC"),
        ("radionM400_HHggtautau_Era2018_private", "/hadoop/cms/store/user/hmei/nanoAOD_runII/res_Radion_M400_HHggtautau_2018_20210422_v1_STEP4_v1/", 10, "2018MC"),
        ("radionM500_HHggtautau_Era2018_private", "/hadoop/cms/store/user/hmei/nanoAOD_runII/res_Radion_M500_HHggtautau_2018_20210422_v1_STEP4_v1/", 10, "2018MC"),
        ("radionM800_HHggtautau_Era2018_private", "/hadoop/cms/store/user/hmei/nanoAOD_runII/res_Radion_M800_HHggtautau_2018_20210422_v1_STEP4_v1/", 10, "2018MC"),
        ("radionM1000_HHggtautau_Era2018_private", "/hadoop/cms/store/user/hmei/nanoAOD_runII/res_Radion_M1000_HHggtautau_2018_20210422_v1_STEP4_v1/", 10, "2018MC")
    ]

# some job configurations
job_dir = "nanoaod_runII/HHggtautau/"
job_tag = args.tag
job_filter = args.filter
ds_filter = args.dsfilter
skip_central = args.skip_central
hadoop_path = "{0}".format(job_dir)

#cmssw_ver = "CMSSW_10_2_22"
cmssw_ver = "CMSSW_10_6_20"

DOSKIM = False 

#exec_path = "condor_exe_%s.sh" % args.tag
exec_path = "condor_exe.sh"
#tar_path = "nanoAOD_package_%s.tar.gz" % args.tag

if not args.soft_rerun:
#    os.system("rm -rf tasks/*" + args.tag + "*")
    os.system("rm package.tar.gz")
    os.system("XZ_OPT='-3e -T24' tar -Jc --exclude='.git' --exclude='*.root' --exclude='*.tar*' --exclude='*.out' --exclude='*.err' --exclude='*.log' --exclude '*.nfs*' -f package.tar.gz %s" % cmssw_ver)

    #os.system("cp package.tar.gz /hadoop/cms/store/user/smay/FCNC/tarballs/%s" % tar_path)
    #os.system("hadoop fs -setrep -R 30 /cms/store/user/smay/FCNC/tarballs/%s" % tar_path)

total_summary = {}
while True:
    allcomplete = True

    # Loop through central samples
    for ds,fpo,args in dsdefs[:]:
        if skip_central: continue
        if (job_filter != "") and (args not in job_filter) : continue         
        if (ds_filter != "") and (ds_filter not in ds) : continue         
        sample = DBSSample( dataset=ds )
        print(ds, args)

        task = CondorTask(
                sample = sample,
                open_dataset = False,
                files_per_output = fpo,
                output_name = "test_nanoaod.root",
                tag = job_tag,
        	cmssw_version = cmssw_ver,
                executable = exec_path,
                tarfile = "./package.tar.gz",
                condor_submit_params = {"sites" : "T2_US_UCSD",
                    #"classads": [["SingularityImage","/cvmfs/singularity.opensciencegrid.org/cmssw/cms:rhel6-m202006"]]},
                    "classads": [["SingularityImage","/cvmfs/singularity.opensciencegrid.org/cmssw/cms:rhel7-m202006"]]},
                    #"SingularityImage":"/cvmfs/singularity.opensciencegrid.org/cmssw/cms:rhel6-m202006"},
                #condor_submit_params = {"sites" : "T2_US_UCSD,T2_US_CALTECH,T2_US_MIT,T2_US_WISCONSIN,T2_US_Nebraska,T2_US_Purdue,T2_US_Vanderbilt,T2_US_Florida"},
                special_dir = hadoop_path,
                arguments = args.replace(" ","|")
                )
        task.process()
        allcomplete = allcomplete and task.complete()
        # save some information for the dashboard
        total_summary[ds] = task.get_task_summary()
        with open("summary.json", "w") as f_out:
            json.dump(total_summary, f_out, indent=4, sort_keys=True)

    # Loop through local samples
    for ds,loc,fpo,args in local_sets[:]:
        sample = DirectorySample( dataset = ds, location = loc )
        files = [f.name for f in sample.get_files()]
        print "For sample %s in directory %s, there are %d input files" % (ds, loc, len(files))
        #for file in files:
        #    print file

        task = CondorTask(
                sample = sample,
                open_dataset = True,
                files_per_output = fpo,
                output_name = "test_nanoaod.root",
                tag = job_tag,
                cmssw_version = cmssw_ver,
                executable = exec_path,
                tarfile = "./package.tar.gz",
                condor_submit_params = {"sites" : "T2_US_UCSD",
                    #"classads": [["SingularityImage","/cvmfs/singularity.opensciencegrid.org/cmssw/cms:rhel6-m202006"]]},
                    "classads": [["SingularityImage","/cvmfs/singularity.opensciencegrid.org/cmssw/cms:rhel7-m202006"]]},
                special_dir = hadoop_path,
                arguments = args.replace(" ","|")
        )
        task.process()
        allcomplete = allcomplete and task.complete()
        # save some information for the dashboard
        total_summary[ds] = task.get_task_summary()
        with open("summary.json", "w") as f_out:
            json.dump(total_summary, f_out, indent=4, sort_keys=True)


    # parse the total summary and write out the dashboard
    StatsParser(data=total_summary, webdir="~/public_html/dump/metis_nanoaod_v8/").do()
    os.system("chmod -R 755 ~/public_html/dump/metis_nanoaod_v8")
    if allcomplete:
        print ""
        print "Job={} finished".format(job_tag)
        print ""
        break
    print "Sleeping 1000 seconds ..."
    time.sleep(1000)
