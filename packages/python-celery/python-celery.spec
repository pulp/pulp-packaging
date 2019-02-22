%global desc An open source asynchronous task queue/job queue based on\
distributed message passing. It is focused on real-time\
operation, but supports scheduling as well.\
\
The execution units, called tasks, are executed concurrently\
on one or more worker nodes using multiprocessing, Eventlet\
or gevent. Tasks can execute asynchronously (in the background)\
or synchronously (wait until ready).\
\
Celery is used in production systems to process millions of\
tasks a day.\
\
Celery is written in Python, but the protocol can be implemented\
in any language. It can also operate with other languages using\
web hooks.\
\
The recommended message broker is RabbitMQ, but limited support\
for Redis, Beanstalk, MongoDB, CouchDB and databases\
(using SQLAlchemy or the Django ORM) is also available.\


Name:           python-celery
Version:        4.0.2
Release:        7%{?dist}
BuildArch:      noarch
Epoch:          10
License:        BSD
URL:            http://celeryproject.org
Source0:        https://github.com/celery/celery/archive/v%{version}/%{name}-%{version}.tar.gz
Summary:        Distributed Task Queue

# can be removed w/ celery 4.0.3+
Patch0: 3752.patch

%description
%desc


%package doc
Summary: Documentation for python-celery

%description doc
Documentation for python-celery.


%package -n python2-celery
Summary:        Distributed Task Queue

Provides:       python-celery
Obsoletes:      python-celery < %{version}

Requires:       python-amqp
Requires:       python-anyjson
Requires:       python-billiard >= 1:3.3.0.22
Requires:       python-kombu >= 1:3.0.33
Requires:       python2-setuptools
Requires:       pytz

BuildRequires:  python2-devel
BuildRequires:  python2-rpm-macros
BuildRequires:  python-setuptools



%description -n python2-celery
%{desc}


%prep
%autosetup -n celery-%{version} -p1


%build
%{__python} setup.py build


%install
%{__python} setup.py install -O1 --skip-build --root %{buildroot}


%files doc
%license LICENSE


%files -n python2-celery
%license LICENSE
%doc README.rst TODO CONTRIBUTORS.txt examples
%{_bindir}/celery
#%{_bindir}/celerybeat
#%{_bindir}/celerybeat-2*
#%{_bindir}/celeryd
#%{_bindir}/celeryd-2*
#%{_bindir}/celeryd-multi
#%{_bindir}/celeryd-multi-2*
%{python2_sitelib}/celery-*.egg-info
%{python2_sitelib}/celery


%changelog
* Fri Feb 22 2019 Patrick Creech <pcreech@redhat.com> - 10:4.0.2-7
- Setting Epoch

* Mon Feb 18 2019 Patrick Creech <pcreech@redhat.com> - 4.0.2-6
- rebuilt

* Wed Jul 25 2018 Daniel Alley <dalley@redhat.com> - 4.0.2-5
- Added a patch to fix Celery issue https://github.com/celery/celery/issues/3620

