Summary:	Layer on top of PKCS#11 API to make using PKCS#11 implementations easier
Summary(pl):	Warstwa powy¿ej API PKCS#11 u³atwiaj±ca u¿ywanie implementacji PKCS#11
Name:		libp11
Version:	0.2.0
Release:	1
License:	LGPL v2.1+
Group:		Libraries
Source0:	http://www.opensc.org/files/%{name}-%{version}.tar.gz
# Source0-md5:	549803a368aa2b457ebcf9d5c7d36dfd
URL:		http://www.opensc.org/libp11/
BuildRequires:	libltdl-devel
BuildRequires:	openssl-devel
BuildRequires:	pkgconfig
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Libp11 is a library implementing a small layer on top of PKCS#11 API
to make using PKCS#11 implementations easier.

%description -l pl
Libp11 to biblioteka implementuj±ca niewielk± warstwê na wierzchu API
PKCS#11 maj±ca u³atwiæ u¿ywanie implementacji PKCS#11.

%package devel
Summary:	Header files for libp11 library
Summary(pl):	Pliki nag³ówkowe biblioteki libp11
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	libltdl-devel
Requires:	openssl-devel

%description devel
Header files for libp11 library.

%description devel -l pl
Pliki nag³ówkowe biblioteki libp11.

%package static
Summary:	Static libp11 library
Summary(pl):	Statyczna biblioteka libp11
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static libp11 library.

%description static -l pl
Statyczna biblioteka libp11.

%prep
%setup -q

%build
%configure
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
%doc doc/{README,*.html,*.css}
%attr(755,root,root) %{_libdir}/libp11.so.*.*.*

%files devel
%defattr(644,root,root,755)
%doc doc/api/*
%attr(755,root,root) %{_libdir}/libp11.so
%{_libdir}/libp11.la
%{_includedir}/libp11.h
%{_pkgconfigdir}/libp11.pc
%{_examplesdir}/%{name}-%{version}

%files static
%defattr(644,root,root,755)
%{_libdir}/libp11.a
