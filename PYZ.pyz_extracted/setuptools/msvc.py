# Source Generated with Decompyle++
# File: msvc.pyc (Python 3.12)

"""
Environment info about Microsoft Compilers.

>>> getfixture('windows_only')
>>> ei = EnvironmentInfo('amd64')
"""
from __future__ import annotations
import contextlib
import itertools
import json
import os
import os.path as os
import platform
from typing import TYPE_CHECKING, TypedDict
from more_itertools import unique_everseen
import distutils.errors as distutils
if TYPE_CHECKING:
    from typing_extensions import LiteralString, NotRequired

class PlatformInfo:
    '''
    Current and Target Architectures information.

    Parameters
    ----------
    arch: str
        Target architecture.
    '''
    current_cpu = environ.get('processor_architecture', '').lower()
    
    def __init__(self = None, arch = None):
        self.arch = arch.lower().replace('x64', 'amd64')

    target_cpu = (lambda self: self.arch[self.arch.find('_') + 1:])()
    
    def target_is_x86(self):
        '''
        Return True if target CPU is x86 32 bits..

        Return
        ------
        bool
            CPU is x86 32 bits
        '''
        return self.target_cpu == 'x86'

    
    def current_is_x86(self):
        '''
        Return True if current CPU is x86 32 bits..

        Return
        ------
        bool
            CPU is x86 32 bits
        '''
        return self.current_cpu == 'x86'

    
    def current_dir(self = None, hidex86 = None, x64 = property):
        """
        Current platform specific subfolder.

        Parameters
        ----------
        hidex86: bool
            return '' and not '' if architecture is x86.
        x64: bool
            return 'd' and not '\x07md64' if architecture is amd64.

        Return
        ------
        str
            subfolder: '\target', or '' (see hidex86 parameter)
        """
        if self.current_cpu == 'x86' and hidex86:
            return ''
        if None.current_cpu == 'amd64' and x64:
            return '\\x64'
        return f'''{self.current_cpu}'''

    
    def target_dir(self = None, hidex86 = None, x64 = None):
        """
        Target platform specific subfolder.

        Parameters
        ----------
        hidex86: bool
            return '' and not '\\x86' if architecture is x86.
        x64: bool
            return '\\x64' and not '\\amd64' if architecture is amd64.

        Return
        ------
        str
            subfolder: '\\current', or '' (see hidex86 parameter)
        """
        if self.target_cpu == 'x86' and hidex86:
            return ''
        if None.target_cpu == 'amd64' and x64:
            return '\\x64'
        return f'''{self.target_cpu}'''

    
    def cross_dir(self, forcex86 = (False,)):
        """
        Cross platform specific subfolder.

        Parameters
        ----------
        forcex86: bool
            Use 'x86' as current architecture even if current architecture is
            not x86.

        Return
        ------
        str
            subfolder: '' if target architecture is current architecture,
            '\\current_target' if not.
        """
        current = 'x86' if forcex86 else self.current_cpu
        if self.target_cpu == current:
            return ''
        return None.target_dir().replace('\\', f'''\\{current}_''')



