# Instructions

Make private MC or nanoAOD based on ProjectMetis. This branch contains the setup and instructions for the X --> Y(γγ)H(bb) analysis.

## Setup
```bash
git clone git@github.com:cmstas/privateMC_gen.git
cd privateMC_gen/
git checkout XtoYH_privNanoAODProd

source /cvmfs/cms.cern.ch/cmsset_default.sh
export SCRAM_ARCH=slc7_amd64_gcc700
cmsrel CMSSW_10_6_27
cd CMSSW_10_6_27/src
cmsenv
git cms-init
git remote add cmstas git@github.com:cmstas/cmssw.git
git fetch cmstas
git checkout CMSSW_10_6_27_customNanoAODv9WithPhotonVariables
git cms-addpkg DataFormats/NanoAOD PhysicsTools/NanoAOD
scram b -j 8
cd -

git clone git@github.com:aminnj/ProjectMetis.git
```

## Usage
```bash
source setup.sh
```

### Private NanoAOD production (v9 + Hgg-related variables)
```bash
python mini2nanoAOD_XtoYH.py --tag <tag>
```

The command above prepares and submits condor jobs for the samples included in the `dsdefs_miniaod_UL_XtoYH.py` file. The local files in there can be skipped with the `--skip_local` option and the central files can be skipped with the `--skip_central` option. Further selection can be achieved with the `--filter` (for years/eras/data/MC) and the `--dsfilter` (for dataset names).

For the submission to condor, a tar package is prepared. To skip the packaging, the `--soft_rerun` can be used.

### Private MC production

Instructions to be added soon.

