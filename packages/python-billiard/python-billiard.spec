%global srcname billiard

Name:           python-%{srcname}
Version:        3.5.0.3
Release:        2%{?dist}
Epoch:          1
Summary:        Multiprocessing Pool Extensions

License:        BSD
URL:            https://github.com/celery/billiard
Source0:        https://files.pythonhosted.org/packages/source/b/%{srcname}/%{srcname}-%{version}.tar.gz
#Source0:        https://github.com/celery/billiard/archive/v%{version}.tar.gz#/%{srcname}-%{version}.tar.gz

BuildRequires:  python2-devel
BuildRequires:  python-setuptools
BuildRequires:  python-mock


%description
This package contains extensions to the multiprocessing Pool.

%package -n python2-%{srcname}
Summary:        %{summary}
Provides:       python-%{srcname}
Obsoletes:      python-%{srcname} < %{version}

%description -n python2-%{srcname}
This package contains extensions to the multiprocessing Pool.

%prep
%autosetup -n %{srcname}-%{version}

%build
%{__python} setup.py build

%install
%{__python} setup.py install --skip-build --root %{buildroot}

%files -n python2-%{srcname}
%doc CHANGES.txt README.rst
%license LICENSE.txt
%{python2_sitearch}/_billiard*
%{python2_sitearch}/%{srcname}/
%{python2_sitearch}/%{srcname}*.egg-info
%exclude %{python2_sitearch}/funtests/

%changelog
* Mon Mar 26 2018 Patrick Creech <pcreech@redhat.com> - 1:3.5.0.3-2
- Adding in obsoletes

