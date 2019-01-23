%global majorversion 1
%global minorversion 7
%global patchversion 0
%global majorminorversion %{majorversion}.%{minorversion}
%global nsversion %{majorversion}.0

Name:           libmodulemd
Version:        %{majorminorversion}%{?patchversion:.%{patchversion}}
Release:        1%{?dist}
Summary:        Module metadata manipulation library

License:        MIT
URL:            https://github.com/fedora-modularity/libmodulemd
Source0:        %{url}/releases/download/%{name}-%{version}/modulemd-%{version}.tar.xz

BuildRequires:  meson
BuildRequires:  pkgconfig
BuildRequires:  gcc
BuildRequires:  pkgconfig(gobject-2.0)
BuildRequires:  pkgconfig(gobject-introspection-1.0)
BuildRequires:  pkgconfig(yaml-0.1)
BuildRequires:  pkgconfig(gtk-doc)
BuildRequires:  valgrind

# Patches
%description
C Library for manipulating module metadata files.
See https://github.com/fedora-modularity/libmodulemd/blob/master/README.md for
more details.


%package devel
Summary:        Development files for libmodulemd
Requires:       %{name}%{?_isa} = %{version}-%{release}


%description devel
Development files for libmodulemd.


%prep
%autosetup -p1 -n modulemd-%{version}


%build
%meson -Ddeveloper_build=false
# ALERT!!! PURE HACK FOR EPEL!
# https://bugzilla.redhat.com/show_bug.cgi?id=1546757
sed -r -i -e "/g-ir-scanner/s/-l(gobject-2.0|glib-2.0|yaml)//g" %{_vpath_builddir}/build.ninja
%meson_build


%check

export LC_CTYPE=C.utf8

%ifarch %{power64}
# Valgrind is broken on ppc64[le] with GCC7:
# https://bugs.kde.org/show_bug.cgi?id=386945
export MMD_SKIP_VALGRIND=1
%endif

%meson_test


%install
%meson_install


%ldconfig_scriptlets


%files
%license COPYING
%doc README.md
%{_bindir}/modulemd-validator
%{_libdir}/%{name}.so.%{majorversion}*
%dir %{_libdir}/girepository-1.0
%{_libdir}/girepository-1.0/Modulemd-%{nsversion}.typelib


%files devel
%{_libdir}/%{name}.so
%{_libdir}/pkgconfig/modulemd.pc
%{_includedir}/modulemd/
%dir %{_datadir}/gir-1.0
%{_datadir}/gir-1.0/Modulemd-%{nsversion}.gir
%dir %{_datadir}/gtk-doc
%dir %{_datadir}/gtk-doc/html
%{_datadir}/gtk-doc/html/modulemd-1.0/

%changelog
* Tue Sep 04 2018 Stephen Gallagher <sgallagh@redhat.com> - 1.6.3-1
- Update to 1.6.3
- Drop upstreamed patch
- Don't return ModuleStream objects from modulemd_module_new_all_from_*_ext()
- Ensure that Component buildorder property is signed
- Work around optimization bug
- Don't crash dumping translation events without summary or desc

* Wed Aug 15 2018 Stephen Gallagher <sgallagh@redhat.com> - 1.6.2-2.1
- Remove Obsoletes: python-modulemd from EPEL

* Thu Aug 09 2018 Stephen Gallagher <sgallagh@redhat.com> - 1.6.2-2
- Fix backwards-incompatible API change
- Resolves: rhbz#1607083

* Tue Aug 07 2018 Stephen Gallagher <sgallagh@redhat.com> - 1.6.2-1
- Update to 1.6.2
- Make buildorder a signed integer to match modulemd specification

* Mon Jul 23 2018 Stephen Gallagher <sgallagh@redhat.com> - 1.6.1-2
- Obsolete unsupported pythonX-modulemd packages

* Fri Jul 20 2018 Stephen Gallagher <sgallagh@redhat.com> - 1.6.1-1
- Update to 1.6.1
- Fix header include ordering
- Suppress empty sections from .dump() ordering

