from earsketch import *

volumeEffect = initEffect('basicVolume')

track = createUGen(volumeEffect, INPUT)
multiply = createUGen(volumeEffect, TIMES)
out = createUGen(volumeEffect, OUTPUT)

connect(volumeEffect, track, multiply)
connect(volumeEffect, multiply, out)

setParam(multiply, VALUE, 0.5)

finishEffect(volumeEffect)
