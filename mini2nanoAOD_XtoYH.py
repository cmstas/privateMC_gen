import sys, os
import time
import itertools
import json

from metis.Sample import DBSSample, DirectorySample, Sample
from metis.CondorTask import CondorTask
#from LocalNanoAODMergeTask import LocalNanoAODMergeTask
from metis.StatsParser import StatsParser

import argparse
parser = argparse.ArgumentParser()
parser.add_argument("--tag", help = "tag to identify this set of babies", type=str)
parser.add_argument("--filter", help = "only process mc/data with some requirement (e.g. 2016MC, 2017Data)", default="", type=str)
parser.add_argument("--dsfilter", help = "only process mc/data with some name pattern(e.g. DY***)", default="", type=str)
parser.add_argument("--soft_rerun", help = "don't remake tarball", action="store_true")
parser.add_argument("--skip_local", help = "don't submit jobs for local samples", action = "store_true")
parser.add_argument("--skip_central", help = "don't submit jobs for central samples", action = "store_true")
parser.add_argument("--localcp", help = "first copy the file, then run on it, rather than remote accessing it", action = "store_true")
args = parser.parse_args()

user = os.environ.get("USER")

from dsdefs_miniaod_UL_XtoYH import *

# some job configurations
job_dir = "XtoYH_customNanoAOD/"
job_tag = args.tag
job_filter = args.filter
ds_filter = args.dsfilter
skip_local = args.skip_local
skip_central = args.skip_central
ceph_path = "{0}".format(job_dir)
merged_dir = "/ceph/cms/store/user/{}/{}/".format(user,ceph_path)

cmssw_ver = "CMSSW_10_6_27"

exec_path = "condor_exe_XtoYH.sh"

if not args.soft_rerun:
    os.system("cp cmsDrivers/miniToNanoAOD_201* CMSSW_10_6_27/src/.")
    os.system("rm package.tar.gz")
    os.system("XZ_OPT='-3e -T24' tar -Jc --exclude='.git' --exclude='*.root' --exclude='*.tar*' --exclude='*.out' --exclude='*.err' --exclude='*.log' --exclude '*.nfs*' -f package.tar.gz %s" % cmssw_ver)

total_summary = {}
dsdefs = dsdefs_data + dsdefs_signal + dsdefs_bkg
# Loop through samples
for ds,loc,fpo,arguments in dsdefs[:]:
  if (job_filter != "") and (arguments not in job_filter) : continue
  if (ds_filter != "") and (ds_filter not in ds) : continue

  if loc != None:
    if skip_local: continue
    sample = DirectorySample( dataset = ds, location = loc )
  else:
    if skip_central: continue
    sample = DBSSample( dataset=ds )
  print(ds, arguments)

  task = CondorTask(
    sample = sample,
    open_dataset = True,
    files_per_output = fpo,
    output_name = "nanoaod.root",
    tag = job_tag,
    cmssw_version = cmssw_ver,
    scram_arch = "slc7_amd64_gcc700",
    executable = exec_path,
    tarfile = "package.tar.gz",
    condor_submit_params = {"sites": "T2_US_UCSD,T2_US_CALTECH,T2_US_WISCONSIN,T2_US_Florida", # other_sites can be good_sites, your own list, etc.
        "classads": [["SingularityImage","/cvmfs/singularity.opensciencegrid.org/cmssw/cms:rhel7-m202006"]]},
    special_dir = ceph_path,
    arguments = arguments.replace(" ","|")+("|LOCAL" if args.localcp else "")
  )

  if not task.complete():
    task.process()
  total_summary[ds] = task.get_task_summary()

# Parse the summary and make a summary.txt that will be used to pretty status of the jobs
os.system("rm -f web_summary.json")
os.system("rm -f summary.json")
webdir="~/public_html/customNanoAODDashboard"
StatsParser(data=total_summary, webdir=webdir).do()
os.system("chmod -R 755 {}".format(webdir))
os.system("msummary -r -i {}/web_summary.json".format(webdir))
