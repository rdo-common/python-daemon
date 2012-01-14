%{!?pyver: %define pyver %(%{__python} -c "import sys ; print sys.version[:3]")}

Name:           python-daemon
Version:        1.6
Release:        2%{?dist}
Summary:        Library to implement a well-behaved Unix daemon process

Group:          Development/Languages
License:        Python
URL:            http://pypi.python.org/pypi/python-daemon/
Source0:        http://pypi.python.org/packages/source/p/python-daemon/%{name}-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  python-devel, python-setuptools
BuildRequires:  python-lockfile python-minimock
Requires:       python-lockfile

%description
This library implements the well-behaved daemon specification of PEP 3143,
"Standard daemon process library".

%prep
%setup -q

sed -i -e '/^#!\//, 1d' daemon/version/version_info.py


%build
%{__python} setup.py build


%install
%{__python} setup.py install -O1 --skip-build --root %{buildroot}
rm -fr %{buildroot}%{python_sitelib}/tests


# Test suite requires minimock and lockfile
#Disabled tests as pidlockfile is not anymore in the lastest python-lockfile
#%check
#PYTHONPATH=$(pwd) nosetests

%files
%doc LICENSE.PSF-2
%{python_sitelib}/daemon/
%{python_sitelib}/python_daemon-%{version}-py%{pyver}.egg-info/

%changelog
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