* Sun Aug 27 2017 Fabian Affolter <mail@fabian-affolter.ch> - 1:3.5.0.3-1
- Update to latest upstream version 3.5.0.3 (rhbz#1471568)

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1:3.5.0.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1:3.5.0.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Feb 07 2017 Matthias Runge <mrunge@redhat.com> - 1:3.5.0.2-1
- update to 3.5.0.2
- enable tests again

* Thu Dec 22 2016 Adam Williamson <awilliam@redhat.com> -  - 1:3.5.0.1-2
- Disable tests for now, they cannot work till python-case is packaged

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com>
- Rebuild for Python 3.6

* Wed Nov 16 2016 Fabian Affolter <mail@fabian-affolter.ch> - 1:3.5.0.1-1
- Update to latest upstream version 3.5.0.1 (rhbz#1354091)

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:3.3.0.23-2
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Wed Mar 09 2016 Fabian Affolter <mail@fabian-affolter.ch> - 1:3.3.0.23-1
- Update to latest upstream version 3.3.0.23 (rhbz#1314751)

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1:3.3.0.22-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sun Nov 15 2015 Fabian Affolter <mail@fabian-affolter.ch> - 1:3.3.0.22-1
- Update to latest upstream version 3.3.0.22 (rhbz#1275443)

* Thu Nov 12 2015 Kalev Lember <klember@redhat.com> - 1:3.3.0.21-2
- Rebuilt for https://fedoraproject.org/wiki/Changes/python3.5

* Wed Oct 28 2015 Fabian Affolter <mail@fabian-affolter.ch> - 1:3.3.0.21-1
- Update to latest upstream version 3.3.0.21 (rhbz#1086634)

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:3.3.0.20-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Apr 18 2015 Fabian Affolter <mail@fabian-affolter.ch> - 1:3.3.0.20-1
- Update to latest upstream version 3.3.0.20 (rhbz#1213018)

* Fri Nov 21 2014 Fabian Affolter <mail@fabian-affolter.ch> - 1:3.3.0.19-1
- Update to latest upstream version 3.3.0.19 (rhbz#1166400)

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:3.3.0.18-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Mon Jun 23 2014 Fabian Affolter <mail@fabian-affolter.ch> - 3.3.0.18-1
- Update to latest upstream version 3.3.0.18 (rhbz#1111875)

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:3.3.0.17-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Mon May 19 2014 Bohuslav Kabrda <bkabrda@redhat.com> - 1:3.3.0.17-2
- Rebuilt for https://fedoraproject.org/wiki/Changes/Python_3.4

* Thu Apr 17 2014 Fabian Affolter <mail@fabian-affolter.ch> - 3.3.0.17-1
- Update to latest upstream version 3.3.0.17 (rhbz#1088894)

* Wed Mar 05 2014 Fabian Affolter <mail@fabian-affolter.ch> - 3.3.0.16-1
- Update to latest upstream version 3.3.0.16 (rhbz#1063785)

* Thu Jan 23 2014 Fabian Affolter <mail@fabian-affolter.ch> - 3.3.0.14-1
- Update to latest upstream version 3.3.0.14 (rhbz#1055303)

* Wed Jan 08 2014 Matthias Runge <mrunge@redhat.com> - 3.3.0.13-1
- update to 3.3.013 (rhbz#1034114)
- use epoch:1 (rhbz#1028626)

* Thu Nov 21 2013 Matthias Runge <mrunge@redhat.com> - 3.3.0.7-1
- update to 3.3.0.7 (rhbz#1026722)

* Sat Nov 09 2013 Fabian Affolter <mail@fabian-affolter.ch> - 3.3.0.1-1
- Update to latest upstream version 3.3.0.1 (rhbz#1026722)

* Mon Oct 28 2013 Fabian Affolter <mail@fabian-affolter.ch> - 3.3.0.0-1
- Update to latest upstream version 3.3.0.0 (rhbz#1019144)

* Mon Oct 14 2013 Matthias Runge <mrunge@redhat.com> - 2.7.34-1
- update to 2.7.34 (rhbz#1018595)
- enable tests

* Tue Oct 08 2013 Fabian Affolter <mail@fabian-affolter.ch> - 2.7.3.33-1
- Update to latest upstream version 2.7.3.33

* Sat Aug 17 2013 Fabian Affolter <mail@fabian-affolter.ch> - 2.7.3.32-1
- Update to latest upstream version 2.7.3.32

* Wed Jul 31 2013 Fabian Affolter <mail@fabian-affolter.ch> - 2.7.3.31-1
- Update to latest upstream version 2.7.3.31

* Sat Jun 29 2013 Fabian Affolter <mail@fabian-affolter.ch> - 2.7.3.30-1
- Update to latest upstream version 2.7.3.30

* Wed Apr 17 2013 Fabian Affolter <mail@fabian-affolter.ch> - 2.7.3.28-1
- Update to latest upstream version 2.7.3.28

* Tue Mar 26 2013 Fabian Affolter <mail@fabian-affolter.ch> - 2.7.3.23-1
- Update to latest upstream version 2.7.3.23

* Sat Mar 09 2013 Fabian Affolter <mail@fabian-affolter.ch> - 2.7.3.22-1
- Update to latest upstream version 2.7.3.22

* Wed Feb 13 2013 Fabian Affolter <mail@fabian-affolter.ch> - 2.7.3.21-1
- Update to latest upstream version 2.7.3.21

* Mon Feb 11 2013 Fabian Affolter <mail@fabian-affolter.ch> - 2.7.3.20-1
- Update to latest upstream version 2.7.3.20

* Sun Dec 02 2012 Matthias Runge <mrunge@redhat.com> - 2.7.3.19-1
- Update to upstream version 2.7.3.19

* Tue Nov 06 2012 Matthias Runge <mrunge@redhat.com> - 2.7.3.18-1
- Update to upstream version 2.7.3.18

* Fri Sep 28 2012 Matthias Runge <mrunge@redhat.com> - 2.7.3.17-1
- Update to upstream version 2.7.3.17

* Thu Sep 20 2012 Matthias Runge <mrunge@redhat.com> - 2.7.3.14-1
- Update to upstream version 2.7.3.14

* Sun Aug 26 2012 Matthias Runge <mrunge@matthias-runge.de> - 2.7.3.12-1
- Update to new upstream version 2.7.3.12
- Provide python3 packages
- Enable checks

* Fri Aug 03 2012 Matthias Runge <mrunge@matthias-runge.de> 2.7.3.11-1
- Update to new upstream version 2.7.3.11

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.7.3.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Jun 19 2012 Fabian Affolter <mail@fabian-affolter.ch> - 2.7.3.9-1
- Update to new upstream version 2.7.3.9

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sat Aug 14 2010 Fabian Affolter <mail@fabian-affolter.ch> - 0.3.1-2
- TODO removed

* Sat Jul 03 2010 Fabian Affolter <mail@fabian-affolter.ch> - 0.3.1-1
- Initial package
