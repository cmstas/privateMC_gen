dsdefs_data = [
# 2016
  ("/DoubleEG/Run2016B-ver1_HIPM_UL2016_MiniAODv2-v1/MINIAOD", None , 1, "2016APV_Data"),
  ("/DoubleEG/Run2016B-ver2_HIPM_UL2016_MiniAODv2-v3/MINIAOD", None , 1, "2016APV_Data"),
  ("/DoubleEG/Run2016C-HIPM_UL2016_MiniAODv2-v1/MINIAOD", None, 1, "2016APV_Data"),
  ("/DoubleEG/Run2016D-HIPM_UL2016_MiniAODv2-v1/MINIAOD", None, 1, "2016APV_Data"),
  ("/DoubleEG/Run2016E-HIPM_UL2016_MiniAODv2-v1/MINIAOD", None, 1, "2016APV_Data"),
  ("/DoubleEG/Run2016F-HIPM_UL2016_MiniAODv2-v1/MINIAOD", None, 1, "2016APV_Data"),
  ("/DoubleEG/Run2016F-UL2016_MiniAODv2-v1/MINIAOD", None, 1, "2016_Data"),
  ("/DoubleEG/Run2016G-UL2016_MiniAODv2-v1/MINIAOD", None, 1, "2016_Data"),
  ("/DoubleEG/Run2016H-UL2016_MiniAODv2-v1/MINIAOD", None, 1, "2016_Data"),
# 2017
  ("/DoubleEG/Run2017B-UL2017_MiniAODv2-v1/MINIAOD", None, 1, "2017_Data"),
  ("/DoubleEG/Run2017C-UL2017_MiniAODv2-v2/MINIAOD", None, 1, "2017_Data"),
  ("/DoubleEG/Run2017D-UL2017_MiniAODv2-v1/MINIAOD", None, 1, "2017_Data"),
  ("/DoubleEG/Run2017E-UL2017_MiniAODv2-v1/MINIAOD", None, 1, "2017_Data"),
  ("/DoubleEG/Run2017F-UL2017_MiniAODv2-v2/MINIAOD", None, 1, "2017_Data"),
# 2018
  ("/EGamma/Run2018A-UL2018_MiniAODv2_GT36-v1/MINIAOD", None, 1, "2018_Data"),
  ("/EGamma/Run2018B-UL2018_MiniAODv2_GT36-v1/MINIAOD", None, 1, "2018_Data"),
  ("/EGamma/Run2018C-UL2018_MiniAODv2_GT36-v1/MINIAOD", None, 1, "2018_Data"),
  ("/EGamma/Run2018D-UL2018_MiniAODv2-v2/MINIAOD", None, 1, "2018_Data"),
]
dsdefs_signal = [
# Private
  ("NMSSM_XYH_Y_gg_H_bb_MX_600_MY_90_2017_221227", "/ceph/cms/store/user/evourlio/testCustomNanoAOD/miniAODFiles/", 1, "2017_MC"),
# Central
]

