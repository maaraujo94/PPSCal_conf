# hltGetConfiguration /users/maaraujo/HLT_11/HLT_PPS_Kin/V2 --input file:/eos/user/m/maaraujo/HLT_work/HLT_rem_319639/066AD206-A487-E811-A6D5-FA163E5E2735.root --setup /dev/CMSSW_11_2_0/GRun/V9 --data --max-events -1 --unprescale --l1 L1Menu_Collisions2018_v1_0_0-d1_xml --globaltag 112X_dataRun2_v3 --output none --customise HLTrigger/Configuration/customizeHLTforCMSSW.synchronizeHCALHLTofflineRun3on2018data

# /users/maaraujo/HLT_11/HLT_PPS_Kin/V2 (CMSSW_11_2_0_pre5)

import FWCore.ParameterSet.Config as cms

process = cms.Process( "HLTX" )
process.load("setup_dev_CMSSW_11_2_0_GRun_V9_cff")

process.HLTConfigVersion = cms.PSet(
  tableName = cms.string('/users/maaraujo/HLT_11/HLT_PPS_Kin/V2')
)

process.XMLIdealGeometryESSource_CTPPS = cms.ESProducer( "XMLIdealGeometryESProducer",
  rootDDName = cms.string( "cms:CMSE" ),
  label = cms.string( "CTPPS" ),
  appendToDataLabel = cms.string( "XMLIdealGeometryESSource_CTPPS" )
)
process.CTPPSGeometryESModule = cms.ESProducer( "CTPPSGeometryESModule",
  verbosity = cms.untracked.uint32( 1 ),
  compactViewTag = cms.string( "XMLIdealGeometryESSource_CTPPS" )
)
process.ctppsInterpolatedOpticalFunctionsESSource = cms.ESProducer( "CTPPSInterpolatedOpticalFunctionsESSource",
  appendToDataLabel = cms.string( "" ),
  lhcInfoLabel = cms.string( "" ),
  opticsLabel = cms.string( "" )
)

