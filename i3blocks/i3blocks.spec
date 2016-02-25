Name:       i3blocks
Summary:    A flexible scheduler for your i3bar blocks
License:    GPLv3
Version: 1.4
Release:    1%{?dist}
Url:        https://github.com/vivien/i3blocks
Source0:    %{name}-%{version}.tar.gz

BuildRequires:  gcc-c++
BuildRequires:  rubygem-ronn


%description
i3blocks is a highly flexible status line for the i3 window manager.
It handles clicks, signals and language-agnostic user scripts.


%prep
%autosetup


%build
make %{?_smp_mflags}


%install
make \
    PREFIX="%{_prefix}" \
    MANDIR="%{_mandir}" \
    DESTDIR="%{buildroot}" \
    install


%files
%defattr(-,root,root)
%doc CHANGELOG.md README.md
%license COPYING
%{_bindir}/%{name}
%{_sysconfdir}/%{name}.conf
%{_libexecdir}/%{name}
%{_mandir}/man1/%{name}*


%changelog
