import info


class subinfo(info.infoclass):
    def setTargets( self ):
        self.svnTargets[ "master" ] = "https://github.com/lukesampson/concfg.git"
        self.targetInstallPath[ "master" ] = "dev-utils/concfg/"
        self.defaultTarget = "master"


    def setDependencies( self ):
        self.dependencies['virtual/base'] = 'default'


from Package.BinaryPackageBase import *

class Package(BinaryPackageBase):
    def __init__( self):
        BinaryPackageBase.__init__(self)

    def unpack(self):
        return True

    def install( self ):
        if not BinaryPackageBase.install(self):
            return False
        utils.createShim(os.path.join(self.imageDir(),"dev-utils","bin","concfg.exe"),
                         utils.utilsCache.findApplication("powershell"),
                         useAbsolutePath=True)
        return True

