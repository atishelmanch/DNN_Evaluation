import FWCore.ParameterSet.Config as cms

process = cms.PSet()

process.ioFilesOpt = cms.PSet(

    ##input files
    inputFiles = cms.vstring(
      #  '/afs/cern.ch/work/a/atishelm/private/HHWWgg_DNN/CMSSW_10_6_8/src/DNN_Evaluation/Evaluation/ggF_SM_WWgg_qqlnugg_Hadded_evalDNN.root'
       '/afs/cern.ch/work/a/atishelm/public/ForJosh/2017_DataMC_ntuples_moreVars/Signal/ggF_SM_WWgg_qqlnugg_Hadded_WithTaus.root'
      #  '/afs/cern.ch/work/a/atishelm/public/ForJosh/2017_DataMC_ntuples_moreVars/Backgrounds/DYJetsToLL_M-50_TuneCP5_13TeV-amcatnloFXFX-pythia8_Hadded.root',
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
   #  outputDir = cms.string('/eos/user/b/bmarzocc/HHWWgg/2017_DataMC_ntuples_moreVars/HHWWyyDNN_binary_basictraining_Tag_0_1/'),
    outputDir = cms.string('/afs/cern.ch/work/a/atishelm/private/HHWWgg_DNN/CMSSW_10_6_8/src/DNN_Evaluation/Evaluation/'),
    
    ##input DNN
    inputModel = cms.string('/afs/cern.ch/work/j/jthomasw/public/forBadder/HHWWyy_networkfiles/HHWWyyDNN_binary_basictraining_Tag_0_1.pb'),
    inputParams = cms.vstring('dense_1_input:0','dense_6/Sigmoid:0'),   
    inputVars = cms.vstring(
       'goodJets_1_pt',
       'Leading_Photon_MVA',
       'goodMuons_0_E', 
       'goodJets_0_E',
       'Subleading_Photon_E',
       'Leading_Photon_pt',
       'goodJets_1_eta', 
       'goodJets_1_phi', 
       'Subleading_Photon_eta', 
       'goodMuons_0_eta',    
       'Subleading_Photon_pt', 
       'goodJets_0_pt',   
       'goodJets_1_E', 
       'Subleading_Photon_phi', 
       'goodMuons_0_pt',     
       'N_goodJets', 
       'goodJets_0_phi',  
       'goodElectrons_0_eta', 
       'Leading_Photon_phi', 
       'Subleading_Photon_MVA', 
       'goodJets_1_bDiscriminator_mini_pfDeepFlavourJetTags_probb', 
       'goodJets_0_bDiscriminator_mini_pfDeepFlavourJetTags_probb', 
       'goodElectrons_0_phi', 
       'Leading_Photon_E', 
       'goodMuons_0_phi', 
       'goodJets_0_eta', 
       'Leading_Photon_eta', 
       'goodElectrons_0_pt', 
       'goodElectrons_0_E'
    ) 

)   