process.hltGetConditions = cms.EDAnalyzer( "EventSetupRecordDataGetter",
    toGet = cms.VPSet( 
    ),
    verbose = cms.untracked.bool( False )
)
process.hltGetRaw = cms.EDAnalyzer( "HLTGetRaw",
    RawDataCollection = cms.InputTag( "rawDataCollector" )
)
process.hltPSetMap = cms.EDProducer( "ParameterSetBlobProducer" )
process.hltBoolFalse = cms.EDFilter( "HLTBool",
    result = cms.bool( False )
)
process.hltTriggerType = cms.EDFilter( "HLTTriggerTypeFilter",
    SelectedTriggerType = cms.int32( 1 )
)
process.hltGtStage2Digis = cms.EDProducer( "L1TRawToDigi",
    lenSlinkTrailer = cms.untracked.int32( 8 ),
    lenAMC13Header = cms.untracked.int32( 8 ),
    CTP7 = cms.untracked.bool( False ),
    lenAMC13Trailer = cms.untracked.int32( 8 ),
    Setup = cms.string( "stage2::GTSetup" ),
    MinFeds = cms.uint32( 0 ),
    InputLabel = cms.InputTag( "rawDataCollector" ),
    lenSlinkHeader = cms.untracked.int32( 8 ),
    MTF7 = cms.untracked.bool( False ),
    FWId = cms.uint32( 0 ),
    TMTCheck = cms.bool( True ),
    lenAMCTrailer = cms.untracked.int32( 0 ),
    debug = cms.untracked.bool( False ),
    FedIds = cms.vint32( 1404 ),
    lenAMCHeader = cms.untracked.int32( 8 ),
    DmxFWId = cms.uint32( 0 ),
    FWOverride = cms.bool( False )
)
process.hltGtStage2ObjectMap = cms.EDProducer( "L1TGlobalProducer",
    L1DataBxInEvent = cms.int32( 5 ),
    AlgorithmTriggersUnmasked = cms.bool( True ),
    EtSumInputTag = cms.InputTag( 'hltGtStage2Digis','EtSum' ),
    BstLengthBytes = cms.int32( -1 ),
    MuonInputTag = cms.InputTag( 'hltGtStage2Digis','Muon' ),
    AlgorithmTriggersUnprescaled = cms.bool( True ),
    AlternativeNrBxBoardDaq = cms.uint32( 0 ),
    JetInputTag = cms.InputTag( 'hltGtStage2Digis','Jet' ),
    EmulateBxInEvent = cms.int32( 1 ),
    Verbosity = cms.untracked.int32( 0 ),
    ProduceL1GtDaqRecord = cms.bool( True ),
    TriggerMenuLuminosity = cms.string( "startup" ),
    PrescaleCSVFile = cms.string( "prescale_L1TGlobal.csv" ),
    PrintL1Menu = cms.untracked.bool( False ),
    ExtInputTag = cms.InputTag( "hltGtStage2Digis" ),
    AlgoBlkInputTag = cms.InputTag( "hltGtStage2Digis" ),
    PrescaleSet = cms.uint32( 1 ),
    EGammaInputTag = cms.InputTag( 'hltGtStage2Digis','EGamma' ),
    ProduceL1GtObjectMapRecord = cms.bool( True ),
    GetPrescaleColumnFromData = cms.bool( False ),
    TauInputTag = cms.InputTag( 'hltGtStage2Digis','Tau' )
)
process.hltScalersRawToDigi = cms.EDProducer( "ScalersRawToDigi",
    scalersInputTag = cms.InputTag( "rawDataCollector" )
)
process.hltOnlineBeamSpot = cms.EDProducer( "BeamSpotOnlineProducer",
    maxZ = cms.double( 40.0 ),
    src = cms.InputTag( "hltScalersRawToDigi" ),
    gtEvmLabel = cms.InputTag( "" ),
    changeToCMSCoordinates = cms.bool( False ),
    setSigmaZ = cms.double( 0.0 ),
    maxRadius = cms.double( 2.0 )
)
process.hltL1sZeroBias = cms.EDFilter( "HLTL1TSeed",
    L1SeedsLogicalExpression = cms.string( "L1_ZeroBias" ),
    L1EGammaInputTag = cms.InputTag( 'hltGtStage2Digis','EGamma' ),
    L1JetInputTag = cms.InputTag( 'hltGtStage2Digis','Jet' ),
    saveTags = cms.bool( True ),
    L1ObjectMapInputTag = cms.InputTag( "hltGtStage2ObjectMap" ),
    L1EtSumInputTag = cms.InputTag( 'hltGtStage2Digis','EtSum' ),
    L1TauInputTag = cms.InputTag( 'hltGtStage2Digis','Tau' ),
    L1MuonInputTag = cms.InputTag( 'hltGtStage2Digis','Muon' ),
    L1GlobalInputTag = cms.InputTag( "hltGtStage2Digis" )
)
process.hltPreCTPPSFilter = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "hltGtStage2Digis" ),
    offset = cms.uint32( 0 )
)
process.ctppsPixelDigis = cms.EDProducer( "CTPPSPixelRawToDigi",
    mappingLabel = cms.string( "RPix" ),
    inputLabel = cms.InputTag( "rawDataCollector" ),
    includeErrors = cms.bool( True )
)
process.ctppsPixelClusters = cms.EDProducer( "CTPPSPixelClusterProducer",
    ADCThreshold = cms.int32( 2 ),
    ElectronADCGain = cms.double( 135.0 ),
    SeedADCThreshold = cms.int32( 2 ),
    VCaltoElectronGain = cms.int32( 50 ),
    RPixVerbosity = cms.untracked.int32( 0 ),
    VCaltoElectronOffset = cms.int32( -411 ),
    label = cms.string( "ctppsPixelDigis" ),
    doSingleCalibration = cms.bool( False )
)
process.ctppsPixelRecHits = cms.EDProducer( "CTPPSPixelRecHitProducer",
    RPixVerbosity = cms.untracked.int32( 0 ),
    RPixClusterTag = cms.InputTag( "ctppsPixelClusters" )
)
process.ctppsPixelLocalTracks = cms.EDProducer( "CTPPSPixelLocalTrackProducer",
    maximumXLocalDistanceFromTrack = cms.double( 0.2 ),
    maxHitPerRomanPot = cms.int32( 60 ),
    maxTrackPerPattern = cms.int32( 5 ),
    trackFinderAlgorithm = cms.string( "RPixPlaneCombinatoryTracking" ),
    minRoadSize = cms.int32( 3 ),
    trackMinNumberOfPoints = cms.uint32( 3 ),
    roadRadius = cms.double( 1.0 ),
    label = cms.string( "ctppsPixelRecHits" ),
    numberOfPlanesPerPot = cms.int32( 6 ),
    maxTrackPerRomanPot = cms.int32( 10 ),
    maximumYLocalDistanceFromTrack = cms.double( 0.3 ),
    maxHitPerPlane = cms.int32( 20 ),
    maximumChi2OverNDF = cms.double( 5.0 ),
    patternFinderAlgorithm = cms.string( "RPixRoadFinder" ),
    maxRoadSize = cms.int32( 20 ),
    verbosity = cms.untracked.int32( 0 )
)
process.HLTPPSCalFilter = cms.EDFilter( "HLTPPSCalFilter",
    pixelLocalTrackInputTag = cms.InputTag( "ctppsPixelLocalTracks" ),
    stripLocalTrackInputTag = cms.InputTag( "totemRPLocalTrackFilter" ),
    diamondLocalTrackInputTag = cms.InputTag( "ctppsDiamondLocalTracks" ),
    minTracks = cms.int32( 1 ),
    maxTracks = cms.int32( 1 ),
    do_express = cms.bool( True )
)
process.hltBoolEnd = cms.EDFilter( "HLTBool",
    result = cms.bool( True )
)
process.hltFEDSelector = cms.EDProducer( "EvFFEDSelector",
    inputTag = cms.InputTag( "rawDataCollector" ),
    fedList = cms.vuint32( 1023, 1024 )
)
process.hltTriggerSummaryAOD = cms.EDProducer( "TriggerSummaryProducerAOD",
    moduleLabelPatternsToSkip = cms.vstring(  ),
    processName = cms.string( "@" ),
    throw = cms.bool( False ),
    moduleLabelPatternsToMatch = cms.vstring( 'hlt*' )
)
process.hltTriggerSummaryRAW = cms.EDProducer( "TriggerSummaryProducerRAW",
    processName = cms.string( "@" )
)

