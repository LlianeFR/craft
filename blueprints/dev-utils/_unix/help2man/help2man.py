import info


class subinfo( info.infoclass ):
    def setTargets( self ):
        for ver in ["1.47.6"]:
            self.targets[ ver ] = f"http://mirror.netcologne.de/gnu/help2man/help2man-{ver}.tar.xz"
            self.targetInstSrc[ ver ] = f"help2man-{ver}"
            self.targetInstallPath[ver] = "dev-utils"

        self.description = "help2man produces simple manual pages from the ‘--help’ and ‘--version’ output of other commands."
        self.defaultTarget = "1.47.6"

    def setDependencies( self ):
        self.runtimeDependencies["virtual/base"] = "default"
        self.buildDependencies["dev-utils/autoconf"] = "default"

from Package.AutoToolsPackageBase import *

class Package( AutoToolsPackageBase ):
    def __init__( self ):
        AutoToolsPackageBase.__init__( self )
        self.subinfo.options.configure.autoreconf = False
        self.subinfo.options.configure.args += " --disable-static --enable-shared "

