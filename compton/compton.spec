Name:           compton
Version: 0.1.20161012gitb7f43e
Release:        1%{?dist}
Summary:        Compositor for X11
License:        MIT
URL:            https://github.com/chjj/compton

Source0:        %{name}-%{version}.tar.gz

BuildRequires: pkgconfig(x11)
BuildRequires: pkgconfig(xcomposite)
BuildRequires: pkgconfig(xdamage)
BuildRequires: pkgconfig(xfixes)
BuildRequires: pkgconfig(xext)
BuildRequires: pkgconfig(xrender)
BuildRequires: pkgconfig(xrandr)
BuildRequires: pkgconfig(xinerama)
BuildRequires: pkgconfig(xproto)
BuildRequires: pkgconfig(libpcre)
BuildRequires: pkgconfig(libconfig)
BuildRequires: pkgconfig(libdrm)
BuildRequires: pkgconfig(gl)
BuildRequires: pkgconfig(dbus-1)
BuildRequires: asciidoc
BuildRequires:  desktop-file-utils

Requires:       xorg-x11-utils


%description
Compton is a compositor for X, and a fork of xcompmgr-dana.


%prep
%autosetup


%build
%make_build
make docs


%install
%make_install
desktop-file-validate %{buildroot}%{_datadir}/applications/%{name}.desktop


%post
/usr/bin/update-desktop-database -q
xdg-icon-resource forceupdate --theme hicolor &> /dev/null


%postun
/usr/bin/update-desktop-database -q
xdg-icon-resource forceupdate --theme hicolor &> /dev/null


%files
%doc LICENSE README.md
%{_bindir}/%{name}
%{_bindir}/%{name}-trans
%{_mandir}/man1/%{name}.1.*
%{_mandir}/man1/%{name}-trans.1.*
%{_datadir}/icons/*
%{_datadir}/applications/%{name}.desktop


%changelog
