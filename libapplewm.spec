%define name		libapplewm
%define version		1.0.0
%define release		%mkrel 5

%define major		7
%define libname 	%mklibname applewm %major
%define develname	%mklibname applewm -d
%define staticname	%mklibname applewm -d -s

Name: %{name}
Summary: The AppleWM Library
Version: %{version}
Release: %{release}
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

%package -n %{libname}
Summary:  The AppleWM Library
Group: Development/X11
Conflicts: libxorg-x11 < 7.0
Provides: %{name} = %{version}

%description -n %{libname}
libapplewm is a simple library designed to interface with the Apple-WM 
extension. This extension allows X window managers to better interact 
with the Mac OS X Aqua user interface when running X11 in a rootless mode.

#-----------------------------------------------------------

%package -n %{develname}
Summary: Development files for %{name}
Group: Development/X11
Requires: %{libname} = %{version}-%{release}
Provides: %{name}-devel = %{version}-%{release}
Obsoletes: %mklibname applewm 7 -d
Conflicts: libxorg-x11-devel < 7.0

%description -n %{develname}
Development files for %{name}

%files -n %{develname}
%defattr(-,root,root)
%{_libdir}/*.so
%{_libdir}/*.la
%{_libdir}/pkgconfig/applewm.pc
%{_mandir}/man3/AppleWM.3*

#-----------------------------------------------------------

%package -n %{staticname}
Summary: Static development files for %{name}
Group: Development/X11
Requires: %{develname} >= %{version}
Provides: %{name}-static-devel = %{version}-%{release}
Obsoletes: %mklibname applewm 7 -d -s
Conflicts: libxorg-x11-static-devel < 7.0

%description -n %{staticname}
Static development files for %{name}

%files -n %{staticname}
%defattr(-,root,root)
%{_libdir}/*.a

#-----------------------------------------------------------

%prep
%setup -q -n libAppleWM-%{version}

%build
%configure2_5x	--x-includes=%{_includedir}\
		--x-libraries=%{_libdir}

%make

%install
rm -rf %{buildroot}
%makeinstall_std

%clean
rm -rf %{buildroot}

%post -n %{libname} -p /sbin/ldconfig
%postun -n %{libname} -p /sbin/ldconfig

%files -n %{libname}
%defattr(-,root,root)
%{_libdir}/*.so.%{major}*
