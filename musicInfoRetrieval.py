# Will finish later today 10/25/13

from earsketch import *

init()
tempo(120)

trackMusicOne = MUSIC_LOOP_001
trackMusicTwo = MUSIC_LOOP_002

start = 1
end = 3

fitMedia(trackMusicOne, 1, start, end)
fitMedia(trackMusicTwo, 2, start, end)

analysisMethod = RMS_AMPLITUDE
one = 0.0625
RMS_Threshold = 0.35

location = start
if (location < end):
  RMS_val = analyzeTrackForTime(1, analysisMethod, location, location + hop)
  if RMS_val < RMS_Threshold:
    setEffect(2, VOLUME, GAIN, -60, location, -60, location + one)
  else:
    setEffect(2, VOLUME, GAIN, 0, location, 0, location + one)
  location += one
  
finish()
