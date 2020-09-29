import FWCore.ParameterSet.Config as cms

##-- Electrons, Muons, Jets: Keep all analysis selections except dR, pT
electronCuts = ""
muonCuts = ""
jetCuts = ""
maxObjects = 5

lepton_pt_cut = 10 
jet_pt_cut = 25 
## Define New Variables Pythonically 
for i in range(0,maxObjects): # info for 5 first electrons, muons, jets saved 
    elec, muon, jet = "allElectrons_%s"%(i), "allMuons_%s"%(i), "allJets_%s"%(i)
    electronCuts += "( (%s_pt >= %s) && (%s_passLooseId==1) && (fabs(%s_eta)<1.4442 || (fabs(%s_eta)>1.566 && fabs(%s_eta)<2.5) ) )"%(elec,lepton_pt_cut,elec,elec,elec,elec)
    muonCuts += "( (%s_pt >= %s) && (%s_isTightMuon==1) && (fabs(%s_eta) <= 2.4 ))"%(muon,lepton_pt_cut,muon,muon)
    jetCuts += "( (%s_pt>%s) && (%s_passTight2017==1) && fabs(%s_eta) <= 2.4)"%(jet,jet_pt_cut,jet,jet)     

    if(i != maxObjects-1): # if not the last object, multiply by next selection
        electronCuts += "+"
        muonCuts += "+"
        jetCuts += "+"

N_looseElectrons_cut = "%s"%(electronCuts)
N_looseMuons_cut = "%s"%(muonCuts)
N_looseJets_cut = "%s"%(jetCuts)

## Input vars necessary to compute new vars 
requiredVars = [] 
elecVars = ['pt','passLooseId','eta']
muonVars = ['pt','isTightMuon','eta'] 
jetVars = ['pt','passTight2017','eta']
for i in range(0,maxObjects):
    elec, muon, jet = "allElectrons_%s"%(i), "allMuons_%s"%(i), "allJets_%s"%(i)
    for eVar in elecVars:
      var = "%s_%s"%(elec,eVar)
      requiredVars.append(var)
    for muVar in muonVars:
      var = "%s_%s"%(muon,muVar)
      requiredVars.append(var)     
    for jetVar in jetVars:
      var = "%s_%s"%(jet,jetVar)
      requiredVars.append(var)

for i,requiredVar in enumerate(requiredVars):
  N_looseElectrons_cut = N_looseElectrons_cut.replace(requiredVar,"branchVals[%s]"%(i))
  N_looseMuons_cut = N_looseMuons_cut.replace(requiredVar,"branchVals[%s]"%(i))
  N_looseJets_cut = N_looseJets_cut.replace(requiredVar,"branchVals[%s]"%(i))

print "N_looseElectrons_cut:",N_looseElectrons_cut
print "N_looseMuons_cut:",N_looseMuons_cut
print "N_looseJets_cut:",N_looseJets_cut

process = cms.PSet()

