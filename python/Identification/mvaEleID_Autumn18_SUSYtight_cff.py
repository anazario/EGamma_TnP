import FWCore.ParameterSet.Config as cms
from RecoEgamma.ElectronIdentification.Identification.mvaElectronID_tools import *

EleMVA_SUSYtight18 = [
    "pt >= 5. && pt < 10. && abs(superCluster.eta) < 0.800",
    "pt >= 5. && pt < 10. && abs(superCluster.eta) >= 0.800 && abs(superCluster.eta) < 1.479",
    "pt >= 5. && pt < 10. && abs(superCluster.eta) >= 1.479 && abs(superCluster.eta) < 2.5",
    "pt >= 10. && pt < 25 && abs(superCluster.eta) < 0.800",
    "pt >= 10. && pt < 25 && abs(superCluster.eta) >= 0.800 && abs(superCluster.eta) < 1.479",
    "pt >= 10. && pt < 25 && abs(superCluster.eta) >= 1.479 && abs(superCluster.eta) < 2.5",
    "pt >= 25. && abs(superCluster.eta) < 0.800",
    "pt >= 25. && abs(superCluster.eta) >= 0.800 && abs(superCluster.eta) < 1.479",
    "pt >= 25. && abs(superCluster.eta) >= 1.479 && abs(superCluster.eta) < 2.5",
    ]

mvaTag = "Fall17NoIsoV2"

idNameSUSYtight = "mvaEleID-Autumn18-SUSYtight"
MVA_SUSYtight = EleMVA_WP(
    idName = idNameSUSYtight, mvaTag = mvaTag,
    cutCategory0 = "tanh(1.320)",
    cutCategory1 = "tanh(0.192)",
    cutCategory2 = "tanh(0.362)",
    cutCategory3 = "tanh(4.277 + 0.112*(pt - 25.))",
    cutCategory4 = "tanh(3.152 + 0.060*(pt - 25.))",
    cutCategory5 = "tanh(2.359 + 0.087*(pt - 25.))",
    cutCategory6 = "tanh(4.277)",
    cutCategory7 = "tanh(3.152)",
    cutCategory8 = "tanh(2.359)",
)

mvaEleID_Autumn18_SUSYtight_config = cms.PSet(
    mvaName             = cms.string(mvaClassName),
    mvaTag              = cms.string(mvaTag),
    # Category parameters
    nCategories         = cms.int32(6),
    categoryCuts        = cms.vstring(*EleMVA_SUSYtight18),
    # Weight files and variable definitions
    #weightFileNames     = mvaFall17WeightFiles_V1,
    variableDefinition  = cms.string(mvaVariablesFile)
    )

mvaEleID_Autumn18_SUSYtight = configureVIDMVAEleID(MVA_SUSYtight)

mvaEleID_Autumn18_SUSYtight.isPOGApproved = cms.untracked.bool(True)
