%global srcname amqp

Name:           python-%{srcname}
Version:        2.2.2
Release:        5%{?dist}
Summary:        Low-level AMQP client for Python (fork of amqplib)
Epoch:          10
Group:          Development/Languages
License:        LGPLv2+
URL:            http://pypi.python.org/pypi/amqp
Source0:        https://files.pythonhosted.org/packages/source/a/%{srcname}/%{srcname}-%{version}.tar.gz
BuildArch:      noarch

%description
Low-level AMQP client for Python

This is a fork of amqplib, maintained by the Celery project.

This library should be API compatible with librabbitmq.


%package -n python2-%{srcname}
Summary:     Client library for AMQP
Requires:    python2-vine >= 1.1.3
BuildRequires:  python2-devel
BuildRequires:  python-setuptools
BuildRequires:  python-nose
Provides:       python-%{srcname} 
Obsoletes:      python-%{srcname} < %{version}-%{release}

%description -n python2-%{srcname}
Low-level AMQP client for Python

This is a fork of amqplib, maintained by the Celery project.

This library should be API compatible with librabbitmq.


%package doc
Summary:        Documentation for python-amqp
Group:          Documentation

Requires:       %{name} = %{version}-%{release}

%description doc
Documentation for python-amqp


%prep
%autosetup -n %{srcname}-%{version}


%build
%{__python} setup.py build


%install
%{__python} setup.py install --skip-build --root %{buildroot}


%files -n python2-%{srcname}
%doc Changelog README.rst
%license LICENSE
%{python2_sitelib}/%{srcname}
%{python2_sitelib}/%{srcname}-%{version}-py%{python2_version}.egg-info


%files doc
%license LICENSE

%changelog
* Fri Feb 22 2019 Patrick Creech <pcreech@redhat.com> - 10:2.2.2-5
- Setting Epoch

* Tue Feb 19 2019 Patrick Creech <pcreech@redhat.com> - 2.2.2-4
- rebuilt

* Tue Jan 16 2018 Patrick Creech <pcreech@redhat.com> - 2.2.2-3
- Fix obsoletes for 2.2.2

* Tue Jan 16 2018 Eric Harney <eharney@redhat.com> - 2.2.2-2
- Enable py3 build for el8

* Tue Oct 24 2017 Eric Harney <eharney@redhat.com> - 2.2.2-1
- Update to 2.2.2

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Jul 14 2017 Eric Harney <eharney@redhat.com> - 2.2.1-2
- Enable unit tests

* Fri Jul 14 2017 Eric Harney <eharney@redhat.com> - 2.2.1-1
- Update to 2.2.1

* Thu Jul 13 2017 Eric Harney <eharney@redhat.com> - 2.2.0-1
- Update to 2.2.0

* Wed Feb 08 2017 Matthias Runge <mrunge@redhat.com> - 2.1.4-1
- upgrade to 2.1.4 (rhbz#1340298)
- modernize spec, add provides (rhbz#1399248)

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 1.4.9-4
- Rebuild for Python 3.6

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.9-3
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jan 15 2016 Eric Harney <eharney@redhat.com> - 1.4.9-1
- Update to 1.4.9

* Thu Jan 07 2016 Eric Harney <eharney@redhat.com> - 1.4.8-1
- Update to 1.4.8

* Thu Nov 12 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.7-2
- Rebuilt for https://fedoraproject.org/wiki/Changes/python3.5

* Wed Nov 11 2015 Eric Harney <eharney@redhat.com> - 1.4.7-1
- Update to 1.4.7

* Wed Nov 04 2015 Matej Stuchlik <mstuchli@redhat.com> - 1.4.6-3
- Rebuilt for Python 3.5

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Oct 06 2014 Eric Harney <eharney@redhat.com> - 1.4.6-1
- Update to 1.4.6

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed May 14 2014 Bohuslav Kabrda <bkabrda@redhat.com> - 1.4.5-2
- Rebuilt for https://fedoraproject.org/wiki/Changes/Python_3.4

* Wed Apr 16 2014 Eric Harney <eharney@redhat.com> - 1.4.5-1
- Update to 1.4.5

* Fri Feb 07 2014 Eric Harney <eharney@redhat.com> - 1.4.2-1
- Update to 1.4.2

* Fri Jan 17 2014 Eric Harney <eharney@redhat.com> - 1.4.1-1
- Update to 1.4.1

* Fri Nov 15 2013 Eric Harney <eharney@redhat.com> - 1.3.3-1
- Update to 1.3.3

* Fri Oct 25 2013 Eric Harney <eharney@redhat.com> - 1.3.1-1
- Update to 1.3.1

* Tue Oct 08 2013 Eric Harney <eharney@redhat.com> - 1.3.0-1
- Update to 1.3.0

* Fri Sep 20 2013 Eric Harney <eharney@redhat.com> - 1.2.1-1
- Update to 1.2.1

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.11-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Jun 21 2013 Eric Harney <eharney@redhat.com> - 1.0.11-1
- Initial package