process.ioFilesOpt = cms.PSet(

    ##input files
    inputFiles = cms.vstring(
      #  '/afs/cern.ch/work/a/atishelm/public/ForJosh/2017_DataMC_ntuples_moreVars/Signal/ggF_SM_WWgg_qqlnugg_Hadded_WithTaus.root'
       '/afs/cern.ch/work/a/atishelm/public/ForJosh/2017_DataMC_ntuples_moreVars/Backgrounds/DYJetsToLL_M-50_TuneCP5_13TeV-amcatnloFXFX-pythia8_Hadded.root',
      #  '/afs/cern.ch/work/a/atishelm/public/ForJosh/2017_DataMC_ntuples_moreVars/Backgrounds/DiPhotonJetsBox_M40_80-Sherpa_Hadded.root',
      #  '/afs/cern.ch/work/a/atishelm/public/ForJosh/2017_DataMC_ntuples_moreVars/Backgrounds/DiPhotonJetsBox_MGG-80toInf_13TeV-Sherpa_Hadded.root',
      #  '/afs/cern.ch/work/a/atishelm/public/ForJosh/2017_DataMC_ntuples_moreVars/Backgrounds/GJet_Pt-20to40_DoubleEMEnriched_MGG-80toInf_TuneCP5_13TeV_Pythia8_Hadded.root',
      #  '/afs/cern.ch/work/a/atishelm/public/ForJosh/2017_DataMC_ntuples_moreVars/Backgrounds/GJet_Pt-20toInf_DoubleEMEnriched_MGG-40to80_TuneCP5_13TeV_Pythia8_Hadded.root',
      #  '/afs/cern.ch/work/a/atishelm/public/ForJosh/2017_DataMC_ntuples_moreVars/Backgrounds/GJet_Pt-40toInf_DoubleEMEnriched_MGG-80toInf_TuneCP5_13TeV_Pythia8_Hadded.root',
      #  '/afs/cern.ch/work/a/atishelm/public/ForJosh/2017_DataMC_ntuples_moreVars/Backgrounds/GluGluHToGG_M125_13TeV_amcatnloFXFX_pythia8_Hadded.root',
      #  '/afs/cern.ch/work/a/atishelm/public/ForJosh/2017_DataMC_ntuples_moreVars/Backgrounds/QCD_Pt-30to40_DoubleEMEnriched_MGG-80toInf_TuneCP5_13TeV_Pythia8_Hadded.root',
      #  '/afs/cern.ch/work/a/atishelm/public/ForJosh/2017_DataMC_ntuples_moreVars/Backgrounds/QCD_Pt-30toInf_DoubleEMEnriched_MGG-40to80_TuneCP5_13TeV_Pythia8_Hadded.root',
      #  '/afs/cern.ch/work/a/atishelm/public/ForJosh/2017_DataMC_ntuples_moreVars/Backgrounds/QCD_Pt-40toInf_DoubleEMEnriched_MGG-80toInf_TuneCP5_13TeV_Pythia8_Hadded.root',
      #  '/afs/cern.ch/work/a/atishelm/public/ForJosh/2017_DataMC_ntuples_moreVars/Backgrounds/THQ_ctcvcp_HToGG_M125_13TeV-madgraph-pythia8_TuneCP5_Hadded.root',
      #  '/afs/cern.ch/work/a/atishelm/public/ForJosh/2017_DataMC_ntuples_moreVars/Backgrounds/TTGG_0Jets_TuneCP5_13TeV_amcatnlo_madspin_pythia8_Hadded.root',
      #  '/afs/cern.ch/work/a/atishelm/public/ForJosh/2017_DataMC_ntuples_moreVars/Backgrounds/TTGJets_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8_Hadded.root',
      #  '/afs/cern.ch/work/a/atishelm/public/ForJosh/2017_DataMC_ntuples_moreVars/Backgrounds/TTJets_HT-1200to2500_TuneCP5_13TeV-madgraphMLM-pythia8_Hadded.root',
      #  '/afs/cern.ch/work/a/atishelm/public/ForJosh/2017_DataMC_ntuples_moreVars/Backgrounds/TTJets_HT-2500toInf_TuneCP5_13TeV-madgraphMLM-pythia8_Hadded.root',
      #  '/afs/cern.ch/work/a/atishelm/public/ForJosh/2017_DataMC_ntuples_moreVars/Backgrounds/TTJets_HT-600to800_TuneCP5_13TeV-madgraphMLM-pythia8_Hadded.root',
      #  '/afs/cern.ch/work/a/atishelm/public/ForJosh/2017_DataMC_ntuples_moreVars/Backgrounds/TTJets_HT-800to1200_TuneCP5_13TeV-madgraphMLM-pythia8_Hadded.root',
      #  '/afs/cern.ch/work/a/atishelm/public/ForJosh/2017_DataMC_ntuples_moreVars/Backgrounds/TTToHadronic_TuneCP5_13TeV-powheg-pythia8_Hadded.root',
      #  '/afs/cern.ch/work/a/atishelm/public/ForJosh/2017_DataMC_ntuples_moreVars/Backgrounds/VBFHToGG_M-125_13TeV_powheg_pythia8_Hadded.root',
      #  '/afs/cern.ch/work/a/atishelm/public/ForJosh/2017_DataMC_ntuples_moreVars/Backgrounds/VHToGG_M125_13TeV_amcatnloFXFX_madspin_pythia8_Hadded.root',
      #  '/afs/cern.ch/work/a/atishelm/public/ForJosh/2017_DataMC_ntuples_moreVars/Backgrounds/W1JetsToLNu_LHEWpT_0-50_TuneCP5_13TeV-amcnloFXFX-pythia8_Hadded.root',
      #  '/afs/cern.ch/work/a/atishelm/public/ForJosh/2017_DataMC_ntuples_moreVars/Backgrounds/W1JetsToLNu_LHEWpT_150-250_TuneCP5_13TeV-amcnloFXFX-pythia8_Hadded.root',
      #  '/afs/cern.ch/work/a/atishelm/public/ForJosh/2017_DataMC_ntuples_moreVars/Backgrounds/W1JetsToLNu_LHEWpT_250-400_TuneCP5_13TeV-amcnloFXFX-pythia8_Hadded.root',
      #  '/afs/cern.ch/work/a/atishelm/public/ForJosh/2017_DataMC_ntuples_moreVars/Backgrounds/W1JetsToLNu_LHEWpT_400-inf_TuneCP5_13TeV-amcnloFXFX-pythia8_Hadded.root',
      #  '/afs/cern.ch/work/a/atishelm/public/ForJosh/2017_DataMC_ntuples_moreVars/Backgrounds/W1JetsToLNu_LHEWpT_50-150_TuneCP5_13TeV-amcnloFXFX-pythia8_Hadded.root',
      #  '/afs/cern.ch/work/a/atishelm/public/ForJosh/2017_DataMC_ntuples_moreVars/Backgrounds/W2JetsToLNu_LHEWpT_0-50_TuneCP5_13TeV-amcnloFXFX-pythia8_Hadded.root',
      #  '/afs/cern.ch/work/a/atishelm/public/ForJosh/2017_DataMC_ntuples_moreVars/Backgrounds/W2JetsToLNu_LHEWpT_150-250_TuneCP5_13TeV-amcnloFXFX-pythia8_Hadded.root',
      #  '/afs/cern.ch/work/a/atishelm/public/ForJosh/2017_DataMC_ntuples_moreVars/Backgrounds/W2JetsToLNu_LHEWpT_250-400_TuneCP5_13TeV-amcnloFXFX-pythia8_Hadded.root',
      #  '/afs/cern.ch/work/a/atishelm/public/ForJosh/2017_DataMC_ntuples_moreVars/Backgrounds/W2JetsToLNu_LHEWpT_400-inf_TuneCP5_13TeV-amcnloFXFX-pythia8_Hadded.root',
      #  '/afs/cern.ch/work/a/atishelm/public/ForJosh/2017_DataMC_ntuples_moreVars/Backgrounds/W2JetsToLNu_LHEWpT_50-150_TuneCP5_13TeV-amcnloFXFX-pythia8_Hadded.root',
      #  '/afs/cern.ch/work/a/atishelm/public/ForJosh/2017_DataMC_ntuples_moreVars/Backgrounds/W3JetsToLNu_TuneCP5_13TeV-madgraphMLM-pythia8_Hadded.root',
      #  '/afs/cern.ch/work/a/atishelm/public/ForJosh/2017_DataMC_ntuples_moreVars/Backgrounds/W4JetsToLNu_TuneCP5_13TeV-madgraphMLM-pythia8_Hadded.root',
      #  '/afs/cern.ch/work/a/atishelm/public/ForJosh/2017_DataMC_ntuples_moreVars/Backgrounds/WGGJets_TuneCP5_13TeV_madgraphMLM_pythia8_Hadded.root',
      #  '/afs/cern.ch/work/a/atishelm/public/ForJosh/2017_DataMC_ntuples_moreVars/Backgrounds/WGJJToLNuGJJ_EWK_aQGC-FS-FM_TuneCP5_13TeV-madgraph-pythia8.root',
      #  '/afs/cern.ch/work/a/atishelm/public/ForJosh/2017_DataMC_ntuples_moreVars/Backgrounds/WWTo1L1Nu2Q_13TeV_amcatnloFXFX_madspin_pythia8_Hadded.root',
      #  '/afs/cern.ch/work/a/atishelm/public/ForJosh/2017_DataMC_ntuples_moreVars/Backgrounds/WW_TuneCP5_13TeV-pythia8_Hadded.root',
      #  '/afs/cern.ch/work/a/atishelm/public/ForJosh/2017_DataMC_ntuples_moreVars/Backgrounds/ttHJetToGG_M125_13TeV_amcatnloFXFX_madspin_pythia8_Hadded.root',
      #  '/afs/cern.ch/work/a/atishelm/public/ForJosh/2017_DataMC_ntuples_moreVars/Backgrounds/ttWJets_TuneCP5_13TeV_madgraphMLM_pythia8_Hadded.root',
      #  '/afs/cern.ch/work/a/atishelm/public/ForJosh/2017_DataMC_ntuples_moreVars/Data/Data.root'
    ),
    inputDir = cms.string('tagsDumper/trees'), 
    outputDir = cms.string('/eos/user/a/atishelm/ntuples/HHWWgg_DataMC/DNN_addVars/'),
    inputVars = cms.vstring(
      requiredVars

    ),

    newVar_Cuts = cms.vstring(
      N_looseElectrons_cut,
      N_looseMuons_cut
    )

)   
