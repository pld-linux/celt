Summary:	CELT low-latency audio codec
Summary(pl.UTF-8):	CELT - kodek dźwiękowy o małym opóźnieniu
Name:		celt
Version:	0.11.3
Release:	1
License:	BSD
Group:		Libraries
Source0:	http://downloads.xiph.org/releases/celt/%{name}-%{version}.tar.gz
# Source0-md5:	5511732a426cc42bf986ca79b5cdd02f
URL:		http://celt-codec.org/
# for tools
BuildRequires:	libogg-devel
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
%doc COPYING README TODO
%attr(755,root,root) %{_bindir}/celtdec
%attr(755,root,root) %{_bindir}/celtenc
%attr(755,root,root) %{_libdir}/libcelt0.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libcelt0.so.2

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libcelt0.so
%{_libdir}/libcelt0.la
%{_includedir}/celt
%{_pkgconfigdir}/celt.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/libcelt0.a
