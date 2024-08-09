#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: cmake
# autospec version: v18
# autospec commit: f35655a
#
# Source0 file verified with key 0x2C8DF587A6D4AAC1 (nicolas.fella@kde.org)
#
Name     : kdesu
Version  : 6.5.0
Release  : 84
URL      : https://download.kde.org/stable/frameworks/6.5/kdesu-6.5.0.tar.xz
Source0  : https://download.kde.org/stable/frameworks/6.5/kdesu-6.5.0.tar.xz
Source1  : https://download.kde.org/stable/frameworks/6.5/kdesu-6.5.0.tar.xz.sig
Source2  : 2C8DF587A6D4AAC1.pkey
Summary  : Integration with su for elevated privileges
Group    : Development/Tools
License  : CC0-1.0 GPL-2.0 LGPL-2.0 LGPL-2.1 LGPL-3.0
Requires: kdesu-data = %{version}-%{release}
Requires: kdesu-lib = %{version}-%{release}
Requires: kdesu-license = %{version}-%{release}
Requires: kdesu-locales = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : buildreq-kde
BuildRequires : extra-cmake-modules-data
BuildRequires : gnupg
BuildRequires : libX11-dev libICE-dev libSM-dev libXau-dev libXcomposite-dev libXcursor-dev libXdamage-dev libXdmcp-dev libXext-dev libXfixes-dev libXft-dev libXi-dev libXinerama-dev libXi-dev libXmu-dev libXpm-dev libXrandr-dev libXrender-dev libXres-dev libXScrnSaver-dev libXt-dev libXtst-dev libXv-dev libXxf86vm-dev
BuildRequires : qt6base-dev
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

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
mkdir .gnupg
chmod 700 .gnupg
gpg --homedir .gnupg --import %{SOURCE2}
gpg --homedir .gnupg --status-fd 1 --verify %{SOURCE1} %{SOURCE0} > gpg.status
grep -E '^\[GNUPG:\] (GOODSIG|EXPKEYSIG) 2C8DF587A6D4AAC1' gpg.status
%setup -q -n kdesu-6.5.0
cd %{_builddir}/kdesu-6.5.0
pushd ..
cp -a kdesu-6.5.0 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1723244690
mkdir -p clr-build
pushd clr-build
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export GOAMD64=v2
%cmake ..   -G 'Unix Makefiles'
make  %{?_smp_mflags}
popd
pushd ../buildavx2/
mkdir -p clr-build-avx2
pushd clr-build-avx2
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
GOAMD64=v3
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS -march=x86-64-v3 "
%cmake ..   -G 'Unix Makefiles'
make  %{?_smp_mflags}
popd
popd

%install
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export SOURCE_DATE_EPOCH=1723244690
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/kdesu
cp %{_builddir}/kdesu-%{version}/LICENSES/CC0-1.0.txt %{buildroot}/usr/share/package-licenses/kdesu/82da472f6d00dc5f0a651f33ebb320aa9c7b08d0 || :
cp %{_builddir}/kdesu-%{version}/LICENSES/GPL-2.0-only.txt %{buildroot}/usr/share/package-licenses/kdesu/2a638514c87c4923c0570c55822620fad56f2a33 || :
cp %{_builddir}/kdesu-%{version}/LICENSES/LGPL-2.0-or-later.txt %{buildroot}/usr/share/package-licenses/kdesu/20079e8f79713dce80ab09774505773c926afa2a || :
cp %{_builddir}/kdesu-%{version}/LICENSES/LGPL-2.1-only.txt %{buildroot}/usr/share/package-licenses/kdesu/3c3d7573e137d48253731c975ecf90d74cfa9efe || :
cp %{_builddir}/kdesu-%{version}/LICENSES/LGPL-3.0-only.txt %{buildroot}/usr/share/package-licenses/kdesu/757b86330df80f81143d5916b3e92b4bcb1b1890 || :
cp %{_builddir}/kdesu-%{version}/LICENSES/LicenseRef-KDE-Accepted-LGPL.txt %{buildroot}/usr/share/package-licenses/kdesu/e458941548e0864907e654fa2e192844ae90fc32 || :
cp %{_builddir}/kdesu-%{version}/LICENSES/LicenseRef-KDE-Accepted-LGPL.txt %{buildroot}/usr/share/package-licenses/kdesu/e458941548e0864907e654fa2e192844ae90fc32 || :
export GOAMD64=v2
pushd ../buildavx2/
GOAMD64=v3
pushd clr-build-avx2
%make_install_v3  || :
popd
popd
GOAMD64=v2
pushd clr-build
%make_install
popd
%find_lang kdesud6
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)
/V3/usr/lib64/libexec/kf6/kdesu_stub
/V3/usr/lib64/libexec/kf6/kdesud
/usr/lib64/libexec/kf6/kdesu_stub
/usr/lib64/libexec/kf6/kdesud

%files data
%defattr(-,root,root,-)
/usr/share/qlogging-categories6/ksu.categories

%files dev
%defattr(-,root,root,-)
/usr/include/KF6/KDESu/KDESu/Client
/usr/include/KF6/KDESu/KDESu/PtyProcess
/usr/include/KF6/KDESu/KDESu/SshProcess
/usr/include/KF6/KDESu/KDESu/StubProcess
/usr/include/KF6/KDESu/KDESu/SuProcess
/usr/include/KF6/KDESu/kdesu/client.h
/usr/include/KF6/KDESu/kdesu/defaults.h
/usr/include/KF6/KDESu/kdesu/kdesu_export.h
/usr/include/KF6/KDESu/kdesu/ptyprocess.h
/usr/include/KF6/KDESu/kdesu/sshprocess.h
/usr/include/KF6/KDESu/kdesu/stubprocess.h
/usr/include/KF6/KDESu/kdesu/suprocess.h
/usr/include/KF6/KDESu/kdesu_version.h
/usr/lib64/cmake/KF6Su/KF6SuConfig.cmake
/usr/lib64/cmake/KF6Su/KF6SuConfigVersion.cmake
/usr/lib64/cmake/KF6Su/KF6SuTargets-relwithdebinfo.cmake
/usr/lib64/cmake/KF6Su/KF6SuTargets.cmake
/usr/lib64/libKF6Su.so

%files lib
%defattr(-,root,root,-)
/V3/usr/lib64/libKF6Su.so.6.5.0
/usr/lib64/libKF6Su.so.6
/usr/lib64/libKF6Su.so.6.5.0

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/kdesu/20079e8f79713dce80ab09774505773c926afa2a
/usr/share/package-licenses/kdesu/2a638514c87c4923c0570c55822620fad56f2a33
/usr/share/package-licenses/kdesu/3c3d7573e137d48253731c975ecf90d74cfa9efe
/usr/share/package-licenses/kdesu/757b86330df80f81143d5916b3e92b4bcb1b1890
/usr/share/package-licenses/kdesu/82da472f6d00dc5f0a651f33ebb320aa9c7b08d0
/usr/share/package-licenses/kdesu/e458941548e0864907e654fa2e192844ae90fc32

%files locales -f kdesud6.lang
%defattr(-,root,root,-)

