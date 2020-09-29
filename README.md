# DNN_Evaluation

1) Install:

    * scram project CMSSW_10_5_X # or CMSSW_10_6_X or inside any Flashgg CMSSW release
    * cd CMSSW_10_5_X/src/
    * cmsenv
    * git clone https://github.com/bmarzocc/DNN_Evaluation
    * scram b -j 

2) Run: set parameters in python/Evaluate_WWggDNN.py

    * cd DNN_Evaluation/Evaluation
    * cmsenv
    * Evaluate_WWggDNN python/Evaluate_WWggDNN.py
   
# AddWWggVars

To add variables to existing ntuples, run very similar steps to DNN evaluation:

1) Install: 

    * scram project CMSSW_10_5_X # or CMSSW_10_6_X or inside any Flashgg CMSSW release
    * cd CMSSW_10_5_X/src/
    * cmsenv
    * git clone https://github.com/bmarzocc/DNN_Evaluation
    * scram b -j

2) Run: Set Parameters in python/AddWWggVars.py

    * cd DNN_Evaluation/Evaluation
    * cmsenv
    * AddWWggVars python/AddWWggVars.py