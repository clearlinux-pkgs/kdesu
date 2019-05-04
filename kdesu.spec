#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0x58D0EE648A48B3BB (faure@kde.org)
#
Name     : kdesu
Version  : 5.57.0
Release  : 17
URL      : https://download.kde.org/stable/frameworks/5.57/kdesu-5.57.0.tar.xz
Source0  : https://download.kde.org/stable/frameworks/5.57/kdesu-5.57.0.tar.xz
Source99 : https://download.kde.org/stable/frameworks/5.57/kdesu-5.57.0.tar.xz.sig
Summary  : Integration with su for elevated privileges
Group    : Development/Tools
License  : LGPL-2.1
Requires: kdesu-lib = %{version}-%{release}
Requires: kdesu-license = %{version}-%{release}
Requires: kdesu-locales = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : buildreq-kde
BuildRequires : libX11-dev libICE-dev libSM-dev libXau-dev libXcomposite-dev libXcursor-dev libXdamage-dev libXdmcp-dev libXext-dev libXfixes-dev libXft-dev libXi-dev libXinerama-dev libXi-dev libXmu-dev libXpm-dev libXrandr-dev libXrender-dev libXres-dev libXScrnSaver-dev libXt-dev libXtst-dev libXv-dev libXxf86misc-dev libXxf86vm-dev

%description
Maintainer: Adriaan de Groot <groot@kde.org>
Maintainer: kdesu was maintained by Alan Eldridge until his
death in 2003.

%package dev
Summary: dev components for the kdesu package.
Group: Development
Requires: kdesu-lib = %{version}-%{release}
Provides: kdesu-devel = %{version}-%{release}
Requires: kdesu = %{version}-%{release}

%description dev
dev components for the kdesu package.


%package lib
Summary: lib components for the kdesu package.
Group: Libraries
Requires: kdesu-license = %{version}-%{release}

%description lib
lib components for the kdesu package.


%package license
Summary: license components for the kdesu package.
Group: Default

%description license
license components for the kdesu package.


%package locales
Summary: locales components for the kdesu package.
Group: Default

%description locales
locales components for the kdesu package.


%prep
%setup -q -n kdesu-5.57.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1557010410
mkdir -p clr-build
pushd clr-build
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
%cmake ..
make  %{?_smp_mflags}
popd

%install
export SOURCE_DATE_EPOCH=1557010410
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/kdesu
cp COPYING.LIB %{buildroot}/usr/share/package-licenses/kdesu/COPYING.LIB
pushd clr-build
%make_install
popd
%find_lang kdesud5

%files
%defattr(-,root,root,-)
/usr/lib64/libexec/kf5/kdesu_stub
/usr/lib64/libexec/kf5/kdesud

%files dev
%defattr(-,root,root,-)
/usr/include/KF5/KDESu/KDESu/Client
/usr/include/KF5/KDESu/KDESu/PtyProcess
/usr/include/KF5/KDESu/KDESu/SshProcess
/usr/include/KF5/KDESu/KDESu/StubProcess
/usr/include/KF5/KDESu/KDESu/SuProcess
/usr/include/KF5/KDESu/kdesu/client.h
/usr/include/KF5/KDESu/kdesu/defaults.h
/usr/include/KF5/KDESu/kdesu/kdesu_export.h
/usr/include/KF5/KDESu/kdesu/process.h
/usr/include/KF5/KDESu/kdesu/ptyprocess.h
/usr/include/KF5/KDESu/kdesu/ssh.h
/usr/include/KF5/KDESu/kdesu/sshprocess.h
/usr/include/KF5/KDESu/kdesu/stub.h
/usr/include/KF5/KDESu/kdesu/stubprocess.h
/usr/include/KF5/KDESu/kdesu/su.h
/usr/include/KF5/KDESu/kdesu/suprocess.h
/usr/include/KF5/kdesu_version.h
/usr/lib64/cmake/KF5Su/KF5SuConfig.cmake
/usr/lib64/cmake/KF5Su/KF5SuConfigVersion.cmake
/usr/lib64/cmake/KF5Su/KF5SuTargets-relwithdebinfo.cmake
/usr/lib64/cmake/KF5Su/KF5SuTargets.cmake
/usr/lib64/libKF5Su.so
/usr/lib64/qt5/mkspecs/modules/qt_KDESu.pri

%files lib
%defattr(-,root,root,-)
/usr/lib64/libKF5Su.so.5
/usr/lib64/libKF5Su.so.5.57.0

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/kdesu/COPYING.LIB

%files locales -f kdesud5.lang
%defattr(-,root,root,-)