class RegistryInfo:
    '''
    Microsoft Visual Studio related registry information.

    Parameters
    ----------
    platform_info: PlatformInfo
        "PlatformInfo" instance.
    '''
    HKEYS = (winreg.HKEY_USERS, winreg.HKEY_CURRENT_USER, winreg.HKEY_LOCAL_MACHINE, winreg.HKEY_CLASSES_ROOT)
    
    def __init__(self = None, platform_info = None):
        self.pi = platform_info

    visualstudio = (lambda self = None: 'VisualStudio')()
    sxs = (lambda self: os.path.join(self.visualstudio, 'SxS'))()
    vc = (lambda self: os.path.join(self.sxs, 'VC7'))()
    vs = (lambda self: os.path.join(self.sxs, 'VS7'))()
    vc_for_python = (lambda self = property: 'DevDiv\\VCForPython')()
    microsoft_sdk = (lambda self = None: 'Microsoft SDKs')()
    windows_sdk = (lambda self: os.path.join(self.microsoft_sdk, 'Windows'))()
    netfx_sdk = (lambda self: os.path.join(self.microsoft_sdk, 'NETFXSDK'))()
    windows_kits_roots = (lambda self = property: 'Windows Kits\\Installed Roots')()
    
    def microsoft(self, key, x86 = (False,)):
        '''
        Return key in Microsoft software registry.

        Parameters
        ----------
        key: str
            Registry key path where look.
        x86: str
            Force x86 software registry.

        Return
        ------
        str
            Registry key
        '''
        node64 = '' if self.pi.current_is_x86() or x86 else 'Wow6432Node'
        return os.path.join('Software', node64, 'Microsoft', key)

    
    def lookup(self, key, name):
        '''
        Look for values in registry in Microsoft software registry.

        Parameters
        ----------
        key: str
            Registry key path where look.
        name: str
            Value name to find.

        Return
        ------
        str
            value
        '''
        key_read = winreg.KEY_READ
        openkey = winreg.OpenKey
        closekey = winreg.CloseKey
        ms = self.microsoft
        for hkey in self.HKEYS:
            bkey = None
            bkey = openkey(hkey, ms(key), 0, key_read)
            if bkey:
                closekey(bkey)
                
                return self.HKEYS, winreg.QueryValueEx(bkey, name)[0]
            winreg.QueryValueEx(bkey, name)[0]
            return self.HKEYS
        return None
        except OSError:
            if not self.pi.current_is_x86():
                pass
            else:
                except OSError:
                    continue
            continue
        except OSError:
            pass
        if not bkey:
            continue
        closekey(bkey)
        continue
        if bkey:
            closekey(bkey)