dsdefs_bkg = [
### Non-resonant bkg
# DY
  ("/DYJetsToLL_M-50_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v1/MINIAODSIM", None, 1, "2016APV_MC"),
  ("/DYJetsToLL_M-50_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v1/MINIAODSIM", None, 1, "2016_MC"),
  ("/DYJetsToLL_M-50_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v2/MINIAODSIM", None, 1, "2017_MC"),
  ("/DYJetsToLL_M-50_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2/MINIAODSIM", None, 1, "2018_MC"),

#Diphoton
  ("/DiPhotonJetsBox_MGG-80toInf_13TeV-sherpa/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v2/MINIAODSIM", None, 1, "2016APV_MC"),
  ("/DiPhotonJetsBox_MGG-80toInf_13TeV-sherpa/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v2/MINIAODSIM", None, 1, "2016_MC"),
  ("/DiPhotonJetsBox_MGG-80toInf_13TeV-sherpa/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v2/MINIAODSIM", None, 1, "2017_MC"),
  ("/DiPhotonJetsBox_MGG-80toInf_13TeV-sherpa/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2/MINIAODSIM", None, 1, "2018_MC"),

#GJets
  ("/GJets_HT-40To100_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v1/MINIAODSIM", None, 1, "2016APV_MC"),
  ("/GJets_HT-40To100_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v1/MINIAODSIM", None, 1, "2016_MC"),
  ("/GJets_HT-40To100_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v2/MINIAODSIM", None, 1, "2017_MC"),
  ("/GJets_HT-40To100_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2/MINIAODSIM", None, 1, "2018_MC"),
#
  ("/GJets_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL16MiniAODAPVv2-4cores5k_106X_mcRun2_asymptotic_preVFP_v11-v1/MINIAODSIM", None, 1, "2016APV_MC"),
  ("/GJets_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL16MiniAODv2-4cores5k_106X_mcRun2_asymptotic_v17-v1/MINIAODSIM", None, 1, "2016_MC"),
  ("/GJets_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL17MiniAODv2-4cores5k_106X_mc2017_realistic_v9-v2/MINIAODSIM", None, 1, "2017_MC"),
  ("/GJets_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL18MiniAODv2-4cores5k_106X_upgrade2018_realistic_v16_L1v1-v2/MINIAODSIM", None, 1, "2018_MC"),
#
  ("/GJets_HT-200To400_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v1/MINIAODSIM", None, 1, "2016APV_MC"),
  ("/GJets_HT-200To400_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v1/MINIAODSIM", None, 1, "2016_MC"),
  ("/GJets_HT-200To400_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v2/MINIAODSIM", None, 1, "2017_MC"),
  ("/GJets_HT-200To400_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2/MINIAODSIM", None, 1, "2018_MC"),
#
  ("/GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v1/MINIAODSIM", None, 1, "2016APV_MC"),
  ("/GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v1/MINIAODSIM", None, 1, "2016_MC"),
  ("/GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v2/MINIAODSIM", None, 1, "2017_MC"),
  ("/GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2/MINIAODSIM", None, 1, "2018_MC"),
#
  ("/GJets_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v1/MINIAODSIM", None, 1, "2016APV_MC"),
  ("/GJets_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v1/MINIAODSIM", None, 1, "2016_MC"),
  ("/GJets_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v2/MINIAODSIM", None, 1, "2017_MC"),
  ("/GJets_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2/MINIAODSIM", None, 1, "2018_MC"),

# TTGG0Jets
  ("/TTGG_0Jets_TuneCP5_13TeV-amcatnlo-madspin-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v1/MINIAODSIM", None, 1, "2016APV_MC"),
  ("/TTGG_0Jets_TuneCP5_13TeV-amcatnlo-madspin-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v1/MINIAODSIM", None, 1, "2016_MC"),
  ("/TTGG_0Jets_TuneCP5_13TeV-amcatnlo-madspin-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v1/MINIAODSIM", None, 1, "2017_MC"),
  ("/TTGG_0Jets_TuneCP5_13TeV-amcatnlo-madspin-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v1/MINIAODSIM", None, 1, "2018_MC"),

# TTGJets
  ("/TTGJets_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v2/MINIAODSIM", None, 1, "2016APV_MC"),
  ("/TTGJets_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v1/MINIAODSIM", None, 1, "2016_MC"),
  ("/TTGJets_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v1/MINIAODSIM", None, 1, "2017_MC"),
  ("/TTGJets_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v1/MINIAODSIM", None, 1, "2018_MC"),

# TTJets
  ("/TTJets_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v1/MINIAODSIM", None, 1, "2016APV_MC"),
  ("/TTJets_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v1/MINIAODSIM", None, 1, "2016_MC"),
  ("/TTJets_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v2/MINIAODSIM", None, 1, "2017_MC"),
  ("/TTJets_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2/MINIAODSIM", None, 1, "2018_MC"),

#WG
  ("/WGToLNuG_01J_5f_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v1/MINIAODSIM", None, 1, "2016APV_MC"),
  ("/WGToLNuG_01J_5f_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v1/MINIAODSIM", None, 1, "2016_MC"),
  ("/WGToLNuG_01J_5f_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v1/MINIAODSIM", None, 1, "2017_MC"),
  ("/WGToLNuG_01J_5f_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v1/MINIAODSIM", None, 1, "2018_MC"),

#ZG
  ("/ZGToLLG_01J_5f_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v1/MINIAODSIM", None, 1, "2016APV_MC"),
  ("/ZGToLLG_01J_5f_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v1/MINIAODSIM", None, 1, "2016_MC"),
  ("/ZGToLLG_01J_5f_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v1/MINIAODSIM", None, 1, "2017_MC"),
  ("/ZGToLLG_01J_5f_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v1/MINIAODSIM", None, 1, "2018_MC"),

## Resonant bkg
# GluGluHToGG_M125
  ("/GluGluHToGG_M125_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v2/MINIAODSIM", None, 1, "2016APV_MC"),
  ("/GluGluHToGG_M125_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v2/MINIAODSIM", None, 1, "2016_MC"),
  ("/GluGluHToGG_M125_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v1/MINIAODSIM", None, 1, "2017_MC"),
  ("/GluGluHToGG_M125_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v1/MINIAODSIM", None, 1, "2018_MC"),

# ttHJetToGG_M125
  ("/ttHJetToGG_M125_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v3/MINIAODSIM", None, 1, "2016APV_MC"),
  ("/ttHJetToGG_M125_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v2/MINIAODSIM", None, 1, "2016_MC"),
  ("/ttHJetToGG_M125_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v2/MINIAODSIM", None, 1, "2017_MC"),
  ("/ttHJetToGG_M125_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2/MINIAODSIM", None, 1, "2018_MC"),

# VBFHToGG_M125
  ("/VBFHToGG_M125_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v2/MINIAODSIM", None, 1, "2016APV_MC"),
  ("/VBFHToGG_M125_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v2/MINIAODSIM", None, 1, "2016_MC"),
  ("/VBFHToGG_M125_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v2/MINIAODSIM", None, 1, "2017_MC"),
  ("/VBFHToGG_M125_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2/MINIAODSIM", None, 1, "2018_MC"),

# VHToGG_M125
  ("/VHToGG_M125_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v1/MINIAODSIM", None, 1, "2016APV_MC"),
  ("/VHToGG_M125_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v2/MINIAODSIM", None, 1, "2016_MC"),
  ("/VHToGG_M125_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v2/MINIAODSIM", None, 1, "2017_MC"),
  ("/VHToGG_M125_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2/MINIAODSIM", None, 1, "2018_MC"),
]