* Wed Jul 18 2018 Stephen Gallagher <sgallagh@redhat.com> - 1.6.0-1
- Update to 1.6.0
- Adds Modulemd.ModuleStream object, deprecating Modulemd.Module
- Adds Modulemd.Translation and Modulemd.TranslationEntry objects
- Adds Modulemd.ImprovedModule object that collects streams, defaults and
  translations together
- Adds new Modulemd.index_from_*() funtions to get a hash table of
  Modulemd.ImprovedModule objects for easier searching
- Moves function documentation to the public headers
- Corrects the license headers to MIT (they were incorrectly listed as MITNFA
  in previous releases)
- Makes the "eol" field optional for Modulemd.ServiceLevel
- Clean up HTML documentation
- Fixes a type error on 32-bit systems

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sat Jun 23 2018 Stephen Gallagher <sgallagh@redhat.com> - 1.5.2-1
- Update to libdmodulemd 1.5.2
- Don't free uninitialized memory

* Fri Jun 22 2018 Stephen Gallagher <sgallagh@redhat.com> - 1.5.1-2
- Fix buildopts property not being initialized

* Tue Jun 19 2018 Stephen Gallagher <sgallagh@redhat.com> - 1.5.1-1
- Update to version 1.5.1
- Re-enable build-time tests

* Mon Jun 18 2018 Stephen Gallagher <sgallagh@redhat.com> - 1.5.0-2
- Temporarily disable build-time tests

* Mon Jun 18 2018 Stephen Gallagher <sgallagh@redhat.com> - 1.5.0-1
- Update to version 1.5.0
- Adds support for "intents" in Modulemd.Defaults
- Adds `Modulemd.get_version()`
- Adds support for RPM whitelists in the buildopts
- Adds a new object: Modulemd.Buildopts
- Deprecates Modulemd.Module.get_rpm_buildopts()
- Deprecates Modulemd.Module.set_rpm_buildopts()
- Fixes some missing license blurbs

* Tue May 08 2018 Stephen Gallagher <sgallagh@redhat.com> - 1.4.1-1
- Update to version 1.4.1
- Improve output from modulemd-validator
- Drop upstreamed patches

* Wed Apr 25 2018 Stephen Gallagher <sgallagh@redhat.com> - 1.4.0-2
- Fix pointer math error
- Fix compilation failure in Fedora build system

* Wed Apr 25 2018 Stephen Gallagher <sgallagh@redhat.com> - 1.4.0-1
- Update to version 1.4.0
- Adds new API for returning failed YAML subdocuments
- Stop emitting log messages by default (polluting consumer logs)
- Validate RPM artifacts for proper NEVRA format
- Improve the validator tool
- Drop upstreamed patch

* Mon Apr 16 2018 Stephen Gallagher <sgallagh@redhat.com> - 1.3.0-2
- Fix serious error in modulemd-defaults emitter

* Fri Apr 13 2018 Stephen Gallagher <sgallagh@redhat.com> - 1.3.0-1
- Update to version 1.3.0
- New Public Objects:
  * Modulemd.Prioritizer - tool to merge module defaults
- New Public Functions:
  * Modulemd.SimpleSet.is_equal()
  * Modulemd.Defaults.copy()
  * Modulemd.Defaults.merge()

* Wed Apr 04 2018 Stephen Gallagher <sgallagh@redhat.com> - 1.2.0-1
- Update to version 1.2.0
- New Functions:
  * Modulemd.objects_from_file()
  * Modulemd.objects_from_string()
  * Modulemd.dump()
  * Modulemd.dumps()
  * Modulemd.Defaults.new_from_file()
  * Modulemd.Defaults.new_from_string()
- Deprecated Functions:
  * Modulemd.Module.new_all_from_file()
  * Modulemd.Module.new_all_from_file_ext()
  * Modulemd.Module.new_all_from_string()
  * Modulemd.Module.new_all_from_string_ext()
  * Modulemd.Module.dump_all()
  * Modulemd.Module.dumps_all()
- Bugfixes
  * Properly use G_BEGIN_DECLS and G_END_DECLS in headers
  * Assorted fixes for memory ownership in GObject Introspection

* Fri Mar 23 2018 Stephen Gallagher <sgallagh@redhat.com> - 1.1.3-2
- Fix missing G_END_DECL from public headers

