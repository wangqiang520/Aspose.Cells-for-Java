# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

#if __name__ == "__main__":
#    print "Hello World"

from quickstart import HelloWorld
import jpype
import os.path

asposeapispath = os.path.join(os.path.abspath("./"), "lib/")
dataDir = os.path.join(os.path.abspath("./"), "tests/")

print "You need to put your Aspose.Cells for Java APIs .jars in this folder:\n"+asposeapispath

#print dataDir
jpype.startJVM(jpype.getDefaultJVMPath(), "-Djava.ext.dirs=%s" % asposeapispath)

hw = HelloWorld(dataDir)
hw.main()