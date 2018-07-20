#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0x58D0EE648A48B3BB (faure@kde.org)
#
Name     : kdesu
Version  : 5.48.0
Release  : 1
URL      : https://download.kde.org/stable/frameworks/5.48/kdesu-5.48.0.tar.xz
Source0  : https://download.kde.org/stable/frameworks/5.48/kdesu-5.48.0.tar.xz
Source99 : https://download.kde.org/stable/frameworks/5.48/kdesu-5.48.0.tar.xz.sig
Summary  : No detailed summary available
Group    : Development/Tools
License  : LGPL-2.1
Requires: kdesu-lib
Requires: kdesu-license
Requires: kdesu-locales
BuildRequires : buildreq-cmake
BuildRequires : buildreq-kde
BuildRequires : ki18n-dev
BuildRequires : kpty-dev
BuildRequires : kservice-dev

%description
Maintainer: Adriaan de Groot <groot@kde.org>
Maintainer: kdesu was maintained by Alan Eldridge until his
death in 2003.

%package dev
Summary: dev components for the kdesu package.
Group: Development
Requires: kdesu-lib
Provides: kdesu-devel

%description dev
dev components for the kdesu package.


%package lib
Summary: lib components for the kdesu package.
Group: Libraries
Requires: kdesu-license

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
%setup -q -n kdesu-5.48.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1532113453
mkdir clr-build
pushd clr-build
%cmake ..
make  %{?_smp_mflags}
popd

%install
export SOURCE_DATE_EPOCH=1532113453
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/doc/kdesu
cp COPYING.LIB %{buildroot}/usr/share/doc/kdesu/COPYING.LIB
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
/usr/lib64/libKF5Su.so.5.48.0

%files license
%defattr(-,root,root,-)
/usr/share/doc/kdesu/COPYING.LIB

%files locales -f kdesud5.lang
%defattr(-,root,root,-)

