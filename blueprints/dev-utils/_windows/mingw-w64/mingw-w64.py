import info


class subinfo(info.infoclass):
    def setTargets(self):
        for ver, rev, rt in [("5.3.0", "0", "4"),
                             ("5.4.0", "0", "5"),
                             ("6.2.0", "0", "5"),
                             ("7.1.0", "0", "5"),
                             ("7.2.0", "1", "5"),
                             ("7.3.0", "0", "5"),
                             ]:
            arch = "i686" if CraftCore.compiler.isX86() else "x86_64"
            exceptionType = "sjlj" if CraftCore.compiler.isX86() else "seh"
            self.targets[
                f"{ver}-{rev}"] = f"http://downloads.sourceforge.net/sourceforge/mingw-w64/{arch}-{ver}-release-posix-{exceptionType}-rt_v{rt}-rev{rev}.7z"

        self.targetDigestsX64["7.1.0-0"] = (['5391e8e733dcdab71e6ac71d6524e841be5ea980dc14f22a23af64e92af5dcd7'], CraftHash.HashAlgorithm.SHA256)
        self.targetDigestsX64["7.2.0-1"] = (['ef88d8691566b993778ed3ad651a3c75bd67896d1d8e220729fe24ec405ec21c'], CraftHash.HashAlgorithm.SHA256)
        self.targetDigestsX64["7.3.0-0"] = (['784d25b00e7cf27aa64abe2363b315400c27526bfce672fdee97137f71823d03'], CraftHash.HashAlgorithm.SHA256)
        self.targetDigests["7.3.0-0"] = (['c1f80f43dd0fb625ee925b4fd01974140871fe09bb771d0684b306ba58ed47f3'], CraftHash.HashAlgorithm.SHA256)

        self.defaultTarget = "7.3.0-0"

    def setDependencies(self):
        self.runtimeDependencies["dev-utils/7zip"] = "default"


from Package.BinaryPackageBase import *


class PackageMinGW(BinaryPackageBase):
    def __init__(self):
        BinaryPackageBase.__init__(self)

    def install(self):
        if not BinaryPackageBase.install(self):
            return False
        if CraftCore.compiler.isX86():
            return utils.moveDir(os.path.join(self.installDir(), "mingw32"), os.path.join(self.installDir(), "mingw"))
        return True


from Package.Qt5CorePackageBase import *


class Package(Qt5CoreSdkPackageBase):
    def __init__(self):
        Qt5CoreSdkPackageBase.__init__(self, condition=CraftCore.compiler.isMinGW(), classA=PackageMinGW)
