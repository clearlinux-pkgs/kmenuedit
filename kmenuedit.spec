#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: cmake
# autospec version: v10
# autospec commit: 5905be9
#
# Source0 file verified with key 0xD7574483BB57B18D (jr@jriddell.org)
#
Name     : kmenuedit
Version  : 6.0.4
Release  : 97
URL      : https://download.kde.org/stable/plasma/6.0.4/kmenuedit-6.0.4.tar.xz
Source0  : https://download.kde.org/stable/plasma/6.0.4/kmenuedit-6.0.4.tar.xz
Source1  : https://download.kde.org/stable/plasma/6.0.4/kmenuedit-6.0.4.tar.xz.sig
Source2  : D7574483BB57B18D.pkey
Summary  : No detailed summary available
Group    : Development/Tools
License  : CC0-1.0 GPL-2.0
Requires: kmenuedit-bin = %{version}-%{release}
Requires: kmenuedit-data = %{version}-%{release}
Requires: kmenuedit-license = %{version}-%{release}
Requires: kmenuedit-locales = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : buildreq-kde
BuildRequires : extra-cmake-modules-data
BuildRequires : gnupg
BuildRequires : kdbusaddons-dev
BuildRequires : kglobalaccel-dev
BuildRequires : ki18n-dev
BuildRequires : kio-dev
BuildRequires : qt6base-dev
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

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
mkdir .gnupg
chmod 700 .gnupg
gpg --homedir .gnupg --import %{SOURCE2}
gpg --homedir .gnupg --status-fd 1 --verify %{SOURCE1} %{SOURCE0} > gpg.status
grep -E '^\[GNUPG:\] (GOODSIG|EXPKEYSIG) D7574483BB57B18D' gpg.status
%setup -q -n kmenuedit-6.0.4
cd %{_builddir}/kmenuedit-6.0.4

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1713289907
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
%cmake ..
make  %{?_smp_mflags}
popd
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
%cmake ..
make  %{?_smp_mflags}
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
export SOURCE_DATE_EPOCH=1713289907
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/kmenuedit
cp %{_builddir}/kmenuedit-%{version}/LICENSES/CC0-1.0.txt %{buildroot}/usr/share/package-licenses/kmenuedit/82da472f6d00dc5f0a651f33ebb320aa9c7b08d0 || :
cp %{_builddir}/kmenuedit-%{version}/LICENSES/GPL-2.0-only.txt %{buildroot}/usr/share/package-licenses/kmenuedit/3e8971c6c5f16674958913a94a36b1ea7a00ac46 || :
cp %{_builddir}/kmenuedit-%{version}/LICENSES/GPL-2.0-or-later.txt %{buildroot}/usr/share/package-licenses/kmenuedit/e712eadfab0d2357c0f50f599ef35ee0d87534cb || :
export GOAMD64=v2
GOAMD64=v3
pushd clr-build-avx2
%make_install_v3  || :
popd
GOAMD64=v2
pushd clr-build
%make_install
popd
%find_lang kmenuedit
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/V3/usr/bin/kmenuedit
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
/usr/share/metainfo/org.kde.kmenuedit.appdata.xml
/usr/share/qlogging-categories6/kmenuedit.categories

%files doc
%defattr(0644,root,root,0755)
/usr/share/doc/HTML/ca/kmenuedit/done.png
/usr/share/doc/HTML/ca/kmenuedit/index.cache.bz2
/usr/share/doc/HTML/ca/kmenuedit/index.docbook
/usr/share/doc/HTML/ca/kmenuedit/itemname.png
/usr/share/doc/HTML/ca/kmenuedit/new.png
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
/usr/share/doc/HTML/es/kmenuedit/index.cache.bz2
/usr/share/doc/HTML/es/kmenuedit/index.docbook
/usr/share/doc/HTML/fr/kmenuedit/index.cache.bz2
/usr/share/doc/HTML/fr/kmenuedit/index.docbook
/usr/share/doc/HTML/id/kmenuedit/index.cache.bz2
/usr/share/doc/HTML/id/kmenuedit/index.docbook
/usr/share/doc/HTML/it/kmenuedit/done.png
/usr/share/doc/HTML/it/kmenuedit/index.cache.bz2
/usr/share/doc/HTML/it/kmenuedit/index.docbook
/usr/share/doc/HTML/it/kmenuedit/itemname.png
/usr/share/doc/HTML/it/kmenuedit/new.png
/usr/share/doc/HTML/it/kmenuedit/selecticon.png
/usr/share/doc/HTML/it/kmenuedit/selectinternet.png
/usr/share/doc/HTML/it/kmenuedit/toolbars-toolbar.png
/usr/share/doc/HTML/nl/kmenuedit/index.cache.bz2
/usr/share/doc/HTML/nl/kmenuedit/index.docbook
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
/usr/share/doc/HTML/tr/kmenuedit/index.cache.bz2
/usr/share/doc/HTML/tr/kmenuedit/index.docbook
/usr/share/doc/HTML/uk/kmenuedit/done.png
/usr/share/doc/HTML/uk/kmenuedit/index.cache.bz2
/usr/share/doc/HTML/uk/kmenuedit/index.docbook
/usr/share/doc/HTML/uk/kmenuedit/itemname.png
/usr/share/doc/HTML/uk/kmenuedit/new.png
/usr/share/doc/HTML/uk/kmenuedit/selecticon.png
/usr/share/doc/HTML/uk/kmenuedit/selectinternet.png

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/kmenuedit/3e8971c6c5f16674958913a94a36b1ea7a00ac46
/usr/share/package-licenses/kmenuedit/82da472f6d00dc5f0a651f33ebb320aa9c7b08d0
/usr/share/package-licenses/kmenuedit/e712eadfab0d2357c0f50f599ef35ee0d87534cb

%files locales -f kmenuedit.lang
%defattr(-,root,root,-)

