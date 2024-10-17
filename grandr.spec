Name: grandr
Version: 0.1
Release: 9
Summary: Interface to RandR extension
Group: System/X11
URL:    https://www.x.org/
Source0: http://xorg.freedesktop.org/releases/individual/app/%{name}-%{version}.tar.bz2
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

BuildRequires: pkgconfig(x11)
BuildRequires: pkgconfig(xrandr)
BuildRequires: pkgconfig(xrender)
BuildRequires: pkgconfig(xorg-macros)
BuildRequires: pkgconfig(gtk+-2.0)
BuildRequires: pkgconfig(gconf-2.0)

%description
grandr is used to set the screen size, orientation and/or reflection using the
RandR extension.

%prep
%setup -q -n %{name}-%{version}
%autopatch -p1

%build
export LIBS="-lX11 -lgthread-2.0"
%configure2_5x	--x-includes=%{_includedir}\
		--x-libraries=%{_libdir}

%make

%install
%makeinstall_std

%files
%defattr(-,root,root)
%{_bindir}/grandr
#%{_mandir}/man1/grandr.*


%changelog
* Sun Dec 05 2010 Oden Eriksson <oeriksson@mandriva.com> 0.1-8mdv2011.0
+ Revision: 610981
- rebuild

* Tue Jan 26 2010 Paulo Ricardo Zanoni <pzanoni@mandriva.com> 0.1-7mdv2010.1
+ Revision: 496768
- Add upstream patches with small fixes
- Add a Debian patch to fix bug #54985
- Add a patch to fix synchronization problems
  (that can only be seen after the fix for #54985)

* Fri Sep 04 2009 Thierry Vignaud <tv@mandriva.org> 0.1-6mdv2010.0
+ Revision: 429321
- rebuild

* Thu Jul 24 2008 Thierry Vignaud <tv@mandriva.org> 0.1-5mdv2009.0
+ Revision: 246623
- rebuild

* Tue Feb 12 2008 Paulo Andrade <pcpa@mandriva.com.br> 0.1-3mdv2008.1
+ Revision: 166385
- Revert to use upstream tarball, build requires and remove non mandatory local patches.

* Tue Jan 22 2008 Paulo Andrade <pcpa@mandriva.com.br> 0.1-2mdv2008.1
+ Revision: 156528
- Updated BuildRequires and resubmit package.

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request
    - add URL
    - fix man pages extension

* Tue Jun 19 2007 Gustavo Pichorim Boiko <boiko@mandriva.com> 0.1-1mdv2008.0
+ Revision: 41571
- Adding missing BuildRequires
- Import grandr

