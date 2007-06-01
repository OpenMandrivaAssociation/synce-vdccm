%define name     synce-vdccm
%define shortname vdccm
%define release  %mkrel 1
%define version  0.10.0

%define major 0

%define libname %mklibname %shortname %major

Summary: SynCE: Communication application
Name: %{name}
Version: %{version}
Release: %{release}
License: MIT
Group: System/Libraries
Source: %{name}-%{version}.tar.bz2
Patch0: vdccm-dont-chown.patch
URL: http://synce.sourceforge.net/
Buildroot: %{_tmppath}/%name-root
BuildRequires: libsynce-devel = %{version}
BuildRequires: hal-devel
Obsoletes: %libname
Obsoletes: %libname-devel

%description
%{shortname} is part of the SynCE project:

#%package -n %libname
#Group: System/Libraries
#Summary: SynCE: Communication application
#Provides: lib%{shortname} = %{version}-%{release}
#Conflicts: %{_lib}synce0 < 0.9.3

#%description -n %libname
#%{shortname} is part of the SynCE project

#%package -n %libname-devel
#Group: System/Libraries
#Summary: SynCE: Communication application
#Provides: lib%{shortname}-devel = %{version}-%{release}
#Requires: %{libname} = %{version}-%{release}
#Conflicts: %{_lib}synce0-devel < 0.9.3

#%description -n %libname-devel
#%{shortname} is part of the SynCE project

%prep
%setup -q -n %{shortname}-%{version}
%patch0 -p0 -b .dont-chown

%build
automake
autoconf
%configure --with-libsynce=%{_prefix}
%make

%install
%makeinstall

%post -n %libname -p /sbin/ldconfig
%postun -n %libname -p /sbin/ldconfig

%files
%defattr(-,root,root)
%doc README TODO
%{_bindir}/*
%{_mandir}/man1/*

#%files -n %{libname}
#%defattr(-,root,root)
#%_libdir/*.so.*

#%files -n %{libname}-devel
#%defattr(-,root,root)
#%_libdir/*.so
#%_libdir/*.la
