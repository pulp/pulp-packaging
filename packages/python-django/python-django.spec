%global         pkgname Django


# Tests requiring Internet connections are disabled by default
# pass --with internet to run them (e.g. when doing a local rebuild
# for sanity checks before committing)
%bcond_with internet

# one higher than the last Django release, to account for
# dist tags
%global         obs_ver 1.11.11-1

Name:           python-django

Version:        1.11.11
Release:        1%{?dist}
Summary:        A high-level Python Web framework

Group:          Development/Languages
License:        BSD
URL:            http://www.djangoproject.com/
Source0:        https://files.pythonhosted.org/packages/source/D/Django/Django-%{version}.tar.gz


BuildArch:      noarch


%description
Django is a high-level Python Web framework that encourages rapid
development and a clean, pragmatic design. It focuses on automating as
much as possible and adhering to the DRY (Don't Repeat Yourself)
principle.

%package -n     python2-django
Summary:        A high-level Python Web framework
Provides:       python-django
BuildRequires:  python2-devel
BuildRequires:  python-setuptools

# allow users to use django with lowercase d
Provides:       django = %{version}-%{release}
Provides:       %{pkgname} = %{version}-%{release}
Obsoletes:      %{pkgname} < %{obs_ver}
Obsoletes:      python-django < %{obs_ver}

Provides: bundled(jquery) = 2.2.3
Provides: bundled(xregexp) = 2.0.0

%description -n python2-django
Django is a high-level Python Web framework that encourages rapid
development and a clean, pragmatic design. It focuses on automating as
much as possible and adhering to the DRY (Don't Repeat Yourself)
principle.


%prep
%autosetup -n %{pkgname}-%{version}

%build
%{__python} setup.py build

%install
%{__python} setup.py install --skip-build --root %{buildroot}


%find_lang django
%find_lang djangojs
# append djangojs.lang to django.lang
cat djangojs.lang >> django.lang

# install man pages
mkdir -p %{buildroot}%{_mandir}/man1/
cp -p docs/man/* %{buildroot}%{_mandir}/man1/

# Fix items in %%{_bindir}
mv %{buildroot}%{_bindir}/django-admin.py %{buildroot}%{_bindir}/django-admin

# remove .po files
find $RPM_BUILD_ROOT -name "*.po" | xargs rm -f


%files -n python2-django -f django.lang
%doc AUTHORS README.rst
%license LICENSE
# manual pages are owned by both python2 and python3 packages
%{_mandir}/man1/*
# except the symlink with python3 prefix
%{_bindir}/django-admin
%attr(0755,root,root) %{python2_sitelib}/django/bin/django-admin.py*
# Include everything but the locale data ...
%dir %{python2_sitelib}/django
%dir %{python2_sitelib}/django/bin
%{python2_sitelib}/django/apps
%{python2_sitelib}/django/db/
%{python2_sitelib}/django/*.py*
%{python2_sitelib}/django/utils/
%{python2_sitelib}/django/dispatch/
%{python2_sitelib}/django/template/
%{python2_sitelib}/django/views/
%{python2_sitelib}/django/urls/
%dir %{python2_sitelib}/django/conf/
%dir %{python2_sitelib}/django/conf/locale/
%dir %{python2_sitelib}/django/conf/locale/??/
%dir %{python2_sitelib}/django/conf/locale/??_*/
%dir %{python2_sitelib}/django/conf/locale/*/LC_MESSAGES
%dir %{python2_sitelib}/django/contrib/
%{python2_sitelib}/django/contrib/*.py*
%dir %{python2_sitelib}/django/contrib/admin/
%dir %{python2_sitelib}/django/contrib/admin/locale
%dir %{python2_sitelib}/django/contrib/admin/locale/??/
%dir %{python2_sitelib}/django/contrib/admin/locale/??_*/
%dir %{python2_sitelib}/django/contrib/admin/locale/*/LC_MESSAGES
%{python2_sitelib}/django/contrib/admin/*.py*
%{python2_sitelib}/django/contrib/admin/migrations
%{python2_sitelib}/django/contrib/admin/views/
%{python2_sitelib}/django/contrib/admin/static/
%{python2_sitelib}/django/contrib/admin/templatetags/
%{python2_sitelib}/django/contrib/admin/templates/
%dir %{python2_sitelib}/django/contrib/admindocs/
%dir %{python2_sitelib}/django/contrib/admindocs/locale/
%dir %{python2_sitelib}/django/contrib/admindocs/locale/??/
%dir %{python2_sitelib}/django/contrib/admindocs/locale/??_*/
%dir %{python2_sitelib}/django/contrib/admindocs/locale/*/LC_MESSAGES
%{python2_sitelib}/django/contrib/admindocs/*.py*
%{python2_sitelib}/django/contrib/admindocs/templates/
%dir %{python2_sitelib}/django/contrib/auth/
%dir %{python2_sitelib}/django/contrib/auth/locale/
%dir %{python2_sitelib}/django/contrib/auth/locale/??/
%dir %{python2_sitelib}/django/contrib/auth/locale/??_*/
%dir %{python2_sitelib}/django/contrib/auth/locale/*/LC_MESSAGES
%{python2_sitelib}/django/contrib/auth/*.py*
%{python2_sitelib}/django/contrib/auth/common-passwords.txt.gz
%{python2_sitelib}/django/contrib/auth/handlers/
%{python2_sitelib}/django/contrib/auth/management/
%{python2_sitelib}/django/contrib/auth/migrations/
%{python2_sitelib}/django/contrib/auth/templates/
%{python2_sitelib}/django/contrib/auth/tests/
%dir %{python2_sitelib}/django/contrib/contenttypes/
%dir %{python2_sitelib}/django/contrib/contenttypes/locale
%dir %{python2_sitelib}/django/contrib/contenttypes/locale/??/
%dir %{python2_sitelib}/django/contrib/contenttypes/locale/??_*/
%dir %{python2_sitelib}/django/contrib/contenttypes/locale/*/LC_MESSAGES
%{python2_sitelib}/django/contrib/contenttypes/management
%{python2_sitelib}/django/contrib/contenttypes/migrations
%{python2_sitelib}/django/contrib/contenttypes/*.py*
%dir %{python2_sitelib}/django/contrib/flatpages/
%dir %{python2_sitelib}/django/contrib/flatpages/locale/
%dir %{python2_sitelib}/django/contrib/flatpages/locale/??/
%dir %{python2_sitelib}/django/contrib/flatpages/locale/??_*/
%dir %{python2_sitelib}/django/contrib/flatpages/locale/*/LC_MESSAGES
%{python2_sitelib}/django/contrib/flatpages/*.py*
%{python2_sitelib}/django/contrib/flatpages/migrations/
%{python2_sitelib}/django/contrib/flatpages/templatetags
%dir %{python2_sitelib}/django/contrib/gis/
%dir %{python2_sitelib}/django/contrib/gis/locale/
%dir %{python2_sitelib}/django/contrib/gis/locale/??/
%dir %{python2_sitelib}/django/contrib/gis/locale/??_*/
%dir %{python2_sitelib}/django/contrib/gis/locale/*/LC_MESSAGES
%{python2_sitelib}/django/contrib/gis/*.py*
%{python2_sitelib}/django/contrib/gis/geoip/
%{python2_sitelib}/django/contrib/gis/geoip2/
%{python2_sitelib}/django/contrib/gis/serializers/
%{python2_sitelib}/django/contrib/gis/static
%dir %{python2_sitelib}/django/contrib/humanize/
%dir %{python2_sitelib}/django/contrib/humanize/locale/
%dir %{python2_sitelib}/django/contrib/humanize/locale/??/
%dir %{python2_sitelib}/django/contrib/humanize/locale/??_*/
%dir %{python2_sitelib}/django/contrib/humanize/locale/*/LC_MESSAGES
%{python2_sitelib}/django/contrib/humanize/templatetags/
%{python2_sitelib}/django/contrib/humanize/*.py*
%{python2_sitelib}/django/contrib/messages/*.py*
%dir %{python2_sitelib}/django/contrib/postgres/
%{python2_sitelib}/django/contrib/postgres/*.py*
%{python2_sitelib}/django/contrib/postgres/aggregates
%{python2_sitelib}/django/contrib/postgres/jinja2
%{python2_sitelib}/django/contrib/postgres/fields
%{python2_sitelib}/django/contrib/postgres/forms
%{python2_sitelib}/django/contrib/postgres/templates
%dir %{python2_sitelib}/django/contrib/redirects
%dir %{python2_sitelib}/django/contrib/redirects/locale
%dir %{python2_sitelib}/django/contrib/redirects/locale/??/
%dir %{python2_sitelib}/django/contrib/redirects/locale/??_*/
%dir %{python2_sitelib}/django/contrib/redirects/locale/*/LC_MESSAGES
%{python2_sitelib}/django/contrib/redirects/*.py*
%{python2_sitelib}/django/contrib/redirects/migrations
%dir %{python2_sitelib}/django/contrib/sessions/
%dir %{python2_sitelib}/django/contrib/sessions/locale/
%dir %{python2_sitelib}/django/contrib/sessions/locale/??/
%dir %{python2_sitelib}/django/contrib/sessions/locale/??_*/
%dir %{python2_sitelib}/django/contrib/sessions/locale/*/LC_MESSAGES
%{python2_sitelib}/django/contrib/sessions/management/
%{python2_sitelib}/django/contrib/sessions/migrations/
%{python2_sitelib}/django/contrib/sessions/*.py*
%{python2_sitelib}/django/contrib/sitemaps/
%dir %{python2_sitelib}/django/contrib/sites/
%dir %{python2_sitelib}/django/contrib/sites/locale/
%dir %{python2_sitelib}/django/contrib/sites/locale/??/
%dir %{python2_sitelib}/django/contrib/sites/locale/??_*/
%dir %{python2_sitelib}/django/contrib/sites/locale/*/LC_MESSAGES
%{python2_sitelib}/django/contrib/sites/*.py*
%{python2_sitelib}/django/contrib/sites/migrations
%{python2_sitelib}/django/contrib/staticfiles/
%{python2_sitelib}/django/contrib/syndication/
%{python2_sitelib}/django/contrib/gis/admin/
%{python2_sitelib}/django/contrib/gis/db/
%{python2_sitelib}/django/contrib/gis/forms/
%{python2_sitelib}/django/contrib/gis/gdal/
%{python2_sitelib}/django/contrib/gis/geometry/
%{python2_sitelib}/django/contrib/gis/geos/
%{python2_sitelib}/django/contrib/gis/management/
%{python2_sitelib}/django/contrib/gis/sitemaps/
%{python2_sitelib}/django/contrib/gis/static/gis/js/OLMapWidget.js
%{python2_sitelib}/django/contrib/gis/templates/
%{python2_sitelib}/django/contrib/gis/utils/
%{python2_sitelib}/django/contrib/messages/storage/
%{python2_sitelib}/django/contrib/sessions/backends/
%{python2_sitelib}/django/forms/
%{python2_sitelib}/django/templatetags/
%{python2_sitelib}/django/core/
%{python2_sitelib}/django/http/
%{python2_sitelib}/django/middleware/
%{python2_sitelib}/django/test/
%{python2_sitelib}/django/conf/*.py*
%{python2_sitelib}/django/conf/project_template/
%{python2_sitelib}/django/conf/app_template/
%{python2_sitelib}/django/conf/urls/
%{python2_sitelib}/django/conf/locale/*/*.py*
%{python2_sitelib}/django/conf/locale/*.py*

%{python2_sitelib}/*.egg-info


%changelog
* Tue Mar 06 2018 Matthias Runge <mrunge@redhat.com> - 1.11.11-1
- update to 1.11.11, fix CVE-2018-7536, CVE-2018-7537
  (rhbz#1552178)

* Fri Feb 02 2018 Matthias Runge <mrunge@redhat.com> - 1.11.10-1
- update to 1.11.10
- fix CVE-2018-6188: Information leakage in AuthenticationForm

* Fri Dec 15 2017 Matthias Runge <mrunge@redhat.com> - 1.11.8-1
- update to 1.11.8

* Wed Sep 06 2017 Matthias Runge <mrunge@redhat.com> - 1.11.5-1
- update to 1.11.5 (rhbz#1488683)

* Wed Aug 02 2017 Matthias Runge <mrunge@redhat.com> - 1.11.4-1
- update to 1.11.4 (rhbz#1477382)

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.11.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Jul 03 2017 Matthias Runge <mrunge@redhat.com> - 1.11.3-1
- Update to 1.11.3 (rhbz#1467029)

* Thu Jun 15 2017 Matthias Runge <mrunge@redhat.com> - 1.11.2-1
- update to 1.11.2 (rhbz#1448664
- add dependency to pytz (rhbz#1458493)

* Thu Apr 06 2017 Matthias Runge <mrunge@redhat.com> - 1.11-1
- update to 1.11 (rhbz#1410268)

* Tue Feb 28 2017 Matthias Runge <mrunge@redhat.com> - 1.10.5-1
- rebase to 1.10.5, fix FTBFS (rhbz#1424135)
- declare bundled libs (rhbz#1401243)

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.10.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 12 2016 Stratakis Charalampos <cstratak@redhat.com> - 1.10.4-2
- Rebuild for Python 3.6
- Disable python3 tests for now

* Fri Dec 02 2016 Matthias Runge <mrunge@redhat.com> - 1.10.4-1
- update to stable 1.10.4 (rhbz#1400730)

* Wed Nov 02 2016 Matthias Runge <mrunge@redhat.com> - 1.10.3-1
- update to 1.10.3 (rhbz#1390782)
- fix CVE-2016-9013, CVE-2016-9014

* Mon Oct 03 2016 Matthias Runge <mrunge@redhat.com> - 1.10.2-1
- update to 1.10.2 (rhbz#1381019)

* Thu Sep 22 2016 Matthias Runge <mrunge@redhat.com> - 1.10.1-1
- rebase to 1.10.1 (rhbz#1338391)

* Thu Jul 21 2016 Matthias Runge <mrunge@redhat.com> - 1-9.8-1
- fix CVE-2016-6186 (rhbz#1357701)

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.9.7-2
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Mon Jun 06 2016 Matthias Runge <mrunge@redhat.com> - 1.9.7-1
- bugfix release

* Tue May 31 2016 Nils Philippsen <nils@redhat.com>
- fix source URL

* Sun May  8 2016 Peter Robinson <pbrobinson@fedoraproject.org> 1.9.6-2
- Put the provives/obsoletes in the right spot for new python naming

* Tue May 03 2016 Matthias Runge <mrunge@redhat.com> - 1.9.6-1
- update to 1.9.6 (rhbz#1323374)

* Tue Mar 08 2016 Matthias Runge <mrunge@redhat.com> - 1.9.4-1
- update to 1.9.4 fixing a regression introduced in last
  upstream fix for CVE-2016-2512

* Wed Mar 02 2016 Matthias Runge <mrunge@redhat.com> - 1.9.3-1
- update to 1.9.3, fixing CVE-2016-2512, CVE-2016-2513
  (rhbz#1313500)

* Thu Feb 11 2016 Matthias Runge <mrunge@redhat.com> - 1.9.2-1
- update to 1.9.2 (rhbz#1266062)
- modernize spec file, provide py2, obsolete python-django

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Jan 04 2016 Matthias Runge <mrunge@redhat.com> - 1.8.8-1
- update to 1.8.8

* Wed Nov 25 2015 Matthias Runge <mrunge@redhat.com> - 1.8.7-1
- Update to 1.8.7 , fixing CVE-2015-8213 (rhbz#1285278)

* Thu Nov 12 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.8.6-2
- Rebuilt for https://fedoraproject.org/wiki/Changes/python3.5

* Thu Nov 05 2015 Matthias Runge <mrunge@redhat.com> - 1.8.6-1
- rebase to 1.8.6 (rhbz#1276914)

* Wed Nov 04 2015 Robert Kuska <rkuska@redhat.com> - 1.8.5-2
- Rebuilt for Python3.5 rebuild

* Mon Nov 02 2015 Matthias Runge <mrunge@redhat.com> - 1.8.5-1
- rebase to 1.8.5 (rhbz#1276914)

* Wed Aug 12 2015 Ville Skyttä <ville.skytta@iki.fi> - 1.8.3-2
- Do not install bash completion for python executables
  (Ville Skyttä, rhbz#1253076)
- CVE-2015-5963 Denial-of-service possibility in logout() view by filling
  session store (rhbz#1254911)
- CVE-2015-5964 Denial-of-service possibility in logout() view by filling
  session store (rhbz#1252891)

* Thu Jul 09 2015 Matthias Runge <mrunge@redhat.com> - 1.8.3-1
- fix DoS via URL validation, CVE-2015-5145 (rhbh#1240526)
- possible header injection due to validators accepting newlines in 
  input, CVE-2015-5144 (rhbz#1239011)
- possible DoS by filling session store, CVE-2015-5143 (rhbz#1239010)
- update to 1.8.3 (rhbz#1241300)

* Mon Jul 06 2015 Matthias Runge <mrunge@redhat.com> - 1.8.2-2
- disable failing py2 tests for now, p3 passes (rhbz#1239824)

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.8.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed May 20 2015 Matthias Runge <mrunge@redhat.com> - 1.8.2-1
- fix CVE-2015-3982 - Fixed session flushing in the cached_db backend
  (rhbz#1223591)

* Mon May 04 2015 Matthias Runge <mrunge@redhat.com> - 1.8.1-1
- update to 1.8.1 (rhbz#1217863)

* Tue Apr 7 2015 Matthias Runge <mrunge@redhat.com> - 1.8-1
- update to 1.8 final

* Mon Mar 23 2015 Matthias Runge <mrunge@redhat.com> - 1.8.0.7.c1
- modernize spec for python3
- 1.8c1 snapshot
- fix for CVE-2015-2316 (rhbz#1203614)
- fix for CVE-2015-2317 (rhbz#1203616)

* Tue Mar 10 2015 Matthias Runge <mrunge@redhat.com> - 1.8-0.6.b2
- 1.8b2 snapshot and security fix

* Wed Feb 25 2015 Matthias Runge <mrunge@redhat.com> - 1.8-0.5.b1
- 1.8b1 snapshot

* Mon Feb 02 2015 Matthias Runge <mrunge@redhat.com> - 1.8-0.4.a1
- remove BR python-sphinx-latex
- fix build on epel7

* Sun Feb 01 2015 Matthias Runge <mrunge@redhat.com> - 1.7.4-1
- update to 1.7.4
- Install bash completion to %%{_datadir}/bash-completion
  (rhbz#1185574), thanks to Ville Skyttä
- add BR python-sphinx-latex

* Tue Jan 20 2015 Matthias Runge <mrunge@redhat.com> - 1.8-0.1.a1
- update to Django-1.8 Alpha1

* Wed Jan 14 2015 Matthias Runge <mrunge@redhat.com> - 1.7.3-1
- update to 1.7.3, fixes CVE-2015-0221 (rhbz#1181946, rhbz#1179679)

* Mon Jan 05 2015 Matthias Runge <mrunge@redhat.com> - 1.7.2-1
- update to 1.7.2 (rhbz#1157514)

* Tue Nov 11 2014 Matthias Runge <mrunge@redhat.com> - 1.7.1-1
- update to 1.7.1 (rhbz#1157514)

* Fri Oct 17 2014 Matthias Runge <mrunge@redhat.com> - 1.7-1
- update to 1.7 (rhbz#1132877)

* Thu Sep 25 2014 Matthias Runge <mrunge@redhat.com> - 1.6.7-1
- update to 1.6.7
- don't own bash-completion dir.

* Thu Aug 21 2014 Matthias Runge <mrunge@redhat.com> - 1.6.6-1
- update to 1.6.6
- fix CVE-2014-0480 (rhbz#1129950)
- fix CVE-2014-0481 (rhbz#1129952)
- fix CVE-2014-0482 (rhbz#1129954)
- fix CVE-2014-0483 (rhbz#1129959)

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed May 28 2014 Kalev Lember <kalevlember@gmail.com> - 1.6.5-2
- Rebuilt for https://fedoraproject.org/wiki/Changes/Python_3.4


* Fri May 16 2014 Matthias Runge <mrunge@redhat.com> - 1.6.5-1
- update to 1.6.5 CVE-2014-1418, CVE-2014-3730 (rhbz#1097935)

* Mon May 12 2014 Matthias Runge <mrunge@redhat.com> - 1.6.4-2
- don't hardcode python3.3

* Wed May 07 2014 Matthias Runge <mrunge@redhat.com> - 1.6.4-1
- update to 1.6.4 fix a potential regression in reverse()

* Tue Apr 22 2014 Matthias Runge <mrunge@redhat.com> - 1.6.3-1
- update to 1.6.3 fixing CVE-2014-0473 and CVE-2014-0474

* Thu Mar 27 2014 Matthias Runge <mrunge@redhat.com> - 1.6.2-2
- remove simplejson requirement
- make bash-completion a sub-package, both main packages can require

* Thu Feb 13 2014 Matthias Runge <mrunge@redhat.com> - 1.6.2-1
- update to 1.6.2 (rhbz#1027766)
- bash completion for python3-django-admin (rhbz#1035987)

* Sun Nov 24 2013 Matěj Cepl <mcepl@redhat.com> - 1.6-1
- update to 1.6 (rhbz#1027766)
