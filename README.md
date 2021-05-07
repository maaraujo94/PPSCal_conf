Repository for codes being used in PPS Calibration Trigger studies

HLTPPSCalFilter.cc: The filter code

hlt_example.py: Example configuration which includes a PPS reco sequence followed by the calibration filter. Includes all necessary customizations to run in CMSSW_11_2_X. Requires a list of input files as list_cff.py and an input lumiList as goodlist.json. Ignore hltGetConfiguration options at the top, they are out of date