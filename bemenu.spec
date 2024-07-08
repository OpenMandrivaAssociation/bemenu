%define _disable_ld_no_undefined 1

Name:       bemenu
Version:    0.6.22
Release:    1
Summary:    Dynamic menu library and client program inspired by dmenu
License:    GPLv3+ and LGPLv3+
URL:        https://github.com/Cloudef/bemenu
Source0:    https://github.com/Cloudef/bemenu/releases/download/%{version}/bemenu-%{version}.tar.gz
 
BuildRequires:  gnupg2
BuildRequires:  make
BuildRequires:  pkgconfig(cairo)
BuildRequires:  pkgconfig(ncursesw)
BuildRequires:  pkgconfig(pango)
BuildRequires:  pkgconfig(pangocairo)
BuildRequires:  pkgconfig(wayland-client)
BuildRequires:  pkgconfig(wayland-egl)
BuildRequires:  pkgconfig(wayland-protocols)
BuildRequires:  pkgconfig(wayland-server)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xinerama)
BuildRequires:  pkgconfig(xkbcommon)
BuildRequires:  scdoc
 
%description
%{summary}.
 
%package devel
Summary: Development files for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}
 
%description devel
Development files for extending %{name}.
 
%prep
%autosetup -p1
 
%build
%set_build_flags
%make_build   PREFIX='%{_prefix}' libdir='/%{_lib}'
 
%install
%make_install PREFIX='%{_prefix}' libdir='/%{_lib}'
 
%files
%doc README.md
%license LICENSE-CLIENT LICENSE-LIB
%{_bindir}/%{name}
%{_bindir}/%{name}-run
%{_mandir}/man1/%{name}*.1*
# Long live escaping! %%%% resolves to %%; ${v%%.*} strips everything after first dot
%{_libdir}/lib%{name}.so.%(v=%{version}; echo ${v%%%%.*})
%{_libdir}/lib%{name}.so.%{version}
%dir %{_libdir}/%{name}
%{_libdir}/%{name}/%{name}-renderer-curses.so
%{_libdir}/%{name}/%{name}-renderer-wayland.so
%{_libdir}/%{name}/%{name}-renderer-x11.so
 
%files devel
%doc README.md
%{_includedir}/%{name}.h
%{_libdir}/lib%{name}.so
%dir %{_libdir}/pkgconfig
%{_libdir}/pkgconfig/%{name}.pc
