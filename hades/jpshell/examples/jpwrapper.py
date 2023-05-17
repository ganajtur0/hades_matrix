from jp_design_os import *
from hades.jpshell import JPWrapper

jpw = JPWrapper()
print "1",jpw
muller = jpw.createJPObject("Muller", "Muller", "NORTH")
print "2",muller
#addComponentWithSymbol(muller, Point(3600,3600))
