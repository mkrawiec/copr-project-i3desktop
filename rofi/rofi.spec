Name:		rofi
Version: 1.2.0
Release:	1rc1%{?dist}
Summary:	A window switcher, run dialog and dmenu replacement

License:	MIT/X11
URL:		https://davedavenport.github.io/rofi
Source0:	%{name}-%{version}.tar.gz

BuildRequires: i3 >= 4.5
BuildRequires: pkgconfig(xft) >= 2.0
BuildRequires: pkgconfig(glib-2.0)
BuildRequires: pkgconfig(libstartup-notification-1.0)
BuildRequires: pkgconfig(xcb-aux)
BuildRequires: pkgconfig(xkbcommon)
BuildRequires: pkgconfig(xkbcommon-x11)
BuildRequires: pkgconfig(xcb-ewmh)
BuildRequires: pkgconfig(xcb-icccm)
BuildRequires: pkgconfig(pango)
BuildRequires: pkgconfig(pangocairo)


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
