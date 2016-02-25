Name:		rofi
Version: 0.15.12
Release:	1%{?dist}
Summary:	A window switcher, run dialog and dmenu replacement

License:	MIT/X11
URL:		https://davedavenport.github.io/rofi
Source0:	%{name}-%{version}.tar.gz

BuildRequires: i3 >= 4.5
BuildRequires: pkgconfig(xft) >= 2.0
BuildRequires: pkgconfig(cairo-xlib)
BuildRequires: pkgconfig(glib-2.0)
BuildRequires: pkgconfig(libstartup-notification-1.0)
BuildRequires: pkgconfig(pangocairo)
BuildRequires: pkgconfig(x11)
BuildRequires: pkgconfig(xinerama)


%description
A popup window switcher roughly based on superswitcher, requiring only xlib and pango.


%prep
%autosetup


%build
%configure
%make_build


%install
%make_install


%check
make test


%files
%doc AUTHORS Changelog README.md Examples
%license COPYING
%{_bindir}/rofi
%{_bindir}/rofi-sensible-terminal
%{_mandir}/man1/rofi.1.*
%{_mandir}/man1/rofi-sensible-terminal.1.*


%changelog