class SystemInfo:
    '''
    Microsoft Windows and Visual Studio related system information.

    Parameters
    ----------
    registry_info: RegistryInfo
        "RegistryInfo" instance.
    vc_ver: float
        Required Microsoft Visual C++ version.
    '''
    WinDir = environ.get('WinDir', '')
    ProgramFiles = environ.get('ProgramFiles', '')
    ProgramFilesx86 = environ.get('ProgramFiles(x86)', ProgramFiles)
    
    def __init__(self = None, registry_info = None, vc_ver = None):
        self.ri = registry_info
        self.pi = self.ri.pi
        self.known_vs_paths = self.find_programdata_vs_vers()
        if not vc_ver:
            vc_ver
        self.vs_ver = self._find_latest_available_vs_ver()
        self.vc_ver = self._find_latest_available_vs_ver()

    
    def _find_latest_available_vs_ver(self):
        '''
        Find the latest VC version

        Return
        ------
        float
            version
        '''
        reg_vc_vers = self.find_reg_vs_vers()
        if not reg_vc_vers and self.known_vs_paths:
            raise distutils.errors.DistutilsPlatformError('No Microsoft Visual C++ version found')
        vc_vers = set(reg_vc_vers)
        vc_vers.update(self.known_vs_paths)
        return sorted(vc_vers)[-1]

    
    def find_reg_vs_vers(self):
        '''
        Find Microsoft Visual Studio versions available in registry.

        Return
        ------
        list of float
            Versions
        '''
        ms = self.ri.microsoft
        vckeys = (self.ri.vc, self.ri.vc_for_python, self.ri.vs)
        vs_vers = []
        for hkey, key in itertools.product(self.ri.HKEYS, vckeys):
            bkey = winreg.OpenKey(hkey, ms(key), 0, winreg.KEY_READ)
            bkey
            (subkeys, values, _) = winreg.QueryInfoKey(bkey)
            for i in range(values):
                contextlib.suppress(ValueError)
                ver = float(winreg.EnumValue(bkey, i)[0])
                if ver not in vs_vers:
                    vs_vers.append(ver)
                None(None, None)
            for i in range(subkeys):
                contextlib.suppress(ValueError)
                ver = float(winreg.EnumKey(bkey, i))
                if ver not in vs_vers:
                    vs_vers.append(ver)
                None(None, None)
            None(None, None)
        return sorted(vs_vers)
        except OSError:
            continue
        with None:
            if not None:
                pass
        continue
        with None:
            if not None:
                pass
        continue
        with None:
            if not None:
                pass
        continue

    
    def find_programdata_vs_vers(self = None):
        '''
        Find Visual studio 2017+ versions from information in
        "C:\\ProgramData\\Microsoft\\VisualStudio\\Packages\\_Instances".

        Return
        ------
        dict
            float version as key, path as value.
        '''
        vs_versions = { }
        instances_dir = 'C:\\ProgramData\\Microsoft\\VisualStudio\\Packages\\_Instances'
    # WARNING: Decompyle incomplete

    _as_float_version = (lambda version: float('.'.join(version.split('.')[:2])))()
    VSInstallDir = (lambda self: default = os.path.join(self.ProgramFilesx86, f'''Microsoft Visual Studio {self.vs_ver:0.1f}''')if not self.ri.lookup(self.ri.vs, f'''{self.vs_ver:0.1f}'''):
self.ri.lookup(self.ri.vs, f'''{self.vs_ver:0.1f}''')default)()
    VCInstallDir = (lambda self: if not self._guess_vc():
self._guess_vc()path = self._guess_vc_legacy()if not os.path.isdir(path):
msg = 'Microsoft Visual C++ directory not found'raise distutils.errors.DistutilsPlatformError(msg)path)()
    
    def _guess_vc(self):
        '''
        Locate Visual C++ for VS2017+.

        Return
        ------
        str
            path
        '''
        if self.vs_ver <= 14:
            return ''
        
        try:
            vs_dir = self.known_vs_paths[self.vs_ver]
            guess_vc = os.path.join(vs_dir, 'VC\\Tools\\MSVC')
            
            try:
                vc_ver = os.listdir(guess_vc)[-1]
                self.vc_ver = self._as_float_version(vc_ver)
                return os.path.join(guess_vc, vc_ver)
                except KeyError:
                    vs_dir = self.VSInstallDir
                    continue
            except (OSError, IndexError):
                return ''



    
    def _guess_vc_legacy(self):
        '''
        Locate Visual C++ for versions prior to 2017.

        Return
        ------
        str
            path
        '''
        default = os.path.join(self.ProgramFilesx86, f'''Microsoft Visual Studio {self.vs_ver:0.1f}\\VC''')
        reg_path = os.path.join(self.ri.vc_for_python, f'''{self.vs_ver:0.1f}''')
        python_vc = self.ri.lookup(reg_path, 'installdir')
        default_vc = os.path.join(python_vc, 'VC') if python_vc else default
        if not self.ri.lookup(self.ri.vc, f'''{self.vs_ver:0.1f}'''):
            self.ri.lookup(self.ri.vc, f'''{self.vs_ver:0.1f}''')
        return default_vc

    WindowsSdkVersion = (lambda self = property: if self.vs_ver <= 9:
('7.0', '6.1', '6.0a')if self.vs_ver == 10:
('7.1', '7.0a')if self.vs_ver == 11:
('8.0', '8.0a')if self.vs_ver == 12:
('8.1', '8.1a')if self.vs_ver >= 14:
('10.0', '8.1')())()
    WindowsSdkLastVersion = (lambda self: self._use_last_dir_name(os.path.join(self.WindowsSdkDir, 'lib')))()
    WindowsSdkDir = (lambda self = staticmethod: sdkdir = ''for ver in self.WindowsSdkVersion:
loc = os.path.join(self.ri.windows_sdk, f'''v{ver}''')sdkdir = self.ri.lookup(loc, 'installationfolder')if not sdkdir:
continueself.WindowsSdkVersionif not sdkdir or os.path.isdir(sdkdir):
path = os.path.join(self.ri.vc_for_python, f'''{self.vc_ver:0.1f}''')install_base = self.ri.lookup(path, 'installdir')if install_base:
sdkdir = os.path.join(install_base, 'WinSDK')if not sdkdir or os.path.isdir(sdkdir):
for ver in self.WindowsSdkVersion:
intver = ver[:ver.rfind('.')]path = f'''Microsoft SDKs\\Windows Kits\\{intver}'''d = os.path.join(self.ProgramFiles, path)if not os.path.isdir(d):
continuesdkdir = dif not sdkdir or os.path.isdir(sdkdir):
for ver in self.WindowsSdkVersion:
path = f'''Microsoft SDKs\\Windows\\v{ver}'''d = os.path.join(self.ProgramFiles, path)if not os.path.isdir(d):
continuesdkdir = dif not sdkdir:
sdkdir = os.path.join(self.VCInstallDir, 'PlatformSDK')sdkdir)()
    WindowsSDKExecutablePath = (lambda self: if self.vs_ver <= 11:
netfxver = 35arch = ''else:
netfxver = 40hidex86 = True if self.vs_ver <= 12 else Falsearch = self.pi.current_dir(x64 = True, hidex86 = hidex86).replace('\\', '-')fx = f'''WinSDK-NetFx{netfxver}Tools{arch}'''regpaths = []if self.vs_ver >= 14:
for ver in self.NetFxSdkVersion:
regpaths += [
os.path.join(self.ri.netfx_sdk, ver, fx)]for ver in self.WindowsSdkVersion:
regpaths += [
os.path.join(self.ri.windows_sdk, f'''v{ver}A''', fx)]for path in regpaths:
execpath = self.ri.lookup(path, 'installationfolder')if not execpath:
continueregpaths, execpath)()
    FSharpInstallDir = (lambda self: path = os.path.join(self.ri.visualstudio, f'''{self.vs_ver:0.1f}\\Setup\\F#''')if not self.ri.lookup(path, 'productdir'):
self.ri.lookup(path, 'productdir')'')()
    UniversalCRTSdkDir = (lambda self: vers = ('10', '81') if self.vs_ver >= 14 else ()for ver in vers:
sdkdir = self.ri.lookup(self.ri.windows_kits_roots, f'''kitsroot{ver}''')if not sdkdir:
continueif not sdkdir:
sdkdirvers, '')()
    UniversalCRTSdkLastVersion = (lambda self: self._use_last_dir_name(os.path.join(self.UniversalCRTSdkDir, 'lib')))()
    NetFxSdkVersion = (lambda self: if self.vs_ver >= 14:
('4.7.2', '4.7.1', '4.7', '4.6.2', '4.6.1', '4.6', '4.5.2', '4.5.1', '4.5'))()
    NetFxSdkDir = (lambda self: sdkdir = ''for ver in self.NetFxSdkVersion:
loc = os.path.join(self.ri.netfx_sdk, ver)sdkdir = self.ri.lookup(loc, 'kitsinstallationfolder')if not sdkdir:
continueself.NetFxSdkVersionsdkdirsdkdir)()
    FrameworkDir32 = (lambda self: guess_fw = os.path.join(self.WinDir, 'Microsoft.NET\\Framework')if not self.ri.lookup(self.ri.vc, 'frameworkdir32'):
self.ri.lookup(self.ri.vc, 'frameworkdir32')guess_fw)()
    FrameworkDir64 = (lambda self: guess_fw = os.path.join(self.WinDir, 'Microsoft.NET\\Framework64')if not self.ri.lookup(self.ri.vc, 'frameworkdir64'):
self.ri.lookup(self.ri.vc, 'frameworkdir64')guess_fw)()
    FrameworkVersion32 = (lambda self = property: self._find_dot_net_versions(32))()
    FrameworkVersion64 = (lambda self = property: self._find_dot_net_versions(64))()
    
    def _find_dot_net_versions(self = property, bits = property):
        '''
        Find Microsoft .NET Framework versions.

        Parameters
        ----------
        bits: int
            Platform number of bits: 32 or 64.

        Return
        ------
        tuple of str
            versions
        '''
        reg_ver = self.ri.lookup(self.ri.vc, f'''frameworkver{bits}''')
        dot_net_dir = getattr(self, f'''FrameworkDir{bits}''')
        if not reg_ver:
            reg_ver
            if not self._use_last_dir_name(dot_net_dir, 'v'):
                self._use_last_dir_name(dot_net_dir, 'v')
        ver = ''
        if self.vs_ver >= 12:
            return (ver, 'v4.0')
        if None.vs_ver >= 10:
            if ver.lower()[:2] != 'v4':
                return ('v4.0.30319', 'v3.5')
            return (None, 'v3.5')
        if None.vs_ver == 9:
            return ('v3.5', 'v2.0.50727')
        if self.vs_ver == 8:
            return ('v3.0', 'v2.0.50727')
        return ()

    _use_last_dir_name = (lambda path, prefix = ('',): pass# WARNING: Decompyle incomplete
)()


