# -*- coding: utf-8 -*-
import info

class subinfo(info.infoclass):
    def setTargets( self ):
        self.svnTargets['gitHEAD'] = '[git]kde:kdelibs|KDE/4.7|'
        for ver in ['0', '1', '2', '3', '4']:
            self.targets['4.7.' + ver] = "ftp://ftp.kde.org/pub/kde/stable/4.7." + ver + "/src/kdelibs-4.7." + ver + ".tar.bz2"
            self.targetInstSrc['4.7.' + ver] = 'kdelibs-4.7.' + ver
        self.patchToApply['4.7.0'] = [("kdelibs-4.7.0-20110819.diff", 1) , ("silence_wmi_1.diff" ,1 ) , ("silence_wmi_2.diff" , 1) ]
        self.targetDigests['4.7.0'] = '2a7a59ac78a161c7c2393db89179449b495dd2db'
        self.shortDescription = "The KDE Library"
        self.defaultTarget = 'gitHEAD'


    def setDependencies( self ):
        self.buildDependencies['virtual/base'] = 'default'
        self.buildDependencies['dev-util/perl'] = 'default'
        self.buildDependencies['win32libs-bin/automoc'] = 'default'
        self.dependencies['kdesupport/kdewin'] = 'default'
        self.dependencies['kdesupport/phonon'] = 'default'
        self.dependencies['kdesupport/attica'] = 'default'
        self.dependencies['kdesupport/dbusmenu-qt'] = 'default'
        self.dependencies['kdesupport/qca'] = 'default'
        self.dependencies['kdesupport/qimageblitz'] = 'default'
        self.dependencies['kdesupport/soprano'] = 'default'
        self.dependencies['kdesupport/strigi'] = 'default'
        self.dependencies['virtual/kdelibs-base'] = 'default'
        self.dependencies['data/docbook-dtd'] = 'default'
        self.dependencies['data/docbook-xsl'] = 'default'
        self.dependencies['data/shared-desktop-ontologies'] = 'default'

from Package.CMakePackageBase import *

class Package(CMakePackageBase):
    def __init__( self ):
        self.subinfo = subinfo()
        CMakePackageBase.__init__( self )
        self.subinfo.options.configure.defines = ""
        if self.compiler() == "mingw":
          self.subinfo.options.configure.defines += " -DKDE_DISTRIBUTION_TEXT=\"MinGW 3.4.5\" "
        elif self.compiler() == "mingw4":
          self.subinfo.options.configure.defines += " -DKDE_DISTRIBUTION_TEXT=\"MinGW 4.4.0\" "
        elif self.compiler() == "msvc2005":
          self.subinfo.options.configure.defines += " -DKDE_DISTRIBUTION_TEXT=\"MS Visual Studio 2005 SP1\" "
        elif self.compiler() == "msvc2008":
          self.subinfo.options.configure.defines += " -DKDE_DISTRIBUTION_TEXT=\"MS Visual Studio 2008 SP1\" "
        elif self.compiler() == "msvc2010":
          self.subinfo.options.configure.defines = " -DKDE_DISTRIBUTION_TEXT=\"MS Visual Studio 2010\" "

        self.subinfo.options.configure.defines += "-DBUILD_doc=OFF "

    def install( self ):
        if not CMakePackageBase.install( self ):
            return False
        if compiler.isMinGW():
            manifest = os.path.join( self.packageDir(), "kconf_update.exe.manifest" )
            executable = os.path.join( self.installDir(), "bin", "kconf_update.exe" )
            utils.embedManifest( executable, manifest )
        return True



if __name__ == '__main__':
    Package().execute()
