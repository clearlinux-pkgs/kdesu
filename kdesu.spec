#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0x58D0EE648A48B3BB (faure@kde.org)
#
Name     : kdesu
Version  : 5.75.0
Release  : 33
URL      : https://download.kde.org/stable/frameworks/5.75/kdesu-5.75.0.tar.xz
Source0  : https://download.kde.org/stable/frameworks/5.75/kdesu-5.75.0.tar.xz
Source1  : https://download.kde.org/stable/frameworks/5.75/kdesu-5.75.0.tar.xz.sig
Summary  : Integration with su for elevated privileges
Group    : Development/Tools
License  : GPL-2.0 LGPL-2.0 LGPL-2.1 LGPL-3.0
Requires: kdesu-data = %{version}-%{release}
Requires: kdesu-lib = %{version}-%{release}
Requires: kdesu-license = %{version}-%{release}
Requires: kdesu-locales = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : buildreq-kde
BuildRequires : extra-cmake-modules-data
BuildRequires : kcoreaddons-dev
BuildRequires : ki18n-dev
BuildRequires : kpty-dev
BuildRequires : kservice-dev
BuildRequires : libX11-dev libICE-dev libSM-dev libXau-dev libXcomposite-dev libXcursor-dev libXdamage-dev libXdmcp-dev libXext-dev libXfixes-dev libXft-dev libXi-dev libXinerama-dev libXi-dev libXmu-dev libXpm-dev libXrandr-dev libXrender-dev libXres-dev libXScrnSaver-dev libXt-dev libXtst-dev libXv-dev libXxf86misc-dev libXxf86vm-dev
BuildRequires : qtbase-dev

%description
Maintainer: Adriaan de Groot <groot@kde.org>
Maintainer: kdesu was maintained by Alan Eldridge until his
death in 2003.

%package data
Summary: data components for the kdesu package.
Group: Data

%description data
data components for the kdesu package.


%package dev
Summary: dev components for the kdesu package.
Group: Development
Requires: kdesu-lib = %{version}-%{release}
Requires: kdesu-data = %{version}-%{release}
Provides: kdesu-devel = %{version}-%{release}
Requires: kdesu = %{version}-%{release}

%description dev
dev components for the kdesu package.


%package lib
Summary: lib components for the kdesu package.
Group: Libraries
Requires: kdesu-data = %{version}-%{release}
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
%setup -q -n kdesu-5.75.0
cd %{_builddir}/kdesu-5.75.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1602690811
mkdir -p clr-build
pushd clr-build
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
%cmake ..
make  %{?_smp_mflags}
popd

%install
export SOURCE_DATE_EPOCH=1602690811
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/kdesu
cp %{_builddir}/kdesu-5.75.0/LICENSES/GPL-2.0-only.txt %{buildroot}/usr/share/package-licenses/kdesu/2a638514c87c4923c0570c55822620fad56f2a33
cp %{_builddir}/kdesu-5.75.0/LICENSES/LGPL-2.0-or-later.txt %{buildroot}/usr/share/package-licenses/kdesu/20079e8f79713dce80ab09774505773c926afa2a
cp %{_builddir}/kdesu-5.75.0/LICENSES/LGPL-2.1-only.txt %{buildroot}/usr/share/package-licenses/kdesu/3c3d7573e137d48253731c975ecf90d74cfa9efe
cp %{_builddir}/kdesu-5.75.0/LICENSES/LGPL-3.0-only.txt %{buildroot}/usr/share/package-licenses/kdesu/757b86330df80f81143d5916b3e92b4bcb1b1890
cp %{_builddir}/kdesu-5.75.0/LICENSES/LicenseRef-KDE-Accepted-LGPL.txt %{buildroot}/usr/share/package-licenses/kdesu/e458941548e0864907e654fa2e192844ae90fc32
cp %{_builddir}/kdesu-5.75.0/LICENSES/LicenseRef-KDE-Accepted-LGPL.txt %{buildroot}/usr/share/package-licenses/kdesu/e458941548e0864907e654fa2e192844ae90fc32
pushd clr-build
%make_install
popd
%find_lang kdesud5

%files
%defattr(-,root,root,-)
/usr/lib64/libexec/kf5/kdesu_stub
/usr/lib64/libexec/kf5/kdesud

%files data
%defattr(-,root,root,-)
/usr/share/qlogging-categories5/ksu.categories

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
/usr/lib64/libKF5Su.so.5.75.0

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/kdesu/20079e8f79713dce80ab09774505773c926afa2a
/usr/share/package-licenses/kdesu/2a638514c87c4923c0570c55822620fad56f2a33
/usr/share/package-licenses/kdesu/3c3d7573e137d48253731c975ecf90d74cfa9efe
/usr/share/package-licenses/kdesu/757b86330df80f81143d5916b3e92b4bcb1b1890
/usr/share/package-licenses/kdesu/e458941548e0864907e654fa2e192844ae90fc32

%files locales -f kdesud5.lang
%defattr(-,root,root,-)

