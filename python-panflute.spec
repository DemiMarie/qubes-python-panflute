# Created by pyp2rpm-3.3.4
%global pypi_name panflute

Name:           python-%{pypi_name}
Version:        1.12.5
Release:        2%{?dist}
Summary:        Pythonic Pandoc filters

License:        BSD3
URL:            https://github.com/sergiocorreia/panflute
Source0:        %{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-setuptools

%description
Panflute: Pythonic Pandoc Filters is a Python package that makes
creating Pandoc filters fun.

%package -n     python%{python3_pkgversion}-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python%{python3_pkgversion}-%{pypi_name}}

Requires:       python%{python3_pkgversion}-click
Requires:       python%{python3_pkgversion}-docutils
Requires:       python%{python3_pkgversion}-pygments
%if 0%{?fedora} < 26
Requires:       python%{python3_pkgversion}-PyYAML
%else
Requires:       python%{python3_pkgversion}-pyyaml
%endif
Requires:       python%{python3_pkgversion}-setuptools

# only needed for tests
#Requires:       python%{python3_pkgversion}-pytest-cov
#Requires:       python%{python3_pkgversion}-pandocfilters
#Requires:       python%{python3_pkgversion}-configparser

%description -n python%{python3_pkgversion}-%{pypi_name}
Panflute: Pythonic Pandoc Filters is a Python package that makes
creating Pandoc filters fun.


%prep
%autosetup -n %{pypi_name}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%build
%py3_build

%install
%py3_install

%files -n python%{python3_pkgversion}-%{pypi_name}
%license LICENSE
%doc README.md
%{_bindir}/panfl
%{_bindir}/panflute
%{python3_sitelib}/%{pypi_name}
%{python3_sitelib}/%{pypi_name}-%{version}-py%{python3_version}.egg-info

%changelog
* Sun Oct 04 2020 Marek Marczykowski-Górecki <marmarek@invisiblethingslab.com> - 1.12.5-1
- Initial package.
