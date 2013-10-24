from earsketch import *

init()
setTempo(140)

reverbEffect = initEffect('reverb')

input = createUGen(reverbEffect, INPUT)
output = createUGen(reverbEffect, OUTPUT)

connect(reverbEffect, input, output)

finishEffect(reverbEffect)

finish()