* Mon Mar 19 2018 Stephen Gallagher <sgallagh@redhat.com> - 1.1.3-1
- Fix numerous memory leaks
- Drop upstreamed patch

* Thu Mar 15 2018 Stephen Gallagher <sgallagh@redhat.com> - 1.1.2-1
- Update to version 1.1.2
- Revert backwards-incompatible API change
- Fix version string in pkgconfig file

* Thu Mar 15 2018 Stephen Gallagher <sgallagh@redhat.com> - 1.1.1-1
- Update to version 1.1.1
- Make default stream and profiles optional
- Fixes: https://github.com/fedora-modularity/libmodulemd/issues/25
- Fixes: https://github.com/fedora-modularity/libmodulemd/issues/26
- Fixes: https://github.com/fedora-modularity/libmodulemd/issues/27

* Wed Mar 14 2018 Stephen Gallagher <sgallagh@redhat.com> - 1.1.0-1
- Update to version 1.1.0
- Adds support for handling modulemd-defaults YAML documents
- Adds peek()/dup() routines to all object properties
- Adds Modulemd.Module.dup_nsvc() to retrieve the canonical form of the unique module identifier.
- Adds support for boolean types in the XMD section
- Revert obsoletion of pythonX-modulemd packages for now

* Tue Mar 13 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.0.4-2
- Obsolete unsupported pythonX-modulemd packages

* Tue Feb 27 2018 Stephen Gallagher <sgallagh@redhat.com> - 1.0.4-1
- Update to 1.0.4
- Rework version autodetection
- Avoid infinite loop on unparseable YAML

* Sun Feb 25 2018 Stephen Gallagher <sgallagh@redhat.com> - 1.0.3-1
- RPM components are properly emitted when no module components exist
- Parser works around late determination of modulemd version

* Fri Feb 16 2018 Stephen Gallagher <sgallagh@redhat.com> - 1.0.2-1
- Be more strict with certain parser edge-cases
- Replace popt argument processing with glib
- Drop upstreamed patches

* Thu Feb 15 2018 Stephen Gallagher <sgallagh@redhat.com> - 1.0.1-2
- Handle certain unlikely format violations

* Thu Feb 15 2018 Stephen Gallagher <sgallagh@redhat.com> - 1.0.1-1
- Support modulemd v2
- Add tool to do quick validation of modulemd
- Fix memory management
- Warn and ignore unparseable sub-documents in the YAML
- Fix several memory issues detected by Coverity scan

* Tue Feb 06 2018 Stephen Gallagher <sgallagh@redhat.com> - 0.2.2-1
- Update to libmodulemd 0.2.2
- Fix numerous minor memory leaks
- Fix issues with EOL/SL dates

* Tue Feb 06 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.2.1-3
- Own appropriate directories

* Fri Feb 02 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.2.1-2
- Switch to %%ldconfig_scriptlets

* Fri Jan 05 2018 Stephen Gallagher <sgallagh@redhat.com> - 0.2.1-1
- Update to libmodulemd 0.2.1
- Add 'name' property for Profiles

* Thu Oct 05 2017 Stephen Gallagher <sgallagh@redhat.com> - 0.2.0-2
- Add missing BuildRequires for gtk-doc

* Thu Oct 05 2017 Stephen Gallagher <sgallagh@redhat.com> - 0.2.0-1
- Update to libmodulemd 0.2.0
- Adds gtk-doc generated documentation
- (ABI-break) Makes all optional properties accept NULL as a value to clear
  them
- (ABI-break) Modulemd.SimpleSet takes a STRV (char **) instead of a
  GLib.PtrArray
- Fixes a bug where the name was not always set for components
- Adds support for dumping YAML from the introspected API
- Includes add/remove routines for profiles

* Sat Sep 30 2017 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.1.0-5
- Use %%_isa in Requires for main package from devel

* Mon Sep 18 2017 Stephen Gallagher <sgallagh@redhat.com> - 0.1.0-4
- Correct the license to MIT

* Mon Sep 18 2017 Stephen Gallagher <sgallagh@redhat.com> - 0.1.0-3
- Modifications requested during package review

* Fri Sep 15 2017 Stephen Gallagher <sgallagh@redhat.com> - 0.1.0-2
- First public release

