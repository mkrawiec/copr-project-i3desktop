Name:           dex-xdg
Version: 0.8.20160310gitfdbe3c
Release:        1%{?dist}
Summary:        DesktopEntry Execution

License:        GPLv3
URL:            https://github.com/jceb/dex
Source0:        %{name}-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  python-sphinx
Requires:       python3

%description
DesktopEntry Execution, is a program to generate and execute DesktopEntry
files of the Application type.


%prep
%autosetup


%build
make


%install
%make_install \
    PREFIX=%{_prefix} \
    MANPREFIX=%{_mandir} \
    NAME=dex-xdg \
    VERSION=%{version}

rm -fr %{buildroot}/%{_docdir}


%files
%defattr(-,root,root,-)
%doc README.rst CHANGELOG.md
%license LICENSE
%{_bindir}/dex-xdg
%{_datadir}/man/*/*

%changelog
