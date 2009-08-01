import base
import os
import utils
import info
import shutil

class subinfo(info.infoclass):
    def setTargets( self ):
        """ """
        self.targets['5.1.36-1'] = """
http://downloads.sourceforge.net/kde-windows/mysql-server-5.1.36-1-bin.tar.bz2
http://downloads.sourceforge.net/kde-windows/mysql-server-5.1.36-1-lib.tar.bz2
"""
        self.targetInstSrc['5.1.36-1'] = ""
        self.defaultTarget = '5.1.36-1'

    def setDependencies( self ):
        """ """
        self.hardDependencies['gnuwin32/wget'] = 'default'
        
class subclass(base.baseclass):
    def __init__( self, **args ):
        base.baseclass.__init__( self, args=args )
        self.subinfo = subinfo()

if __name__ == '__main__':
    subclass().execute()
