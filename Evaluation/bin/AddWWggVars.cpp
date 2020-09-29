/////////////////////////////////////////////////////////////////////////////////////////////////////////
// Abraham Tishelman-Charny                                                                            //
// 29 September 2020                                                                                   //
//                                                                                                     //
// The purpose of this module is to add variables to existing ntuples from existing branch variables.  //
// For example, creating a new variable "N_LooseLeptons" from lepton variables                         //
/////////////////////////////////////////////////////////////////////////////////////////////////////////

#include "FWCore/ParameterSet/interface/ParameterSet.h"
#include "FWCore/ParameterSetReader/interface/ParameterSetReader.h"
#include "PhysicsTools/Utilities/macros/setTDRStyle.C"
#include "FWCore/ServiceRegistry/interface/Service.h"
#include "CommonTools/UtilAlgos/interface/TFileService.h"
#include "FWCore/Framework/interface/MakerMacros.h"
#include "FWCore/Utilities/interface/InputTag.h"

#include "TFile.h"
#include "TTree.h"
#include "TROOT.h"
#include "TChain.h"
#include "TGraphErrors.h"
#include "TH1F.h"
#include "TH2F.h"
#include "TCanvas.h"
#include "TVector2.h"
#include "TMath.h"
#include "TLegend.h"
#include "TEfficiency.h"
#include "TProfile.h"
#include "TStyle.h"
#include "TTreeReader.h"
#include <algorithm> 
#include <iostream>
#include <utility>

using namespace std;

void SplitString(const std::string& str, vector<string>& cont, char delim = ' ')
{
    std::stringstream ss(str);
    std::string token;
    while (std::getline(ss, token, delim)) {
        cont.push_back(token);
    }
}

vector<string> ListTrees(TDirectory* dir)
{
    vector<string> names;
    TIter next(dir->GetListOfKeys());
    TObject* object = 0;
    while ((object = next())){
           names.push_back(string(object->GetName()));
    }
    return names;
}

void SetTree(TTree* tree, vector<float>* branchVals, vector<TBranch*>* branchRefs, vector<string>* inputVars)
{

   size_t nBranches = tree->GetListOfBranches()->GetEntries();
   branchVals->resize(inputVars->size());
   branchRefs->resize(inputVars->size()); 

   for(unsigned int iVar = 0; iVar < inputVars->size(); ++iVar)
   {
       for(size_t i = 0; i < nBranches; ++i)
       {
           TBranch *br =dynamic_cast<TBranch*>(tree->GetListOfBranches()->At(i));
           if(string(br->GetName()) == inputVars->at(iVar)) tree->SetBranchAddress(br->GetName(), &branchVals->at(iVar), &branchRefs->at(iVar)); 
       }
   }

}