class _EnvironmentDict(TypedDict):
    py_vcruntime_redist: 'NotRequired[str | None]' = '_EnvironmentDict'


class EnvironmentInfo:
    '''
    Return environment variables for specified Microsoft Visual C++ version
    and platform : Lib, Include, Path and libpath.

    This function is compatible with Microsoft Visual C++ 9.0 to 14.X.

    Script created by analysing Microsoft environment configuration files like
    "vcvars[...].bat", "SetEnv.Cmd", "vcbuildtools.bat", ...

    Parameters
    ----------
    arch: str
        Target architecture.
    vc_ver: float
        Required Microsoft Visual C++ version. If not set, autodetect the last
        version.
    vc_min_ver: float
        Minimum Microsoft Visual C++ version.
    '''
    
    def __init__(self = None, arch = None, vc_ver = None, vc_min_ver = (None, 0)):
        self.pi = PlatformInfo(arch)
        self.ri = RegistryInfo(self.pi)
        self.si = SystemInfo(self.ri, vc_ver)
        if self.vc_ver < vc_min_ver:
            err = 'No suitable Microsoft Visual C++ version found'
            raise distutils.errors.DistutilsPlatformError(err)

    vs_ver = (lambda self: self.si.vs_ver)()
    vc_ver = (lambda self: self.si.vc_ver)()
    VSTools = (lambda self: paths = [
'Common7\\IDE',
'Common7\\Tools']if self.vs_ver >= 14:
arch_subdir = self.pi.current_dir(hidex86 = True, x64 = True)paths += [
'Common7\\IDE\\CommonExtensions\\Microsoft\\TestWindow']paths += [
'Team Tools\\Performance Tools']paths += [
f'''Team Tools\\Performance Tools{arch_subdir}''']# WARNING: Decompyle incomplete
)()
    VCIncludes = (lambda self: [
os.path.join(self.si.VCInstallDir, 'Include'),
os.path.join(self.si.VCInstallDir, 'ATLMFC\\Include')])()
    VCLibraries = (lambda self: if self.vs_ver >= 15:
arch_subdir = self.pi.target_dir(x64 = True)else:
arch_subdir = self.pi.target_dir(hidex86 = True)paths = [
f'''Lib{arch_subdir}''',
f'''ATLMFC\\Lib{arch_subdir}''']if self.vs_ver >= 14:
paths += [
f'''Lib\\store{arch_subdir}''']# WARNING: Decompyle incomplete
)()
    VCStoreRefs = (lambda self: if self.vs_ver < 14:
[][
None.path.join(self.si.VCInstallDir, 'Lib\\store\\references')])()
    VCTools = (lambda self: si = self.sitools = [
os.path.join(si.VCInstallDir, 'VCPackages')]forcex86 = True if self.vs_ver <= 10 else Falsearch_subdir = self.pi.cross_dir(forcex86)if arch_subdir:
tools += [
os.path.join(si.VCInstallDir, f'''Bin{arch_subdir}''')]if self.vs_ver == 14:
path = f'''Bin{self.pi.current_dir(hidex86 = True)}'''tools += [
os.path.join(si.VCInstallDir, path)]toolsif None.vs_ver >= 15:
host_id = self.pi.current_cpu.replace('amd64', 'x64').upper()host_dir = os.path.join('bin', f'''Host{host_id}%s''')tools += [
os.path.join(si.VCInstallDir, host_dir % self.pi.target_dir(x64 = True))]if self.pi.current_cpu != self.pi.target_cpu:
tools += [
os.path.join(si.VCInstallDir, host_dir % self.pi.current_dir(x64 = True))]toolsNone += [
os.path.join(si.VCInstallDir, 'Bin')]tools)()
    OSLibraries = (lambda self: if self.vs_ver <= 10:
arch_subdir = self.pi.target_dir(hidex86 = True, x64 = True)[
os.path.join(self.si.WindowsSdkDir, f'''Lib{arch_subdir}''')]arch_subdir = None.pi.target_dir(x64 = True)lib = os.path.join(self.si.WindowsSdkDir, 'lib')libver = self._sdk_subdir[
os.path.join(lib, f'''{libver}um{arch_subdir}''')])()
    OSIncludes = (lambda self: include = os.path.join(self.si.WindowsSdkDir, 'include')if self.vs_ver <= 10:
[
include,
os.path.join(include, 'gl')]if None.vs_ver >= 14:
sdkver = self._sdk_subdirelse:
sdkver = ''[
os.path.join(include, f'''{sdkver}shared'''),
os.path.join(include, f'''{sdkver}um'''),
os.path.join(include, f'''{sdkver}winrt''')])()
    OSLibpath = (lambda self: ref = os.path.join(self.si.WindowsSdkDir, 'References')libpath = []if self.vs_ver <= 9:
libpath += self.OSLibrariesif self.vs_ver >= 11:
libpath += [
os.path.join(ref, 'CommonConfiguration\\Neutral')]if self.vs_ver >= 14:
libpath += [
ref,
os.path.join(self.si.WindowsSdkDir, 'UnionMetadata'),
os.path.join(ref, 'Windows.Foundation.UniversalApiContract', '1.0.0.0'),
os.path.join(ref, 'Windows.Foundation.FoundationContract', '1.0.0.0'),
os.path.join(ref, 'Windows.Networking.Connectivity.WwanContract', '1.0.0.0'),
os.path.join(self.si.WindowsSdkDir, 'ExtensionSDKs', 'Microsoft.VCLibs', f'''{self.vs_ver:0.1f}''', 'References', 'CommonConfiguration', 'neutral')]libpath)()
    SdkTools = (lambda self: list(self._sdk_tools()))()
    
    def _sdk_tools(self):
        '''
        Microsoft Windows SDK Tools paths generator.

        Return
        ------
        generator of str
            paths
        '''
        pass
    # WARNING: Decompyle incomplete

    _sdk_subdir = (lambda self: ucrtver = self.si.WindowsSdkLastVersionif ucrtver:
f'''{ucrtver}\\''')()
    SdkSetup = (lambda self: if self.vs_ver > 9:
[][
None.path.join(self.si.WindowsSdkDir, 'Setup')])()
    FxTools = (lambda self: pi = self.pisi = self.siif self.vs_ver <= 10:
include32 = Trueif not pi.target_is_x86():
not pi.target_is_x86()include64 = not pi.current_is_x86()elif not pi.target_is_x86():
pi.target_is_x86()include32 = pi.current_is_x86()if not pi.current_cpu == 'amd64':
pi.current_cpu == 'amd64'include64 = pi.target_cpu == 'amd64'tools = []# WARNING: Decompyle incomplete
)()
    NetFxSDKLibraries = (lambda self: if not self.vs_ver < 14 or self.si.NetFxSdkDir:
[]arch_subdir = None.pi.target_dir(x64 = True)[
os.path.join(self.si.NetFxSdkDir, f'''lib\\um{arch_subdir}''')])()
    NetFxSDKIncludes = (lambda self: if not self.vs_ver < 14 or self.si.NetFxSdkDir:
[][
None.path.join(self.si.NetFxSdkDir, 'include\\um')])()
    VsTDb = (lambda self: [
os.path.join(self.si.VSInstallDir, 'VSTSDB\\Deploy')])()
    MSBuild = (lambda self: if self.vs_ver < 12:
[]if None.vs_ver < 15:
base_path = self.si.ProgramFilesx86arch_subdir = self.pi.current_dir(hidex86 = True)else:
base_path = self.si.VSInstallDirarch_subdir = ''path = f'''MSBuild\\{self.vs_ver:0.1f}\\bin{arch_subdir}'''build = [
os.path.join(base_path, path)]if self.vs_ver >= 15:
build += [
os.path.join(base_path, path, 'Roslyn')]build)()
    HTMLHelpWorkshop = (lambda self: if self.vs_ver < 11:
[][
None.path.join(self.si.ProgramFilesx86, 'HTML Help Workshop')])()
    UCRTLibraries = (lambda self: if self.vs_ver < 14:
[]arch_subdir = None.pi.target_dir(x64 = True)lib = os.path.join(self.si.UniversalCRTSdkDir, 'lib')ucrtver = self._ucrt_subdir[
os.path.join(lib, f'''{ucrtver}ucrt{arch_subdir}''')])()
    UCRTIncludes = (lambda self: if self.vs_ver < 14:
[]include = None.path.join(self.si.UniversalCRTSdkDir, 'include')[
os.path.join(include, f'''{self._ucrt_subdir}ucrt''')])()
    _ucrt_subdir = (lambda self: ucrtver = self.si.UniversalCRTSdkLastVersionif ucrtver:
f'''{ucrtver}\\''')()
    FSharp = (lambda self: if  > 11, self.vs_ver or 11, self.vs_ver > 12:
[][
self.si.FSharpInstallDir])()
    VCRuntimeRedist = (lambda self = property: pass# WARNING: Decompyle incomplete
)()
    
    def return_env(self = property, exists = property):
        '''
        Return environment dict.

        Parameters
        ----------
        exists: bool
            It True, only return existing paths.

        Return
        ------
        dict
            environment
        '''
        env = _EnvironmentDict(include = self._build_paths('include', [
            self.VCIncludes,
            self.OSIncludes,
            self.UCRTIncludes,
            self.NetFxSDKIncludes], exists), lib = self._build_paths('lib', [
            self.VCLibraries,
            self.OSLibraries,
            self.FxTools,
            self.UCRTLibraries,
            self.NetFxSDKLibraries], exists), libpath = self._build_paths('libpath', [
            self.VCLibraries,
            self.FxTools,
            self.VCStoreRefs,
            self.OSLibpath], exists), path = self._build_paths('path', [
            self.VCTools,
            self.VSTools,
            self.VsTDb,
            self.SdkTools,
            self.SdkSetup,
            self.FxTools,
            self.MSBuild,
            self.HTMLHelpWorkshop,
            self.FSharp], exists))
        if self.vs_ver >= 14 and self.VCRuntimeRedist:
            env['py_vcruntime_redist'] = self.VCRuntimeRedist
        return env

    
    def _build_paths(self, name, spec_path_lists, exists):
        '''
        Given an environment variable name and specified paths,
        return a pathsep-separated string of paths containing
        unique, extant, directories from those paths and from
        the environment variable. Raise an error if no paths
        are resolved.

        Parameters
        ----------
        name: str
            Environment variable name
        spec_path_lists: list of str
            Paths
        exists: bool
            It True, only return existing paths.

        Return
        ------
        str
            Pathsep-separated paths
        '''
        spec_paths = itertools.chain.from_iterable(spec_path_lists)
        env_paths = environ.get(name, '').split(os.pathsep)
        paths = itertools.chain(spec_paths, env_paths)
        extant_paths = list(filter(os.path.isdir, paths)) if exists else paths
        if not extant_paths:
            msg = f'''{name.upper()} environment variable is empty'''
            raise distutils.errors.DistutilsPlatformError(msg)
        unique_paths = unique_everseen(extant_paths)
        return os.pathsep.join(unique_paths)


