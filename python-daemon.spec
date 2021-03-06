
# 24 picked since that's when the package was updated to contain a version
# capable of python3.  If we're willing to push the update to older Fedora
# releases, the python3 package can go to older releases as well.
%if 0%{?fedora} >= 23
%global with_python3 1
%else
%global with_python3 0
%endif

Name:           python-daemon
Version:        2.1.2
Release:        8%{?dist}
Summary:        Library to implement a well-behaved Unix daemon process

Group:          Development/Languages
# Some build scripts and test franework are licensed GPLv3+ but htose aren't shipped
License:        ASL2.0
URL:            http://pypi.python.org/pypi/python-daemon/
Source0:        https://pagure.io/releases/python-daemon/python-daemon-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  python2-devel, python2-setuptools
BuildRequires:  python2-testscenarios
BuildRequires:  python-docutils
BuildRequires:  python-lockfile
BuildRequires:  python2-mock
%if 0%{?with_python3}
BuildRequires:  python3-devel, python3-setuptools
BuildRequires:  python3-testscenarios
BuildRequires:  python3-docutils
BuildRequires:  python3-lockfile
BuildRequires:  python3-mock
BuildRequires:  python3-testtools
%endif

%global _description\
This library implements the well-behaved daemon specification of PEP 3143,\
"Standard daemon process library".\
\
This is the python2 version of the library.

%description %_description

%package -n python2-daemon
Summary: %summary
Requires:       python-lockfile
Requires:       python-docutils
%{?python_provide:%python_provide python2-daemon}

%description -n python2-daemon %_description

%if 0%{?with_python3}
%package -n python3-daemon
Summary:        Library to implement a well-behaved Unix daemon process
Requires:       python3-lockfile
Requires:       python3-docutils

%description -n python3-daemon
This library implements the well-behaved daemon specification of PEP 3143,
"Standard daemon process library".

This is the python3 version of the library.
%endif

%prep
%setup -q

%if 0%{?with_python3}
rm -rf %{py3dir}
cp -ar . %{py3dir}
%endif

%build
%{__python2} setup.py build

%if 0%{?with_python3}
pushd %{py3dir}
%{__python3} setup.py build
popd
%endif

%install
%{__python2} setup.py install --skip-build --root %{buildroot}
rm -fr %{buildroot}%{python2_sitelib}/tests

%if 0%{?with_python3}
pushd %{py3dir}
%{__python3} setup.py install --skip-build --root %{buildroot}
rm -fr %{buildroot}%{python3_sitelib}/tests
popd
%endif


# Test suite requires minimock and lockfile
%check
PYTHONPATH=$(pwd) %{__python2} -m unittest discover

%if 0%{?with_python3}
pushd %{py3dir}
PYTHONPATH=$(pwd) %{__python3} -m unittest discover
%endif

%files -n python2-daemon
%license LICENSE.ASF-2
%{python2_sitelib}/daemon/
%{python2_sitelib}/python_daemon-%{version}-py%{python2_version}.egg-info/

%if 0%{?with_python3}
%files -n python3-daemon
%license LICENSE.ASF-2
%{python3_sitelib}/daemon/
%{python3_sitelib}/python_daemon-%{version}-py%{python3_version}.egg-info/
%endif

%changelog
* Mon Feb 12 2018 Iryna Shcherbina <ishcherb@redhat.com> - 2.1.2-8
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sun Dec 17 2017 Kevin Fenzi <kevin@scrye.com> - 2.1.2-6
- Add dep on python2-docutils. Fixes bug #1478196

* Sat Aug 19 2017 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 2.1.2-5
- Python 2 binary package renamed to python2-daemon
  See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 2.1.2-2
- Rebuild for Python 3.6

* Wed Nov 09 2016 Kevin Fenzi <kevin@scrye.com> - 2.1.2-1
- Update to 2.1.2. Fixes bug #1389593

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1.1-2
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Sun Apr 10 2016 Kevin Fenzi <kevin@scrye.com> - 2.1.1-1
- Update to 2.1.1. Fixes bug #1234933

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Nov 30 2015 Toshio Kuratomi <toshio@fedoraproject.org> - - 2.1.0-1
- Update to newer upstream.
- Create a python3 subpackage since upstream supports it
- Note that newer upstream has relicensed to Apache 2.0

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Aug  4 2014 Thomas Spura <tomspur@fedoraproject.org> - 1.6-7
- enable tests again as lockfile was fixed

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Thu Jul 14 2011 Kushal Das <kushal@fedoraproject.org> - 1.6-1
- New release of source

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Jul 22 2010 David Malcolm <dmalcolm@redhat.com> - 1.5.2-2
- Rebuilt for https://fedoraproject.org/wiki/Features/Python_2.7/MassRebuild

* Wed Dec 23 2009 Thomas Spura <tomspur@fedoraproject.org> - 1.5.2-1
- add missing BR: python-nose
- also add lockfile as R (bug #513546)
- update to 1.5.2

* Wed Dec 23 2009 Thomas Spura <tomspur@fedoraproject.org> - 1.5.1-2
- add missing BR: minimock and lockfile -> testsuite works again
- remove patch, use sed instead

* Wed Oct 07 2009 Luke Macken <lmacken@redhat.com> - 1.5.1-1
- Update to 1.5.1
- Remove conflicting files (#512760)

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Jun 24 2009 Kushal Das <kushal@fedoraproject.org> 1.4.6-1
- Initial release

