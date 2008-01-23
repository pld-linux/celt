Summary:	CELT low-latency audio codec
Summary(pl.UTF-8):	CELT - kodek dźwiękowy o małym opóźnieniu
Name:		celt
Version:	0.0.2
Release:	0.1
License:	BSD
Group:		Libraries
Source0:	http://downloads.xiph.org/releases/celt/%{name}-%{version}.tar.gz
# Source0-md5:	e2d3c73b23d40840a7d81dfe30ca5d5f
# author's blog for now
URL:		http://jmspeex.livejournal.com/
#BuildRequires:	libogg-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
CELT is an attempt to write a low-latency audio codec.

%description -l pl.UTF-8
CELT to próba napisania kodeka dźwiękowego o małym opóźnieniu.

%package devel
Summary:	Header files for CELT libraries
Summary(pl.UTF-8):	Pliki nagłówkowe bibliotek CELT
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for CELT libraries.

%description devel -l pl.UTF-8
Pliki nagłówkowe bibliotek CELT.

%package static
Summary:	Static CELT libraries
Summary(pl.UTF-8):	Statyczne biblioteki CELT
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static CELT libraries.

%description static -l pl.UTF-8
Statyczne biblioteki CELT.

%prep
%setup -q

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc COPYING README
#%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_libdir}/libcelt.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libcelt.so.0
%attr(755,root,root) %{_libdir}/libentcode.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libentcode.so.0

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libcelt.so
%attr(755,root,root) %{_libdir}/libentcode.so
%{_libdir}/libcelt.la
%{_libdir}/libentcode.la
#%{_includedir}/foo
#%{_pkgconfigdir}/*.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/libcelt.a
%{_libdir}/libentcode.a
