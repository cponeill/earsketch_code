# Here is some sample code for creating a drum loop

# The first code is written as if there were no loop at all

from earsketch import *

init()
tempo(140)

beat = "0-00-00-0+++0+0+"
drum = BIG_BEAT_DRUM_001

makeBeat(drum, 1, 1, beat)
makeBeat(drum, 1, 2, beat)
makeBeat(drum, 1, 3, beat)

finish()



# This code is written with a "for" loop and is much easier and cleaner

from earsketch import *

init()
tempo(140)

beat = "0-00-00-0+++0+0+"
drum = BIG_BEAT_DRUM_001

from measure in range(1, 3):
  makeBeat(drum, 1, measure, beat)
  
finish()