int main(int argc, char** argv)
{
   const edm::ParameterSet &process         = edm::readPSetsFrom( argv[1] )->getParameter<edm::ParameterSet>( "process" );
   const edm::ParameterSet &filesOpt        = process.getParameter<edm::ParameterSet>( "ioFilesOpt" );
    
   // config inputs
   vector<string> inputFiles_ = filesOpt.getParameter<vector<string>>( "inputFiles" );
   string inputDir_           = filesOpt.getParameter<string>( "inputDir" );
   string outputDir_          = filesOpt.getParameter<string>( "outputDir" );
   vector<string> inputVars_   = filesOpt.getParameter<vector<string>>( "inputVars" );
   vector<string> newVar_Cuts_     = filesOpt.getParameter<vector<string>>( "newVar_Cuts" );

   // New Variables
   int N_looseElectrons = -999;
   int N_looseMuons = -999; 
   int N_looseJets = -999;

   for(unsigned int iFile=0; iFile<inputFiles_.size(); iFile++)
   {
       TFile* inFile = TFile::Open(inputFiles_.at(iFile).c_str());
       TDirectory* dir =(TDirectory*)inFile->Get(inputDir_.c_str());
       vector<string> categories_ = ListTrees(dir);

       vector<string> split_str;
       SplitString(inputFiles_.at(iFile), split_str, '/');
       
       TFile* outFile = new TFile((outputDir_+split_str.at(split_str.size()-1)).c_str(),"recreate");
       outFile->cd();

       for(unsigned int iCat=0; iCat<categories_.size(); iCat++)
       { 
           if(!inFile->Get((inputDir_+"/"+categories_.at(iCat)).c_str())){
              std::cout << "WARNING ----> NOT FOUND: " << (inputDir_+"/"+categories_.at(iCat)).c_str() << std::endl;         
              continue;
           }

           TTree* inTree = (TTree*)inFile->Get((inputDir_+"/"+categories_.at(iCat)).c_str());
           TTree* copyTree = (TTree*)inTree->CopyTree("");
           copyTree->SetName(categories_.at(iCat).c_str());
           copyTree->SetTitle(categories_.at(iCat).c_str());

           vector<float> branchVals; 
           vector<TBranch*> branchRefs;
           SetTree(copyTree, &branchVals, &branchRefs, &inputVars_);
           TBranch * N_looseElectrons_Branch = copyTree->Branch("N_looseElectrons", &N_looseElectrons, "N_looseElectrons/I");
           TBranch * N_looseMuons_Branch = copyTree->Branch("N_looseMuons", &N_looseMuons, "N_looseMuons/I");
           TBranch * N_looseJets_Branch = copyTree->Branch("N_looseJets", &N_looseJets, "N_looseJets/I");
           
           for(int entry = 0; entry < copyTree->GetEntries(); entry++)
           {  
                if(entry%1000==0) std::cout << "--- Reading " << categories_.at(iCat).c_str() << " = " << entry << std::endl;
                copyTree->GetEntry(entry);

                // This is done in a very bad way because I'm not sure how to do this properly in c++...
                // I guess you could map each variable string to the input var iterator, but then how do you evaluate?
                // at the moment I'm just printing the string in python and pasting here. 
                N_looseElectrons = ( (branchVals[0] >= 10) && (branchVals[1]==1) && (fabs(branchVals[2])<1.4442 || (fabs(branchVals[2])>1.566 && fabs(branchVals[2])<2.5) ) )+( (branchVals[9] >= 10) && (branchVals[10]==1) && (fabs(branchVals[11])<1.4442 || (fabs(branchVals[11])>1.566 && fabs(branchVals[11])<2.5) ) )+( (branchVals[18] >= 10) && (branchVals[19]==1) && (fabs(branchVals[20])<1.4442 || (fabs(branchVals[20])>1.566 && fabs(branchVals[20])<2.5) ) )+( (branchVals[27] >= 10) && (branchVals[28]==1) && (fabs(branchVals[29])<1.4442 || (fabs(branchVals[29])>1.566 && fabs(branchVals[29])<2.5) ) )+( (branchVals[36] >= 10) && (branchVals[37]==1) && (fabs(branchVals[38])<1.4442 || (fabs(branchVals[38])>1.566 && fabs(branchVals[38])<2.5) ) );
                N_looseMuons =  ( (branchVals[3] >= 10) && (branchVals[4]==1) && (fabs(branchVals[5]) <= 2.4 ))+( (branchVals[12] >= 10) && (branchVals[13]==1) && (fabs(branchVals[14]) <= 2.4 ))+( (branchVals[21] >= 10) && (branchVals[22]==1) && (fabs(branchVals[23]) <= 2.4 ))+( (branchVals[30] >= 10) && (branchVals[31]==1) && (fabs(branchVals[32]) <= 2.4 ))+( (branchVals[39] >= 10) && (branchVals[40]==1) && (fabs(branchVals[41]) <= 2.4 ));
                N_looseJets = ( (branchVals[6]>25) && (branchVals[7]==1) && fabs(branchVals[8]) <= 2.4)+( (branchVals[15]>25) && (branchVals[16]==1) && fabs(branchVals[17]) <= 2.4)+( (branchVals[24]>25) && (branchVals[25]==1) && fabs(branchVals[26]) <= 2.4)+( (branchVals[33]>25) && (branchVals[34]==1) && fabs(branchVals[35]) <= 2.4)+( (branchVals[42]>25) && (branchVals[43]==1) && fabs(branchVals[44]) <= 2.4);
                N_looseElectrons_Branch->Fill();
                N_looseMuons_Branch->Fill(); 
                N_looseJets_Branch->Fill();

           }
       }
       outFile->Write("",outFile->kOverwrite);
       outFile->Close(); 
   }

}

