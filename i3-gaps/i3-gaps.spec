Name:           i3-gaps
Version: 4.12
Release:        1%{?dist}
Summary:        i3 with more features
License:        BSD
URL:            https://github.com/Airblader/i3
Source0:        %{name}-%{version}.tar.gz
Source1:        i3-logo.svg

BuildRequires:  asciidoc
BuildRequires:  bison
BuildRequires:  flex
BuildRequires:  libev-devel
BuildRequires:  libX11-devel
BuildRequires:  libxcb-devel
BuildRequires:  libXcursor-devel
BuildRequires:  libxkbcommon-x11-devel
BuildRequires:  libxkbfile-devel
BuildRequires:  pango-devel
BuildRequires:  pcre-devel
BuildRequires:  perl-generators
BuildRequires:  perl(Getopt::Long)
BuildRequires:  perl(Data::Dumper::Names)
BuildRequires:  startup-notification-devel
BuildRequires:  xcb-proto
BuildRequires:  xcb-util-cursor-devel
BuildRequires:  xcb-util-devel
BuildRequires:  xcb-util-keysyms-devel
BuildRequires:  xcb-util-wm-devel
BuildRequires:  xmlto
BuildRequires:  yajl-devel
BuildRequires:  git

Requires:       perl(:MODULE_COMPAT_%(eval "`perl -V:version`"; echo $version))
Requires:       xorg-x11-fonts-misc


Conflicts:      otherproviders(i3)
Provides:       i3 = %{version}


%description
Key features of i3 are correct implementation of XrandR, horizontal and vertical
columns (think of a table) in tiling. Also, special focus is on writing clean,
readable and well documented code. i3 uses xcb for asynchronous communication
with X11, and has several measures to be very fast.

Please be aware that i3 is primarily targeted at advanced users and developers.


%package        doc
Summary:        Documentation for %{name}
BuildRequires:  doxygen
BuildArch:      noarch
Requires:       %{name} = %{version}-%{release}


%description    doc
Asciidoc and doxygen generated documentations for %{name}.


%prep
%autosetup

# Drop /usr/bin/env lines in those which will be installed to %%_bindir.
find . -maxdepth 1 -type f -name "i3*" -exec sed -i -e '1s;^#!/usr/bin/env perl;#!/usr/bin/perl;' {} + -print

# 1. Drop dwarf-2, -g3 in CFLAGS recommended by gcc maintainer. Since upstream
# uses -pipe and -g only, we can safely ignore these, but ldflags needs
# override still.
# 2. Preserve the timestamps.
sed -i -e 's|LDFLAGS ?=|override LDFLAGS +=|g' \
       -e 's|INSTALL=.*|INSTALL=install -p|g' \
       common.mk


%build
%make_build CFLAGS="%{optflags}" LDFLAGS="%{?__global_ldflags}" V=1
%make_build -C man V=1
%make_build -C docs V=1

doxygen pseudo-doc.doxygen
mv pseudo-doc/html pseudo-doc/doxygen


%install
%make_install

mkdir -p %{buildroot}%{_mandir}/man1/
install -Dpm0644 man/*.1 \
        %{buildroot}%{_mandir}/man1/

mkdir -p %{buildroot}%{_datadir}/pixmaps/
install -Dpm0644 %{SOURCE1} \
        %{buildroot}%{_datadir}/pixmaps/


%files
%doc RELEASE-NOTES-*
%license LICENSE
%{_bindir}/i3*
%{_includedir}/i3/
%dir %{_sysconfdir}/i3/
%config(noreplace) %{_sysconfdir}/i3/config
%config(noreplace) %{_sysconfdir}/i3/config.keycodes
%{_datadir}/xsessions/i3.desktop
%{_datadir}/xsessions/i3-with-shmlog.desktop
%{_mandir}/man*/i3*
%{_datadir}/pixmaps/i3-logo.svg
%{_datadir}/applications/i3.desktop


%files doc
%doc docs/*.{html,png} pseudo-doc/doxygen/


%changelog
