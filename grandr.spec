Name: grandr
Version: 0.1
Release: %mkrel 8
Summary: Interface to RandR extension
Group: System/X11
URL:    http://www.x.org/
Source: http://xorg.freedesktop.org/releases/individual/app/%{name}-%{version}.tar.bz2
# These are all upstream patches since the 0.1 release:
Patch0: grandr-upstream-01-fix-segfault-at-startup.patch
Patch1: grandr-upstream-02-license-was-gpl-not-mit.patch
Patch2: grandr-upstream-03-fix-typo-output.patch
Patch3: grandr-upstream-04-exit-when-window-is-closed.patch
Patch4: grandr-upstream-05-fix-typo-screen.patch
# This was taken from Debian, should fix #54985
# http://git.debian.org/?p=pkg-xorg/app/grandr.git
Patch5: grandr-debian-01-fix-segfault-when-click-monitor.patch
# This one is from Mandriva (read its header for a description of the problem)
Patch6: grandr-mandriva-synchronize-before-and-after-apply.patch

License: MIT
BuildRoot: %{_tmppath}/%{name}-root

BuildRequires: libx11-devel >= 1.0.0
BuildRequires: libxrandr-devel >= 1.1.0.2
BuildRequires: libxrender-devel >= 0.9.0.2
BuildRequires: x11-util-macros >= 1.0.1
BuildRequires: libgtk+2-devel
BuildRequires: libGConf2-devel

%description
grandr is used to set the screen size, orientation and/or reflection using the
RandR extension.

%prep
%setup -q -n %{name}-%{version}
%apply_patches

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
#%{_mandir}/man1/grandr.*
