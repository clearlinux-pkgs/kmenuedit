#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0xEC94D18F7F05997E (jr@jriddell.org)
#
Name     : kmenuedit
Version  : 5.17.1
Release  : 26
URL      : https://download.kde.org/stable/plasma/5.17.1/kmenuedit-5.17.1.tar.xz
Source0  : https://download.kde.org/stable/plasma/5.17.1/kmenuedit-5.17.1.tar.xz
Source1 : https://download.kde.org/stable/plasma/5.17.1/kmenuedit-5.17.1.tar.xz.sig
Summary  : KDE menu editor
Group    : Development/Tools
License  : GFDL-1.2 GPL-2.0
Requires: kmenuedit-bin = %{version}-%{release}
Requires: kmenuedit-data = %{version}-%{release}
Requires: kmenuedit-lib = %{version}-%{release}
Requires: kmenuedit-license = %{version}-%{release}
Requires: kmenuedit-locales = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : buildreq-kde
BuildRequires : util-linux

%description
No detailed description available

%package bin
Summary: bin components for the kmenuedit package.
Group: Binaries
Requires: kmenuedit-data = %{version}-%{release}
Requires: kmenuedit-license = %{version}-%{release}

%description bin
bin components for the kmenuedit package.


%package data
Summary: data components for the kmenuedit package.
Group: Data

%description data
data components for the kmenuedit package.


%package doc
Summary: doc components for the kmenuedit package.
Group: Documentation

%description doc
doc components for the kmenuedit package.


%package lib
Summary: lib components for the kmenuedit package.
Group: Libraries
Requires: kmenuedit-data = %{version}-%{release}
Requires: kmenuedit-license = %{version}-%{release}

%description lib
lib components for the kmenuedit package.


%package license
Summary: license components for the kmenuedit package.
Group: Default

%description license
license components for the kmenuedit package.


%package locales
Summary: locales components for the kmenuedit package.
Group: Default

%description locales
locales components for the kmenuedit package.


%prep
%setup -q -n kmenuedit-5.17.1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1571798355
mkdir -p clr-build
pushd clr-build
# -Werror is for werrorists
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
%cmake ..
make  %{?_smp_mflags}  VERBOSE=1
popd

%install
export SOURCE_DATE_EPOCH=1571798355
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/kmenuedit
cp %{_builddir}/kmenuedit-5.17.1/COPYING %{buildroot}/usr/share/package-licenses/kmenuedit/7c203dee3a03037da436df03c4b25b659c073976
cp %{_builddir}/kmenuedit-5.17.1/COPYING.DOC %{buildroot}/usr/share/package-licenses/kmenuedit/bd75d59f9d7d9731bfabdc48ecd19e704d218e38
pushd clr-build
%make_install
popd
%find_lang kmenuedit

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/kmenuedit

%files data
%defattr(-,root,root,-)
/usr/share/applications/org.kde.kmenuedit.desktop
/usr/share/icons/hicolor/16x16/apps/kmenuedit.png
/usr/share/icons/hicolor/22x22/apps/kmenuedit.png
/usr/share/icons/hicolor/32x32/apps/kmenuedit.png
/usr/share/icons/hicolor/48x48/apps/kmenuedit.png
/usr/share/kmenuedit/icons/hicolor/22x22/actions/menu_new.png
/usr/share/kmenuedit/icons/hicolor/22x22/actions/menu_new_sep.png
/usr/share/kmenuedit/icons/hicolor/32x32/actions/menu_new.png
/usr/share/kmenuedit/icons/hicolor/32x32/actions/menu_new_sep.png
/usr/share/kxmlgui5/kmenuedit/kmenueditui.rc
/usr/share/qlogging-categories5/kmenuedit.categories

