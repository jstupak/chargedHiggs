# Left-Right symmetric model WR (m=1500) production with subsequent decay
# through the chain e Ne -> e e jet jet
# Heavy neutrino Ne mass = 600 GeV, others very heavy

import FWCore.ParameterSet.Config as cms

process = cms.Process("PROD")

process.load("Configuration.StandardSequences.SimulationRandomNumberGeneratorSeeds_cff")

process.source = cms.Source("EmptySource")

process.generator = cms.EDFilter("Pythia8GeneratorFilter",
    maxEventsToPrint = cms.untracked.int32(1),
    pythiaPylistVerbosity = cms.untracked.int32(1),
    filterEfficiency = cms.untracked.double(1.0),
    pythiaHepMCVerbosity = cms.untracked.bool(False),
    comEnergy = cms.double(8000.),
    PythiaParameters = cms.PSet(processParameters=cms.vstring('Higgs:useBSM = on',
                                'HiggsHchg:coup2H1W = 0.0',
                                '25:m0 = 125.',
                                '35:m0 = 279.',
                                '36:m0 = 280.',
                                '37:m0 = 280.',
                                'HiggsHchg:tanBeta = 30',
                                #'HiggsBSM:allH+- = on',
                                'HiggsBSM:bg2H+-t  = on',
                                '37:onMode = 0',
                                '37:onIfAny = 6'),
                                parameterSets = cms.vstring('processParameters')
                                 )
)

process.MessageLogger = cms.Service("MessageLogger",
    cout = cms.untracked.PSet(
        default = cms.untracked.PSet(
            limit = cms.untracked.int32(0)
        )
    ),
    destinations = cms.untracked.vstring('cout')
)

#from random import random
#process.RandomNumberGeneratorService = cms.Service("RandomNumberGeneratorService",
#    moduleSeeds = cms.PSet(
#        generator = cms.untracked.uint32(int(1E6*random())),
#        g4SimHits = cms.untracked.uint32(int(1E8*random())),
#        VtxSmeared = cms.untracked.uint32(int(1E8*random()))
#    ),
#)

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(100)
)

process.GEN = cms.OutputModule("PoolOutputModule",
    fileName = cms.untracked.string('pythia8_ChargedHigstoTB.root')
)

process.p = cms.Path(process.generator)
process.outpath = cms.EndPath(process.GEN)

process.schedule = cms.Schedule(process.p, process.outpath)

