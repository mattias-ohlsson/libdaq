Name:           libdaq
Version:        3.0.0
Release:        1.alpha3%{?dist}
Summary:        Data Acquisition Library

License:        GPLv2+
URL:            https://github.com/snort3/libdaq
Source0:        https://github.com/snort3/libdaq/archive/v%{version}-alpha3.tar.gz

BuildRequires:  libnfnetlink-devel
BuildRequires:  libnetfilter_queue-devel
BuildRequires:  libmnl-devel
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libtool
BuildRequires:  gcc-c++
BuildRequires:  make
BuildRequires:  libpcap-devel

%description
The DAQ replaces direct calls to libpcap functions with an abstraction layer
that facilitates operation on a variety of hardware and software interfaces
without requiring changes to Snort.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package        modules
Summary:        Dynamic DAQ modules

%description    modules
Dynamic DAQ modules.

%prep
%autosetup -n libdaq-3.0.0-alpha3

%build
./bootstrap
%configure --disable-static
%make_build

%install
rm -rf $RPM_BUILD_ROOT
%make_install
find $RPM_BUILD_ROOT -name '*.la' -exec rm -f {} ';'

# get rid of static libraries
find $RPM_BUILD_ROOT -type f -name "*.a" -delete -print

find $RPM_BUILD_ROOT -type f -name "daqtest-static" -delete -print

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%license COPYING LICENSE
%doc README.md
%{_bindir}/daqtest
%{_libdir}/*.so.*

%files devel
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc

%files modules
%dir %{_libdir}/daq
%{_libdir}/daq/*.so
%license COPYING LICENSE

%changelog
* Thu Jan 30 2020 Mattias Ohlsson <mattias.ohlsson@inprose.com> - 3.0.0-1.alpha3
- Initial build
