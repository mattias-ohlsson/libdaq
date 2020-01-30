Name:           libdaq
Version:        
Release:        1%{?dist}
Summary:        

License:        
URL:            
Source0:        

BuildRequires:  
Requires:       

%description


%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%prep
%autosetup


%build
%configure --disable-static
%make_build


%install
rm -rf $RPM_BUILD_ROOT
%make_install
find $RPM_BUILD_ROOT -name '*.la' -exec rm -f {} ';'


%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig


%files
%license add-license-file-here
%doc add-main-docs-here
%{_libdir}/*.so.*

%files devel
%doc add-devel-docs-here
%{_includedir}/*
%{_libdir}/*.so


%changelog
* Thu Jan 30 2020 Mattias Ohlsson <mattias.ohlsson@inprose.com>
- 
