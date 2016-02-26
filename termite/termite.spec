Name:           termite
Version: 11
Release:        1%{?dist}
Summary:        Terminal emulator based on GTK and VTE

Group:          User Interface/X
License:        GPLv2
URL:            https://github.com/thestinger/termite
Source0:        %{name}-%{version}.tar.gz

BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  vte3-ng-devel >= 0.42
BuildRequires:  desktop-file-utils


%description
Termite is a terminal emulator based on GTK and VTE. It's a terminal emulator
with few dependencies, so you don't need a full GNOME desktop installed to
have a decent terminal emulator.  This package requires a patched vte, for
the "select text" features utilized by termite.


%prep
%autosetup

# Generate debug symbols
sed -i -e 's/-O3/-O3 -g/g' Makefile

# Do not strip output file
sed -i -e 's/LDFLAGS := -s/LDFLAGS :=/g' Makefile

%build
make VERBOSE=1 %{?_smp_mflags}


%install
make PREFIX=/usr DESTDIR=%{buildroot} install
install -Dm644 config %{buildroot}/etc/xdg/termite/config


%post
/usr/bin/update-desktop-database -q
xdg-icon-resource forceupdate --theme hicolor &> /dev/null


%postun
/usr/bin/update-desktop-database -q
xdg-icon-resource forceupdate --theme hicolor &> /dev/null


%files
%doc README.rst TODO.rst
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/terminfo/x/xterm-termite
%{_mandir}/man1/%{name}.1.*
%{_mandir}/man5/%{name}.config.5.*
%{_sysconfdir}/xdg/termite/config


%changelog
