Summary:	Layer on top of PKCS#11 API to make using PKCS#11 implementations easier
Summary(pl.UTF-8):	Warstwa powyżej API PKCS#11 ułatwiająca używanie implementacji PKCS#11
Name:		libp11
Version:	0.2.4
Release:	1
License:	LGPL v2.1+
Group:		Libraries
Source0:	http://www.opensc-project.org/files/libp11/%{name}-%{version}.tar.gz
# Source0-md5:	9e2c5cbececde245e2d2f535bd49ce35
URL:		http://www.opensc-project.org/libp11/
BuildRequires:	libltdl-devel
BuildRequires:	openssl-devel >= 0.9.7
BuildRequires:	pkgconfig
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Libp11 is a library implementing a small layer on top of PKCS#11 API
to make using PKCS#11 implementations easier.

%description -l pl.UTF-8
Libp11 to biblioteka implementująca niewielką warstwę na wierzchu API
PKCS#11 mająca ułatwić używanie implementacji PKCS#11.

%package devel
Summary:	Header files for libp11 library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki libp11
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	libltdl-devel
Requires:	openssl-devel >= 0.9.7

%description devel
Header files for libp11 library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki libp11.

%package static
Summary:	Static libp11 library
Summary(pl.UTF-8):	Statyczna biblioteka libp11
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static libp11 library.

%description static -l pl.UTF-8
Statyczna biblioteka libp11.

%prep
%setup -q

%build
%configure \
	--enable-api-doc
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
cp -af examples/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc NEWS doc/{README,nonpersistent/wiki.out/*}
%attr(755,root,root) %{_libdir}/libp11.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libp11.so.0

%files devel
%defattr(644,root,root,755)
%doc doc/api.out/html/*
%attr(755,root,root) %{_libdir}/libp11.so
%{_libdir}/libp11.la
%{_includedir}/libp11.h
%{_pkgconfigdir}/libp11.pc
%{_examplesdir}/%{name}-%{version}

%files static
%defattr(644,root,root,755)
%{_libdir}/libp11.a