process.HLTL1UnpackerSequence = cms.Sequence( process.hltGtStage2Digis + process.hltGtStage2ObjectMap )
process.HLTBeamSpot = cms.Sequence( process.hltScalersRawToDigi + process.hltOnlineBeamSpot )
process.HLTBeginSequence = cms.Sequence( process.hltTriggerType + process.HLTL1UnpackerSequence + process.HLTBeamSpot )
process.HLTEndSequence = cms.Sequence( process.hltBoolEnd )

process.HLTriggerFirstPath = cms.Path( process.hltGetConditions + process.hltGetRaw + process.hltPSetMap + process.hltBoolFalse )
process.HLT_CTPPSFilter_v2 = cms.Path( process.HLTBeginSequence + process.hltL1sZeroBias + process.hltPreCTPPSFilter + process.ctppsPixelDigis + process.ctppsPixelClusters + process.ctppsPixelRecHits + process.ctppsPixelLocalTracks + process.HLTPPSCalFilter + process.HLTEndSequence )
process.HLTriggerFinalPath = cms.Path( process.hltGtStage2Digis + process.hltScalersRawToDigi + process.hltFEDSelector + process.hltTriggerSummaryAOD + process.hltTriggerSummaryRAW + process.hltBoolFalse )


process.HLTSchedule = cms.Schedule( *(process.HLTriggerFirstPath, process.HLT_CTPPSFilter_v2, process.HLTriggerFinalPath ))


