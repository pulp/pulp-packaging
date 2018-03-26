%global pypi_name vine

Name:           python-%{pypi_name}
Version:        1.1.3
Release:        4%{?dist}
Summary:        Promises, promises, promises

License:        BSD
URL:            http://github.com/celery/vine
Source0:        https://files.pythonhosted.org/packages/source/v/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python2-devel
BuildRequires:  python-setuptools
BuildRequires:  python-sphinx

%description
%{summary}


%package -n     python2-%{pypi_name}
Summary:        Promises, promises, promises
Provides:       python-%{pypi_name}
Obsoletes:      python-%{pypi_name} < %{version}

%description -n python2-%{pypi_name}
%{summary}

%prep
%autosetup -n %{pypi_name}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%build
%{__python} setup.py build

%install
%{__python} setup.py install --skip-build --root %{buildroot}

%files -n python2-%{pypi_name}
%license LICENSE
%doc docs/templates/readme.txt README.rst
%{python2_sitelib}/%{pypi_name}
%{python2_sitelib}/%{pypi_name}-%{version}-py?.?.egg-info

%changelog
* Mon Mar 26 2018 Patrick Creech <pcreech@redhat.com> - 1.1.3-4
- Adding in obsoletes

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Dec 27 2016 Matthias Runge <mrunge@redhat.com> - 1.1.3-1
- Initial package. (rhbz#1408869)
