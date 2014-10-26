#
# Conditional build:
#
%define		qtver		5.3.1

Summary:	lxqt-mount - libraries
Summary(pl.UTF-8):	lxqt-mount - biblioteki
Name:		liblxqt-mount
Version:	0.8.0
Release:	0.2
License:	GPLv2 and LGPL-2.1+
Group:		X11/Libraries
Source0:	http://lxqt.org/downloads/lxqt/%{version}/%{name}-%{version}.tar.xz
# Source0-md5:	0d12418bb26fb4f630895231e5ecaffb
URL:		http://www.lxqt.org/
BuildRequires:	Qt5Core-devel >= %{qtver}
BuildRequires:	Qt5DBus-devel >= %{qtver}
BuildRequires:	Qt5Gui-devel >= %{qtver}
BuildRequires:	liblxqt-devel >= 0.8.0
BuildRequires:	cmake >= 2.8.3
BuildRequires:	xz-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
lxqt-mount - libraries.

%package devel
Summary:	liblxqt-mount - header files and development documentation
Summary(pl.UTF-8):	liblxqt-mount - pliki nagłówkowe i dokumentacja do lxqt-mount
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	Qt5Core-devel >= %{qtver}
Requires:	Qt5DBus-devel >= %{qtver}
Requires:	Qt5Gui-devel >= %{qtver}

%description devel
This package contains header files and development documentation for
lxqt-mount.

%description devel -l pl.UTF-8
Pakiet ten zawiera pliki nagłówkowe i dokumentację potrzebną przy
pisaniu własnych programów wykorzystujących lxqt-mount.

%prep
%setup -q

%build
install -d build
cd build
%cmake \
    -DUSE_QT5=ON \
	../

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%ghost %{_libdir}/liblxqtmount-qt5.so.0
%attr(755,root,root) %{_libdir}/liblxqtmount-qt5.so.*.*.*

%files devel
%defattr(644,root,root,755)
%{_includedir}/lxqtmount-qt5
%{_libdir}/liblxqtmount-qt5.so
%{_pkgconfigdir}/lxqtmount-qt5.pc
%{_datadir}/cmake/lxqtmount-qt5
