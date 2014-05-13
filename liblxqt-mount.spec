#
# Conditional build:
#
%define		qtver		4.8.5

Summary:	lxqt-mount - libraries
Summary(pl.UTF-8):	lxqt-mount - biblioteki
Name:		liblxqt-mount
Version:	0.7.0
Release:	0.1
License:	GPLv2 and LGPL-2.1+
Group:		X11/Libraries
Source0:	http://lxqt.org/downloads/lxqt/0.7.0/%{name}-%{version}.tar.xz
# Source0-md5:	195cdafc601bd2f798e87ef3d893a5ac
URL:		http://www.lxqt.org/
BuildRequires:	QtCore-devel >= %{qtver}
BuildRequires:	QtDBus-devel >= %{qtver}
BuildRequires:	QtGui-devel >= %{qtver}
BuildRequires:	liblxqt-devel >= 0.7.0
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
Requires:	QtCore-devel >= %{qtver}
Requires:	QtDBus-devel >= %{qtver}
Requires:	QtGui-devel >= %{qtver}

%description devel
This package contains header files and development documentation for
lxqt-mount.

%description devel -l pl.UTF-8
Pakiet ten zawiera pliki nagłówkowe i dokumentację potrzebną przy
pisaniu własnych programów wykorzystujących lxqt-mount.

%prep
%setup -q -c %{name}-%{version}

%build
install -d build
cd build
%cmake \
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
%ghost %{_libdir}/liblxqtmount.so.0
%attr(755,root,root) %{_libdir}/liblxqtmount.so.*.*.*

%files devel
%defattr(644,root,root,755)
%{_includedir}/lxqtmount
%{_libdir}/liblxqtmount.so
%{_pkgconfigdir}/lxqtmount.pc
%{_datadir}/cmake/lxqtmount
