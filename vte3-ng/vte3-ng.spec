%global apiver 2.91

Name:           vte3-ng
Version: 0.44.1
Release:        1%{?dist}
Summary:        Terminal emulator library

License:        LGPLv2+
URL:            http://www.gnome.org/
Source0:        %{name}-%{version}.tar.gz

BuildRequires:  gettext
BuildRequires:  pkgconfig(gnutls)
BuildRequires:  pkgconfig(libpcre2-8) >= 10.00
BuildRequires:  gobject-introspection-devel
BuildRequires:  gtk-doc
BuildRequires:  gperf
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  intltool
BuildRequires:  vala-tools

# initscripts creates the utmp group
Requires:       initscripts
Requires:       vte-profile

Provides: vte291 = %{version}-%{release}
Provides: vte291%{?_isa} = %{version}-%{release}

Conflicts: vte291%{?_isa}

%description
VTE is a library implementing a terminal emulator widget for GTK+. VTE
is mainly used in gnome-terminal, but can also be used to embed a
console/terminal in games, editors, IDEs, etc.


%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}


%description devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

# vte-profile is deliberately not noarch to avoid having to obsolete a noarch
# subpackage in the future when we get rid of the vte3 / vte291 split. Yum is
# notoriously bad when handling noarch obsoletes and insists on installing both
# of the multilib packages (i686 + x86_64) as the replacement.
%package -n     vte-profile
Summary:        Profile script for VTE terminal emulator library
License:        GPLv3+
# vte.sh was previously part of the vte3 package
Conflicts:      vte3 < 0.36.1-3


%description -n vte-profile
The vte-profile package contains a profile.d script for the VTE terminal
emulator library.


%prep
%autosetup


%build
CFLAGS="%optflags -fPIE -DPIE -Wno-nonnull" \
CXXFLAGS="$CFLAGS" \
LDFLAGS="$LDFLAGS -Wl,-z,relro -Wl,-z,now -pie" \
NOCONFIGURE=1 ./autogen.sh
%configure \
        --disable-static \
        --libexecdir=%{_libdir}/vte-%{apiver} \
        --disable-gtk-doc \
        --enable-introspection
make %{?_smp_mflags} V=1


%install
%make_install

rm -f $RPM_BUILD_ROOT%{_libdir}/*.la

%find_lang vte-%{apiver}

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig


%files -f vte-%{apiver}.lang
%license COPYING
%doc NEWS README
%{_libdir}/libvte-%{apiver}.so.0*
%{_libdir}/girepository-1.0/


%files devel
%{_bindir}/vte-%{apiver}
%{_includedir}/vte-%{apiver}/
%{_libdir}/libvte-%{apiver}.so
%{_libdir}/pkgconfig/vte-%{apiver}.pc
%{_datadir}/gir-1.0/
%{_datadir}/vala/


%files -n vte-profile
%{_sysconfdir}/profile.d/vte.sh


%changelog
