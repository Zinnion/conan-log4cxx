
from conans import ConanFile, AutoToolsBuildEnvironment, tools, MSBuild, CMake
from conans.errors import ConanException
from conans.tools import os_info, SystemPackageTool
import os

class Apachelog4cxxConan(ConanFile):
    name = "logging-log4cxx"
    version = "0.10.1"
    description = "log4cxx"
    topics = ("conan", "log4cxx", "log")
    url = "https://github.com/zinnion/conan-log4cxx"
    homepage = "https://github.com/zinnion/logging-log4cxx"
    author = "Zinnion <mauro@zinnion.com>"
    license = "MIT"
    exports = ["LICENSE.md"]
    exports_sources = ["CMakeLists.txt"]
    settings = "os", "compiler", "build_type", "arch"
    short_paths = True
    generators = "cmake"
    source_subfolder = "source_subfolder"
    build_subfolder = "build_subfolder"
    options = {
        "shared": [True, False],
        "enable-wchar_t": ["yes", "no"],
        "enable-unichar": ["yes", "no"],
        "enable-cfstring": ["yes", "no"],
        "with-logchar": ["utf-8", "wchar_t", "unichar"],
        "with-charset": ["utf-8", "iso-8859-1", "usascii", "ebcdic", "auto"],
        "with-SMTP": ["libesmtp", "no"],
        "with-ODBC": ["unixODBC", "iODBC", "Microsoft", "no"]            
    }
    default_options = "enable-wchar_t=yes", "enable-unichar=no", "enable-cfstring=no", "with-logchar=utf-8", "with-charset=auto", "with-SMTP=no", "with-ODBC=no", "shared=True"

    def source(self):
        tools.get("{0}/archive/v{1}.tar.gz".format(self.homepage, self.version))
        extracted_dir = self.name + "-" + self.version
        os.rename(extracted_dir, self.source_subfolder)

    def build(self):
        self.run("cd source_subfolder; ./autogen.sh; ./configure; make")

    def package(self):
        self.copy("*", dst="include", src="include", keep_path=True)
        self.copy("libapr*", dst="lib", src="lib", keep_path=False)
        self.copy("liblog4cxx*", dst="lib", src="lib", keep_path=False)

    def package_info(self):
        self.cpp_info.libs = ["log4cxx"]
