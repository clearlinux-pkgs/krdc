#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0xBB463350D6EF31EF (heiko@shruuf.de)
#
Name     : krdc
Version  : 21.08.1
Release  : 29
URL      : https://download.kde.org/stable/release-service/21.08.1/src/krdc-21.08.1.tar.xz
Source0  : https://download.kde.org/stable/release-service/21.08.1/src/krdc-21.08.1.tar.xz
Source1  : https://download.kde.org/stable/release-service/21.08.1/src/krdc-21.08.1.tar.xz.sig
Summary  : No detailed summary available
Group    : Development/Tools
License  : BSD-3-Clause GFDL-1.2 GPL-2.0
Requires: krdc-bin = %{version}-%{release}
Requires: krdc-data = %{version}-%{release}
Requires: krdc-lib = %{version}-%{release}
Requires: krdc-license = %{version}-%{release}
Requires: krdc-locales = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : buildreq-kde
BuildRequires : buildreq-qmake
BuildRequires : extra-cmake-modules-data
BuildRequires : kdnssd-dev
BuildRequires : kdoctools-dev
BuildRequires : knotifyconfig-dev
BuildRequires : libssh-dev
BuildRequires : qtbase-dev mesa-dev

%description
Qt-only version of the KRDC VNC backend
=======================================
In order to build it, you need the LibVNCClient (LibVNCServer)
library (version 0.9.1 or newer required):
http://sourceforge.net/project/showfiles.php?group_id=32584&package_id=24717

%package bin
Summary: bin components for the krdc package.
Group: Binaries
Requires: krdc-data = %{version}-%{release}
Requires: krdc-license = %{version}-%{release}

%description bin
bin components for the krdc package.


%package data
Summary: data components for the krdc package.
Group: Data

%description data
data components for the krdc package.


%package dev
Summary: dev components for the krdc package.
Group: Development
Requires: krdc-lib = %{version}-%{release}
Requires: krdc-bin = %{version}-%{release}
Requires: krdc-data = %{version}-%{release}
Provides: krdc-devel = %{version}-%{release}
Requires: krdc = %{version}-%{release}

%description dev
dev components for the krdc package.


%package doc
Summary: doc components for the krdc package.
Group: Documentation

%description doc
doc components for the krdc package.


%package lib
Summary: lib components for the krdc package.
Group: Libraries
Requires: krdc-data = %{version}-%{release}
Requires: krdc-license = %{version}-%{release}

%description lib
lib components for the krdc package.


%package license
Summary: license components for the krdc package.
Group: Default

%description license
license components for the krdc package.


%package locales
Summary: locales components for the krdc package.
Group: Default

%description locales
locales components for the krdc package.


%prep
%setup -q -n krdc-21.08.1
cd %{_builddir}/krdc-21.08.1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1630961872
mkdir -p clr-build
pushd clr-build
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=auto "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=auto "
%cmake ..
make  %{?_smp_mflags}
popd

%install
export SOURCE_DATE_EPOCH=1630961872
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/krdc
cp %{_builddir}/krdc-21.08.1/CMakePresets.json.license %{buildroot}/usr/share/package-licenses/krdc/29fb05b49e12a380545499938c4879440bd8851e
cp %{_builddir}/krdc-21.08.1/LICENSES/BSD-3-Clause.txt %{buildroot}/usr/share/package-licenses/krdc/9950d3fdce1cff1f71212fb5abd31453c6ee2f8c
cp %{_builddir}/krdc-21.08.1/LICENSES/GFDL-1.2-or-later.txt %{buildroot}/usr/share/package-licenses/krdc/7697008f58568e61e7598e796eafc2a997503fde
cp %{_builddir}/krdc-21.08.1/LICENSES/GPL-2.0-or-later.txt %{buildroot}/usr/share/package-licenses/krdc/3e8971c6c5f16674958913a94a36b1ea7a00ac46
pushd clr-build
%make_install
popd
%find_lang krdc

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/krdc

%files data
%defattr(-,root,root,-)
/usr/share/applications/org.kde.krdc.desktop
/usr/share/config.kcfg/krdc.kcfg
/usr/share/kservicetypes5/krdc_plugin.desktop
/usr/share/metainfo/org.kde.krdc.appdata.xml
/usr/share/qlogging-categories5/krdc.categories

%files dev
%defattr(-,root,root,-)
/usr/include/krdc/hostpreferences.h
/usr/include/krdc/remoteview.h
/usr/include/krdc/remoteviewfactory.h
/usr/include/krdccore_export.h
/usr/lib64/libkrdccore.so

