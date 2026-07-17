import cowsay
import sys

if len(sys.argv) == 2:
    #cowsay.cow("Hello " + sys.argv[1])
    #cowsay.dragon("Hello " + sys.argv[1])
    cowsay.tux("Hello " + sys.argv[1])
    cowsay.daemon("Hello " + sys.argv[1])