import info

class subinfo(info.infoclass):
    def setTargets( self ):
        self.svnTargets['gitHEAD'] = '[git]kde:rocs|KDE/4.8|'
        for ver in ['0', '1', '2', '3', '4']:
            self.targets['4.8.' + ver] = "ftp://ftp.kde.org/pub/kde/stable/4.8." + ver + "/src/rocs-4.8." + ver + ".tar.bz2"
            self.targetInstSrc['4.8.' + ver] = 'rocs-4.8.' + ver
        self.patchToApply['4.8'] = [("rocs-4.8.0-20120202.diff", 1)]
        self.shortDescription = 'rocs graph theory'
        self.defaultTarget = 'gitHEAD'

    def setDependencies( self ):
        self.dependencies['kde/kde-runtime'] = 'default'
        self.dependencies['win32libs-bin/boost-graph'] = 'default'

from Package.CMakePackageBase import *

class Package(CMakePackageBase):
    def __init__( self ):
        self.subinfo = subinfo()
        CMakePackageBase.__init__( self )

if __name__ == '__main__':
    Package().execute()