* Mon Mar 26 2018 Patrick Creech <pcreech@redhat.com> - 4.0.2-4
- Adding obsoletes

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Jan 10 2017 Matthias Runge <mrunge@redhat.com> - 4.0.2-1
- upgrade to 4.0.x (rhbz#1400270, rhbz#1410864)

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 3.1.20-5
- Rebuild for Python 3.6

* Mon Nov 28 2016 Charalampos Stratakis <cstratak@redhat.com> - 3.1.20-4
- Remove obsolete Requires for python-uuid

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.1.20-3
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.20-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sun Jan 24 2016 Randy Barlow <rbarlow@redhat.com> - 3.1.20-1
- update to 3.1.20 (#1080882).

* Sat Jan 23 2016 Randy Barlow <rbarlow@redhat.com> - 3.1.19-1
- update to 3.1.19 (#1080882).
- Remove conditionals on Python 3 - always build for Python 3.
- Remove tests as they were disabled and don't pass anyway.
- Update to use the python2/3 naming conventions.
- Use the fancy new Python macros (#1300083).
- Add a -doc subpackage (#1223099).
- Use the license macro (#1223099).
- Remove dependency on importlib, since it is present in 2.7 and 3.5.

* Tue Dec 01 2015 Brian Bouterse <bbouters@redhat.com> - 3.1.11-1
- update to 3.1.11

* Tue Nov 10 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.1.9-5
- Rebuilt for https://fedoraproject.org/wiki/Changes/python3.5

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.1.9-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.1.9-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue May 27 2014 Kalev Lember <kalevlember@gmail.com> - 3.1.9-2
- Rebuilt for https://fedoraproject.org/wiki/Changes/Python_3.4

* Wed Feb 26 2014 Matthias Runge <mrunge@redhat.com> - 3.1.9-1
- update to 3.1.9 (rhbz#1055304)

* Wed Feb 26 2014 Matthias Runge <mrunge@redhat.com> - 3.1.7-4
- add runtime requirement pyzu (rhbz#1069774)
- remove runtime req. python-dateutil

* Fri Jan 10 2014 Matthias Runge <mrunge@redhat.com> - 3.1.7-3
- add runtime requirement python-setuptools (rhbz#1051176)

* Wed Jan 08 2014 Matthias Runge <mrunge@redhat.com> - 3.1.7-2
- require correct python-kombu-version

* Wed Jan 08 2014 Matthias Runge <mrunge@redhat.com> - 3.1.7-1
- update to 3.1.7 (rhbz#1034115)
- add more explicit requirement to python-billiard (rhbz#1028626)

* Mon Oct 14 2013 Matthias Runge <mrunge@redhat.com> - 3.0.24-1
- update to 3.0.24 (rhbz#1018596)

* Fri Sep 27 2013 Matthias Runge <mrunge@redhat.com> - 3.0.23-1
- update to 3.0.23 (rhbz#979595)

* Fri Sep 27 2013 Matthias Runge <mrunge@redhat.com> - 3.0.19-4
- add python-amqp to deps
- add requirement python-amqp
- fix requirements: python3-kombu, python3-pytz, python3-dateutil and billiard
- separate binaries for py3 and py (fixes rhbz#1000750)

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.0.19-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Tue Apr 23 2013 Matthias Runge <mrunge@redhat.com> - 3.0.19-1
- update to celery-3.0.19 (rhbz#919560)

* Fri Feb 15 2013 Matthias Runge <mrunge@redhat.com> - 3.0.15-1
- update to celery-3.0.15 (rhbz#909919)

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.0.13-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jan 17 2013 Matthias Runge <mrunge@redhat.com> - 3.0.13-1
- update to upstream version 3.0.13 (rhbz#892923)

* Wed Nov 14 2012 Matthias Runge <mrunge@redhat.com> - 3.0.12-1
- update to upstream version 3.0.12

* Tue Oct 16 2012 Matthias Runge <mrunge@redhat.com> - 3.0.11-1
- update to upstream version 3.0.11

* Sun Aug 26 2012 Matthias Runge <mrunge@matthias-runge.de> - 3.0.7-1
- update to upstream version 3.0.7

* Thu Aug 23 2012 Matthias Runge <mrunge@matthias-runge.de> - 3.0.6-1
- update to upstream version 3.0.6

* Fri Aug 03 2012 Matthias Runge <mrunge@matthias-runge.de> - 3.0.5-1
- update to version 3.0.5
- enable python3 support

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.8-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Nov 28 2011 Andrew Colin Kissa <andrew@topdog.za.net> - 2.2.8-1
- Security FIX CELERYSA-0001

* Fri Jul 15 2011 Andrew Colin Kissa <andrew@topdog.za.net> - 2.2.7-3
- Fix rpmlint errors
- Fix dependencies

* Sat Jun 25 2011 Andrew Colin Kissa <andrew@topdog.za.net> 2.2.7-2
- Update for RHEL6

* Tue Jun 21 2011 Andrew Colin Kissa <andrew@topdog.za.net> 2.2.7-1
- Initial package
