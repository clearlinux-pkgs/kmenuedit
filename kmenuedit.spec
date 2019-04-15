#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0xEC94D18F7F05997E (jr@jriddell.org)
#
Name     : kmenuedit
Version  : 5.15.4
Release  : 16
URL      : https://download.kde.org/stable/plasma/5.15.4/kmenuedit-5.15.4.tar.xz
Source0  : https://download.kde.org/stable/plasma/5.15.4/kmenuedit-5.15.4.tar.xz
Source99 : https://download.kde.org/stable/plasma/5.15.4/kmenuedit-5.15.4.tar.xz.sig
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
%setup -q -n kmenuedit-5.15.4

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1555337532
mkdir -p clr-build
pushd clr-build
%cmake ..
make  %{?_smp_mflags}
popd

%install
export SOURCE_DATE_EPOCH=1555337532
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/kmenuedit
cp COPYING %{buildroot}/usr/share/package-licenses/kmenuedit/COPYING
cp COPYING.DOC %{buildroot}/usr/share/package-licenses/kmenuedit/COPYING.DOC
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
/usr/share/xdg/kmenuedit.categories

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
/usr/share/package-licenses/kmenuedit/COPYING
/usr/share/package-licenses/kmenuedit/COPYING.DOC

%files locales -f kmenuedit.lang
%defattr(-,root,root,-)

