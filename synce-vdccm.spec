%define name     synce-vdccm
%define shortname vdccm
%define release  %mkrel 1
%define version  0.10.1

%define major 0
%define libname %mklibname %shortname %major

Summary: SynCE: Communication application
Name: %{name}
Version: %{version}
Release: %{release}
License: MIT
Group: System/Libraries
Source: http://kent.dl.sourceforge.net/sourceforge/synce/%{shortname}-%{version}.tar.gz
Patch0: vdccm-dont-chown.patch
URL: http://synce.sourceforge.net/
BuildRequires: libsynce-devel >= 0.10.0
#BuildRequires: hal-devel
Obsoletes: %libname
Obsoletes: %libname-devel
Conflicts: synce-kde < 0.9.1-2

%description
%{shortname} is part of the SynCE project:

%prep
%setup -q -n %{shortname}-%{version}
%patch0 -p0 -b .dont-chown

%build
autoreconf -fi
%configure2_5x --with-libsynce=%{_prefix}
%make

%install
rm -rf %buildroot
%makeinstall_std

%files
%defattr(-,root,root)
%doc README TODO
%{_bindir}/*
%{_mandir}/man1/*