%files doc
%defattr(0644,root,root,0755)
/usr/share/doc/HTML/ca/krdc/index.cache.bz2
/usr/share/doc/HTML/ca/krdc/index.docbook
/usr/share/doc/HTML/de/krdc/address_input.png
/usr/share/doc/HTML/de/krdc/bookmarks_menu.png
/usr/share/doc/HTML/de/krdc/general_preferences.png
/usr/share/doc/HTML/de/krdc/index.cache.bz2
/usr/share/doc/HTML/de/krdc/index.docbook
/usr/share/doc/HTML/de/krdc/krdc_mainwindow.png
/usr/share/doc/HTML/de/krdc/password_entry.png
/usr/share/doc/HTML/de/krdc/rdp_preferences.png
/usr/share/doc/HTML/de/krdc/vnc_host_configuration.png
/usr/share/doc/HTML/de/krdc/vnc_preferences.png
/usr/share/doc/HTML/en/krdc/address_input.png
/usr/share/doc/HTML/en/krdc/bookmarks_menu.png
/usr/share/doc/HTML/en/krdc/general_preferences.png
/usr/share/doc/HTML/en/krdc/index.cache.bz2
/usr/share/doc/HTML/en/krdc/index.docbook
/usr/share/doc/HTML/en/krdc/krdc_mainwindow.png
/usr/share/doc/HTML/en/krdc/password_entry.png
/usr/share/doc/HTML/en/krdc/rdp_preferences.png
/usr/share/doc/HTML/en/krdc/view-fullscreen.png
/usr/share/doc/HTML/en/krdc/view-restore.png
/usr/share/doc/HTML/en/krdc/vnc_host_configuration.png
/usr/share/doc/HTML/en/krdc/vnc_preferences.png
/usr/share/doc/HTML/es/krdc/index.cache.bz2
/usr/share/doc/HTML/es/krdc/index.docbook
/usr/share/doc/HTML/et/krdc/index.cache.bz2
/usr/share/doc/HTML/et/krdc/index.docbook
/usr/share/doc/HTML/fr/krdc/address_input.png
/usr/share/doc/HTML/fr/krdc/bookmarks_menu.png
/usr/share/doc/HTML/fr/krdc/general_preferences.png
/usr/share/doc/HTML/fr/krdc/index.cache.bz2
/usr/share/doc/HTML/fr/krdc/index.docbook
/usr/share/doc/HTML/fr/krdc/krdc_mainwindow.png
/usr/share/doc/HTML/fr/krdc/rdp_preferences.png
/usr/share/doc/HTML/fr/krdc/vnc_host_configuration.png
/usr/share/doc/HTML/fr/krdc/vnc_preferences.png
/usr/share/doc/HTML/it/krdc/address_input.png
/usr/share/doc/HTML/it/krdc/bookmarks_menu.png
/usr/share/doc/HTML/it/krdc/general_preferences.png
/usr/share/doc/HTML/it/krdc/index.cache.bz2
/usr/share/doc/HTML/it/krdc/index.docbook
/usr/share/doc/HTML/it/krdc/krdc_mainwindow.png
/usr/share/doc/HTML/it/krdc/password_entry.png
/usr/share/doc/HTML/it/krdc/rdp_preferences.png
/usr/share/doc/HTML/it/krdc/vnc_host_configuration.png
/usr/share/doc/HTML/it/krdc/vnc_preferences.png
/usr/share/doc/HTML/nl/krdc/index.cache.bz2
/usr/share/doc/HTML/nl/krdc/index.docbook
/usr/share/doc/HTML/pl/krdc/bookmarks_menu.png
/usr/share/doc/HTML/pl/krdc/general_preferences.png
/usr/share/doc/HTML/pl/krdc/index.cache.bz2
/usr/share/doc/HTML/pl/krdc/index.docbook
/usr/share/doc/HTML/pl/krdc/krdc_mainwindow.png
/usr/share/doc/HTML/pl/krdc/rdp_preferences.png
/usr/share/doc/HTML/pl/krdc/view-fullscreen.png
/usr/share/doc/HTML/pl/krdc/view-restore.png
/usr/share/doc/HTML/pl/krdc/vnc_host_configuration.png
/usr/share/doc/HTML/pl/krdc/vnc_preferences.png
/usr/share/doc/HTML/pt/krdc/index.cache.bz2
/usr/share/doc/HTML/pt/krdc/index.docbook
/usr/share/doc/HTML/pt_BR/krdc/index.cache.bz2
/usr/share/doc/HTML/pt_BR/krdc/index.docbook
/usr/share/doc/HTML/ru/krdc/index.cache.bz2
/usr/share/doc/HTML/ru/krdc/index.docbook
/usr/share/doc/HTML/sr/krdc/index.cache.bz2
/usr/share/doc/HTML/sr/krdc/index.docbook
/usr/share/doc/HTML/sv/krdc/index.cache.bz2
/usr/share/doc/HTML/sv/krdc/index.docbook
/usr/share/doc/HTML/uk/krdc/index.cache.bz2
/usr/share/doc/HTML/uk/krdc/index.docbook

%files lib
%defattr(-,root,root,-)
/usr/lib64/libkrdccore.so.21.08.1
/usr/lib64/libkrdccore.so.5
/usr/lib64/qt5/plugins/krdc/libkrdc_testplugin.so

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/krdc/29fb05b49e12a380545499938c4879440bd8851e
/usr/share/package-licenses/krdc/3e8971c6c5f16674958913a94a36b1ea7a00ac46
/usr/share/package-licenses/krdc/7697008f58568e61e7598e796eafc2a997503fde
/usr/share/package-licenses/krdc/9950d3fdce1cff1f71212fb5abd31453c6ee2f8c

%files locales -f krdc.lang
%defattr(-,root,root,-)

