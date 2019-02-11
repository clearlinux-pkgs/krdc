#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0xDBD2CE893E2D1C87 (cfeck@kde.org)
#
Name     : krdc
Version  : 18.12.2
Release  : 2
URL      : https://download.kde.org/stable/applications/18.12.2/src/krdc-18.12.2.tar.xz
Source0  : https://download.kde.org/stable/applications/18.12.2/src/krdc-18.12.2.tar.xz
Source99 : https://download.kde.org/stable/applications/18.12.2/src/krdc-18.12.2.tar.xz.sig
Summary  : No detailed summary available
Group    : Development/Tools
License  : BSD-3-Clause GFDL-1.2 GPL-2.0 LGPL-2.1
Requires: krdc-bin = %{version}-%{release}
Requires: krdc-data = %{version}-%{release}
Requires: krdc-lib = %{version}-%{release}
Requires: krdc-license = %{version}-%{release}
Requires: krdc-locales = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : buildreq-kde
BuildRequires : buildreq-qmake
BuildRequires : kdnssd-dev
BuildRequires : knotifyconfig-dev
BuildRequires : libssh-dev

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
%setup -q -n krdc-18.12.2

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1549873392
mkdir -p clr-build
pushd clr-build
%cmake ..
make  %{?_smp_mflags}
popd

%install
export SOURCE_DATE_EPOCH=1549873392
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/krdc
cp COPYING %{buildroot}/usr/share/package-licenses/krdc/COPYING
cp COPYING.DOC %{buildroot}/usr/share/package-licenses/krdc/COPYING.DOC
cp COPYING.LIB %{buildroot}/usr/share/package-licenses/krdc/COPYING.LIB
cp cmake/modules/COPYING-CMAKE-SCRIPTS %{buildroot}/usr/share/package-licenses/krdc/cmake_modules_COPYING-CMAKE-SCRIPTS
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
/usr/share/krdc/pics/pointcursor.png
/usr/share/krdc/pics/pointcursormask.png
/usr/share/kxmlgui5/krdc/krdcui.rc
/usr/share/metainfo/org.kde.krdc.appdata.xml

%files dev
%defattr(-,root,root,-)
/usr/include/*.h
/usr/include/krdc/hostpreferences.h
/usr/include/krdc/remoteview.h
/usr/include/krdc/remoteviewfactory.h
/usr/lib64/libkrdccore.so

%files doc
%defattr(0644,root,root,0755)
/usr/share/doc/HTML/ca/krdc/index.cache.bz2
/usr/share/doc/HTML/ca/krdc/index.docbook
/usr/share/doc/HTML/ca/krdc/view-fullscreen.png
/usr/share/doc/HTML/ca/krdc/view-restore.png
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
/usr/share/doc/HTML/it/krdc/index.cache.bz2
/usr/share/doc/HTML/it/krdc/index.docbook
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
/usr/share/doc/HTML/uk/krdc/index.cache.bz2
/usr/share/doc/HTML/uk/krdc/index.docbook

%files lib
%defattr(-,root,root,-)
/usr/lib64/libkrdccore.so.18.12.2
/usr/lib64/libkrdccore.so.5
/usr/lib64/qt5/plugins/krdc/libkrdc_testplugin.so

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/krdc/COPYING
/usr/share/package-licenses/krdc/COPYING.DOC
/usr/share/package-licenses/krdc/COPYING.LIB
/usr/share/package-licenses/krdc/cmake_modules_COPYING-CMAKE-SCRIPTS

%files locales -f krdc.lang
%defattr(-,root,root,-)