from list_cff import inputFileNames
process.source = cms.Source("PoolSource",
    fileNames = cms.untracked.vstring(inputFileNames),
    inputCommands = cms.untracked.vstring('keep *'),
    duplicateCheckMode = cms.untracked.string("noDuplicateCheck")
)
import FWCore.PythonUtilities.LumiList as LumiList
process.source.lumisToProcess = LumiList.LumiList(filename = 'goodlist.json').getVLuminosityBlockRange()


# avoid PrescaleService error due to missing HLT paths
if 'PrescaleService' in process.__dict__:
    for pset in reversed(process.PrescaleService.prescaleTable):
        if not hasattr(process,pset.pathName.value()):
            process.PrescaleService.prescaleTable.remove(pset)

# limit the number of events to be processed
process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32( -1 )
)

# enable TrigReport, TimeReport and MultiThreading
process.options = cms.untracked.PSet(
    wantSummary = cms.untracked.bool( True ),
    numberOfThreads = cms.untracked.uint32( 4 ),
    numberOfStreams = cms.untracked.uint32( 0 ),
    sizeOfStackForThreadsInKB = cms.untracked.uint32( 10*1024 )
)

# override the GlobalTag, connection string and pfnPrefix
if 'GlobalTag' in process.__dict__:
    from Configuration.AlCa.GlobalTag import GlobalTag as customiseGlobalTag
    process.GlobalTag = customiseGlobalTag(process.GlobalTag, globaltag = '112X_dataRun2_v5', conditions = 'L1Menu_Collisions2018_v2_1_0-d1_xml,L1TUtmTriggerMenuRcd,,,9999-12-31 23:59:59.000')

if 'MessageLogger' in process.__dict__:
    process.MessageLogger.categories.append('TriggerSummaryProducerAOD')
    process.MessageLogger.categories.append('L1GtTrigReport')
    process.MessageLogger.categories.append('L1TGlobalSummary')
    process.MessageLogger.categories.append('HLTrigReport')
    process.MessageLogger.categories.append('FastReport')

# load the DQMStore and DQMRootOutputModule
process.load( "DQMServices.Core.DQMStore_cfi" )

process.dqmOutput = cms.OutputModule("DQMRootOutputModule",
    fileName = cms.untracked.string("DQMIO.root")
)

process.DQMOutput = cms.EndPath( process.dqmOutput )

# add specific customizations
_customInfo = {}
_customInfo['menuType'  ]= "GRun"
_customInfo['globalTags']= {}
_customInfo['globalTags'][True ] = "auto:run3_hlt_GRun"
_customInfo['globalTags'][False] = "auto:run3_mc_GRun"
_customInfo['inputFiles']={}
_customInfo['inputFiles'][True]  = "file:RelVal_Raw_GRun_DATA.root"
_customInfo['inputFiles'][False] = "file:RelVal_Raw_GRun_MC.root"
_customInfo['maxEvents' ]=  -1
_customInfo['globalTag' ]= "112X_dataRun2_v5"
_customInfo['inputFile' ]=  inputFileNames
_customInfo['realData'  ]=  True
from HLTrigger.Configuration.customizeHLTforALL import customizeHLTforAll
process = customizeHLTforAll(process,"GRun",_customInfo)

from HLTrigger.Configuration.customizeHLTforCMSSW import customizeHLTforCMSSW
process = customizeHLTforCMSSW(process,"GRun")

# Eras-based customisations
from HLTrigger.Configuration.Eras import modifyHLTforEras
modifyHLTforEras(process)

#User-defined customization functions
from HLTrigger.Configuration.customizeHLTforCMSSW import customisePixelGainForRun2Input
process = customisePixelGainForRun2Input(process)

from HLTrigger.Configuration.customizeHLTforCMSSW import synchronizeHCALHLTofflineRun3on2018data
process = synchronizeHCALHLTofflineRun3on2018data(process)