%files doc
%defattr(0644,root,root,0755)
/usr/share/doc/HTML/ca/kmenuedit/done.png
/usr/share/doc/HTML/ca/kmenuedit/index.cache.bz2
/usr/share/doc/HTML/ca/kmenuedit/index.docbook
/usr/share/doc/HTML/ca/kmenuedit/itemname.png
/usr/share/doc/HTML/ca/kmenuedit/new.png
/usr/share/doc/HTML/ca/kmenuedit/reset.png
/usr/share/doc/HTML/ca/kmenuedit/selecticon.png
/usr/share/doc/HTML/ca/kmenuedit/selectinternet.png
/usr/share/doc/HTML/de/kmenuedit/index.cache.bz2
/usr/share/doc/HTML/de/kmenuedit/index.docbook
/usr/share/doc/HTML/en/kmenuedit/done.png
/usr/share/doc/HTML/en/kmenuedit/index.cache.bz2
/usr/share/doc/HTML/en/kmenuedit/index.docbook
/usr/share/doc/HTML/en/kmenuedit/itemname.png
/usr/share/doc/HTML/en/kmenuedit/new.png
/usr/share/doc/HTML/en/kmenuedit/reset.png
/usr/share/doc/HTML/en/kmenuedit/selecticon.png
/usr/share/doc/HTML/en/kmenuedit/selectinternet.png
/usr/share/doc/HTML/id/kmenuedit/index.cache.bz2
/usr/share/doc/HTML/id/kmenuedit/index.docbook
/usr/share/doc/HTML/it/kmenuedit/index.cache.bz2
/usr/share/doc/HTML/it/kmenuedit/index.docbook
/usr/share/doc/HTML/nl/kmenuedit/index.cache.bz2
/usr/share/doc/HTML/nl/kmenuedit/index.docbook
/usr/share/doc/HTML/pt/kmenuedit/index.cache.bz2
/usr/share/doc/HTML/pt/kmenuedit/index.docbook
/usr/share/doc/HTML/pt_BR/kmenuedit/done.png
/usr/share/doc/HTML/pt_BR/kmenuedit/index.cache.bz2
/usr/share/doc/HTML/pt_BR/kmenuedit/index.docbook
/usr/share/doc/HTML/pt_BR/kmenuedit/itemname.png
/usr/share/doc/HTML/pt_BR/kmenuedit/new.png
/usr/share/doc/HTML/pt_BR/kmenuedit/reset.png
/usr/share/doc/HTML/pt_BR/kmenuedit/selecticon.png
/usr/share/doc/HTML/pt_BR/kmenuedit/selectinternet.png
/usr/share/doc/HTML/ru/kmenuedit/done.png
/usr/share/doc/HTML/ru/kmenuedit/index.cache.bz2
/usr/share/doc/HTML/ru/kmenuedit/index.docbook
/usr/share/doc/HTML/ru/kmenuedit/itemname.png
/usr/share/doc/HTML/ru/kmenuedit/new.png
/usr/share/doc/HTML/ru/kmenuedit/selecticon.png
/usr/share/doc/HTML/ru/kmenuedit/selectinternet.png
/usr/share/doc/HTML/sv/kmenuedit/index.cache.bz2
/usr/share/doc/HTML/sv/kmenuedit/index.docbook
/usr/share/doc/HTML/uk/kmenuedit/done.png
/usr/share/doc/HTML/uk/kmenuedit/index.cache.bz2
/usr/share/doc/HTML/uk/kmenuedit/index.docbook
/usr/share/doc/HTML/uk/kmenuedit/itemname.png
/usr/share/doc/HTML/uk/kmenuedit/new.png
/usr/share/doc/HTML/uk/kmenuedit/selecticon.png
/usr/share/doc/HTML/uk/kmenuedit/selectinternet.png

%files lib
%defattr(-,root,root,-)
/usr/lib64/libkdeinit5_kmenuedit.so

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/kmenuedit/7c203dee3a03037da436df03c4b25b659c073976
/usr/share/package-licenses/kmenuedit/bd75d59f9d7d9731bfabdc48ecd19e704d218e38

%files locales -f kmenuedit.lang
%defattr(-,root,root,-)

