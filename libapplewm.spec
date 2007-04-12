%define libapplewm %mklibname applewm 7
Name: libapplewm
Summary: The AppleWM Library
Version: 1.0.0
Release: %mkrel 3
Group: Development/X11
License: MIT
URL: http://xorg.freedesktop.org
Source0: http://xorg.freedesktop.org/releases/individual/lib/libAppleWM-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-root

BuildRequires: libx11-devel >= 1.0.0
BuildRequires: libxext-devel >= 1.0.0
BuildRequires: x11-proto-devel >= 1.0.0
BuildRequires: x11-util-macros >= 1.0.1

%description
libapplewm is a simple library designed to interface with the Apple-WM 
extension. This extension allows X window managers to better interact 
with the Mac OS X Aqua user interface when running X11 in a rootless mode.

#-----------------------------------------------------------

%package -n %{libapplewm}
Summary:  The AppleWM Library
Group: Development/X11
Conflicts: libxorg-x11 < 7.0
Provides: %{name} = %{version}

%description -n %{libapplewm}
libapplewm is a simple library designed to interface with the Apple-WM 
extension. This extension allows X window managers to better interact 
with the Mac OS X Aqua user interface when running X11 in a rootless mode.

#-----------------------------------------------------------

%package -n %{libapplewm}-devel
Summary: Development files for %{name}
Group: Development/X11
Requires: %{libapplewm} = %{version}-%{release}
Provides: libapplewm-devel = %{version}-%{release}
Conflicts: libxorg-x11-devel < 7.0

%description -n %{libapplewm}-devel
Development files for %{name}

%files -n %{libapplewm}-devel
%defattr(-,root,root)
%{_libdir}/libAppleWM.so
%{_libdir}/libAppleWM.la
%{_libdir}/pkgconfig/applewm.pc
%{_mandir}/man3/AppleWM.3.bz2

#-----------------------------------------------------------

%package -n %{libapplewm}-static-devel
Summary: Static development files for %{name}
Group: Development/X11
Requires: %{libapplewm}-devel >= %{version}
Provides: libapplewm-static-devel = %{version}-%{release}
Conflicts: libxorg-x11-static-devel < 7.0

%description -n %{libapplewm}-static-devel
Static development files for %{name}

%files -n %{libapplewm}-static-devel
%defattr(-,root,root)
%{_libdir}/libAppleWM.a

#-----------------------------------------------------------

%prep
%setup -q -n libAppleWM-%{version}

%build
%configure2_5x	--x-includes=%{_includedir}\
		--x-libraries=%{_libdir}

%make

%install
rm -rf %{buildroot}
rm -rf %{buildroot}
%makeinstall_std

%clean
rm -rf %{buildroot}

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files -n %{libapplewm}
%defattr(-,root,root)
%{_libdir}/libAppleWM.so.7
%{_libdir}/libAppleWM.so.7.0.0


