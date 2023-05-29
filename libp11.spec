Summary:	Layer on top of PKCS#11 API to make using PKCS#11 implementations easier
Summary(pl.UTF-8):	Warstwa powyżej API PKCS#11 ułatwiająca używanie implementacji PKCS#11
Name:		libp11
Version:	0.4.12
Release:	1
License:	LGPL v2.1+
Group:		Libraries
#Source0Download: https://github.com/OpenSC/libp11/releases
Source0:	https://github.com/OpenSC/libp11/releases/download/%{name}-%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	2ec3c29523cc06ec60166b320c489c63
Patch0:		%{name}-openssl3.patch
URL:		https://github.com/OpenSC/libp11
BuildRequires:	doxygen
BuildRequires:	openssl-devel >= 3.0.0
# for proxy_module detection
BuildRequires:	p11-kit-devel
BuildRequires:	pkgconfig
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%undefine	__cxx

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
Requires:	openssl-devel >= 3.0.0

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

%package apidocs
Summary:	API documentation for libp11 library
Summary(pl.UTF-8):	Dokumentacja API biblioteki libp11
Group:		Documentation

%description apidocs
API documentation for libp11 library.

%description apidocs -l pl.UTF-8
Dokumentacja API biblioteki libp11.

%package -n openssl-engine-pkcs11
Summary:	PKCS#11 engine for OpenSSL
Summary(pl.UTF-8):	Silnik PKCS#11 dla OpenSSL-a
Group:		Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	openssl >= 3.0.0

%description -n openssl-engine-pkcs11
engine_pkcs11 is an implementation of an engine for OpenSSL. It can be
loaded using code, config file or command line and will pass any
function call by openssl to a PKCS#11 module. Engine_pkcs11 is meant
to be used with smart cards and software for using smart cards in
PKCS#11 format, such as OpenSC.

%description -n openssl-engine-pkcs11 -l pl.UTF-8
engine_pkcs11 to implementacja silnika dla OpenSSL-a. Może być
wczytany przy użyciu kodu, pliku konfiguracyjnego i linii poleceń;
przekazuje wszystkie wywołania funkcji openssl-a do modułu PKCS#11.
engine_pkcs11 jest przeznaczony do używania z kartami procesorowymi i
oprogramowaniem do używania kart procesorowych w formacie PKCS#11,
takim jak OpenSC.

%prep
%setup -q
%patch0 -p1

%build
%configure \
	--enable-api-doc \
	--disable-silent-rules \
	--with-enginesdir=/%{_lib}/engines-3
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
cp -af examples/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

# obsoleted by pkgconfig
%{__rm} $RPM_BUILD_ROOT%{_libdir}/libp11.la
# loadable module
%{__rm} $RPM_BUILD_ROOT/%{_lib}/engines-3/*.la
# packaged as %doc
%{__rm} -r $RPM_BUILD_ROOT%{_docdir}/libp11

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc NEWS README.md
%attr(755,root,root) %{_libdir}/libp11.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libp11.so.3

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libp11.so
%{_includedir}/libp11.h
%{_includedir}/p11_err.h
%{_pkgconfigdir}/libp11.pc
%{_examplesdir}/%{name}-%{version}

%files static
%defattr(644,root,root,755)
%{_libdir}/libp11.a

%files apidocs
%defattr(644,root,root,755)
%doc doc/api.out/html/*

%files -n openssl-engine-pkcs11
%defattr(644,root,root,755)
%attr(755,root,root) /%{_lib}/engines-3/libpkcs11.so
%attr(755,root,root) /%{_lib}/engines-3/pkcs11.so
