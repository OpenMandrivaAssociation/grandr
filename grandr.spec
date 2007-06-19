Name: grandr
Version: 0.1
Release: %mkrel 1
Summary: Interface to RandR extension
Group: System/X11
Source: http://xorg.freedesktop.org/releases/individual/app/%{name}-%{version}.tar.bz2
Patch0: grandr-0.1-strcmp.patch
License: MIT
BuildRoot: %{_tmppath}/%{name}-root

BuildRequires: libx11-devel >= 1.0.0
BuildRequires: libxrandr-devel >= 1.1.0.2
BuildRequires: libxrender-devel >= 0.9.0.2
BuildRequires: x11-util-macros >= 1.0.1

%description
grandr is used to set the screen size, orientation and/or reflection using the
RandR extension.

%prep
%setup -q -n %{name}-%{version}
%patch0 -p1 -b .strcmp

%build
%configure2_5x	--x-includes=%{_includedir}\
		--x-libraries=%{_libdir}

%make

%install
rm -rf %{buildroot}
%makeinstall_std

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%{_bindir}/grandr
#%{_mandir}/man1/grandr.1x.bz2