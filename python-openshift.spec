%global with_python3 0

%global library openshift

Name:       python-%{library}
Version:    0.8.1
Release:    12%{?dist}
Summary:    Python client for the OpenShift API  
License:    MIT
URL:        https://github.com/openshift/openshift-restclient-python
Source0:    https://github.com/openshift/openshift-restclient-python/python-openshift-%{version}.tar.gz
BuildArch:  noarch
Epoch:      1

%package -n python2-%{library}
Summary:    Python client for the OpenShift API  
%{?python_provide:%python_provide python2-%{library}}

BuildRequires: python2-devel
BuildRequires: python-setuptools
BuildRequires: git

Requires: python2
Requires: python2-dictdiffer
Requires: python2-kubernetes
Requires: python2-string_utils
Requires: python-requests
Requires: python2-ruamel-yaml
Requires: python-six
Requires: python-jinja2

%description -n python2-%{library}
Python client for the kubernetes API.

%if 0%{?with_python3}
%package -n python3-%{library}
Summary: Python client for the OpenShift API 
%if 0%{?rhel}
%{?python_provide:%python_provide python%{python3_pkgversion}-%{library}}
%else
%{?python_provide:%python_provide python3-%{library}}
%endif

%if 0%{?rhel}
BuildRequires: python%{python3_pkgversion}-devel
BuildRequires: python%{python3_pkgversion}-setuptools
%else
BuildRequires: python3-devel
BuildRequires: python3-setuptools
%endif
BuildRequires: git

%if 0%{?rhel}
Requires: python%{python3_pkgversion}
Requires: python%{python3_pkgversion}-dictdiffer
Requires: python%{python3_pkgversion}-jinja2
Requires: python%{python3_pkgversion}-kubernetes
Requires: python%{python3_pkgversion}-string_utils
Requires: python%{python3_pkgversion}-ruamel-yaml
Requires: python%{python3_pkgversion}-six

%else
Requires: python3
Requires: python3-dictdiffer
Requires: python3-jinja2
Requires: python3-kubernetes
Requires: python3-string_utils
Requires: python3-ruamel-yaml
Requires: python3-six
%endif

%description -n python3-%{library}
Python client for the OpenShift API 
%endif # with_python3

%description
Python client for the OpenShift API 

%prep
%autosetup -S git
#there is no include in RHEL7 setuptools find_packages
#the requirements are also done in an non-backwards compatible way
%if 0%{?rhel}
sed -i -e "s/find_packages(include='openshift.*')/['openshift', 'openshift.ansiblegen', 'openshift.client', 'openshift.client.apis', 'openshift.client.models', 'openshift.config', 'openshift.docs', 'openshift.dynamic', 'openshift.helper', 'openshift.test']/g" setup.py
sed -i -e '30s/^/REQUIRES = [\n    "certifi",\n    "ipaddress",\n    "oauth2client",\n    "setuptools",\n    "six",\n    "urllib3!=1.21",\n    "python-dateutil",\n    "pyyaml",\n    "websocket-client",\n]\n/g' setup.py
sed -i -e "s/extract_requirements('requirements.txt')/REQUIRES/g" setup.py
#sed -i -e '14,21d' setup.py
%endif

%build
%if 0%{?rhel}
%py_build
%else
%py2_build
%endif
%if 0%{?with_python3}
%py3_build
%endif

%install
%if 0%{?rhel}
%py_install
%else
%py2_install
%endif
%if 0%{?with_python3}
%py3_install
%endif

%check

%files -n python2-%{library}
%license LICENSE
%{python2_sitelib}/%{library}/*
%{python2_sitelib}/%{library}-*.egg-info
%exclude %{python2_sitelib}/scripts
%exclude /usr/requirements.txt/requirements.txt
%exclude /usr/custom_objects_spec.json/custom_objects_spec.json
#TODO: What about for python3?
%if %{with_python3} == 0
%{_bindir}/openshift-ansible-gen
%endif

%if 0%{?with_python3}
%files -n python3-%{library}
%license LICENSE
%{python3_sitelib}/%{library}/*
%{python3_sitelib}/%{library}-*.egg-info
%exclude %{python3_sitelib}/scripts
%{_bindir}/openshift-ansible-gen
%endif # with_python3

%changelog
* Mon Aug 06 2018 David Zager <david.j.zager@gmail.com> 0.6.2-12
- Fix decode issue (#192) (lostonamountain@gmail.com)
- b64encode expects bytes not string (fridolin@redhat.com)
- Update releasers for 3.11 (david.j.zager@gmail.com)

* Mon Jul 23 2018 David Zager <david.j.zager@gmail.com> 0.6.2-11
- include version update script (fabian@fabianism.us)
- Version bump to 0.6.2 (fabian@fabianism.us)

* Thu Jul 05 2018 David Zager <david.j.zager@gmail.com> 0.6.1-10
- Install openshift.dynamic in RPM (#180) (dzager@redhat.com)

* Thu Jul 05 2018 David Zager <david.j.zager@gmail.com> 0.6.1-9
- Call functions on resource fields if they don't exist as name (#179)
  (will@thames.id.au)
- Release 0.6.1 (fabian@fabianism.us)
- Fix typo in argument passing for patch in dynamic client. (#176)
  (fabian@fabianism.us)
- Prevent duplicate keys when creating resource (#178) (dzager@redhat.com)
- Allow content type specification in resource.patch (#174) (will@thames.id.au)
- release 0.6.0 (fabian@fabianism.us)
- Default singular name to name sans last letter (#173) (fabian@fabianism.us)
- Serialize body more thoroughly, won't always be passed as kwarg (#172)
  (fabian@fabianism.us)
- decode response data for python3 compatibility (#171) (fabian@fabianism.us)
- add dynamic client (#167) (fabian@fabianism.us)
- Fixes a bug when running fix_serialization on Kubernetes ExternalName… (#161)
  (zapur1@users.noreply.github.com)

* Tue Feb 27 2018 David Zager <david.j.zager@gmail.com> 0.5.0-8
- Bug 1546843- RuntimeRawExtension objects will now deserialize
  (fabian@fabianism.us)
- Add compatiblity matrix (fabian@fabianism.us)

* Thu Feb 22 2018 David Zager <david.j.zager@gmail.com> 0.5.0-7
- Update client for release k8s-client 5.0 (david.j.zager@gmail.com)
- Lint fix (chousekn@redhat.com)
- Add 'Bearer' to auth header (chousekn@redhat.com)
- All objects will now be instantiated with the proper configuration
  (fabian@fabianism.us)
- Restore API and model matching (chousekn@redhat.com)

* Thu Feb 08 2018 David Zager <david.j.zager@gmail.com> 0.5.0.a1-6
- Allow beta k8s client (david.j.zager@gmail.com)
- Update client to use k8s client 5 (david.j.zager@gmail.com)

* Fri Jan 19 2018 David Zager <david.j.zager@gmail.com> 0.4.0.a1-5
- Add object to primitives, treat as string for now (fabian@fabianism.us)
- update version to match new scheme (fabian@fabianism.us)
- regen modules (fabian@fabianism.us)
- Don't exclude modules that appear in both k8s and openshift from codegen
  (fabian@fabianism.us)
- Prefer openshift models to kubernetes models (fabian@fabianism.us)
- extra escape characters (fabian@fabianism.us)
- Update deployment condition to enforce python versioning standards
  (fabian@fabianism.us)
- Update releasers (david.j.zager@gmail.com)

* Tue Jan 16 2018 David Zager <david.j.zager@gmail.com> 0.4.0-4
- fix linting (fabian@fabianism.us)
- Fix ansible module generation for 1.8/3.8 (fabian@fabianism.us)
- Remove old OpenShift versions (david.j.zager@gmail.com)
- Update watch test (fabian@fabianism.us)
- fix a few nil value errors (fabian@fabianism.us)
- regen modules (fabian@fabianism.us)
- Fixed some errors around object instantiation in the helpers
  (fabian@fabianism.us)
- Generated code (david.j.zager@gmail.com)
- Essentials for updating client-python to 4.0 (david.j.zager@gmail.com)
- Helper base cleanup (#132) (chousekn@redhat.com)

* Mon Dec 04 2017 Jason Montleon <jmontleo@redhat.com> 0.3.4-3
- prefix test names with the cluster type (openshift/k8s) to prevent collision
  (fabian@fabianism.us)
- after the argspec is fully created, go through all aliases and remove any
  collisions (fabian@fabianism.us)
- Add test for build config (fabian@fabianism.us)
- Update _from conversion to handle all python keywords (fabian@fabianism.us)
- Handle _from -> from and vice versa in ansible helper (fabian@fabianism.us)
- add exclude for new file that won't be packaged (#125) (jmontleo@redhat.com)
- Fix k8s_v1beta1_role_binding 404s (#122) (fabian@fabianism.us)
- Pin pytest version due to broken internal API (fabian@fabianism.us)
- Add custom_objects_spec.json to package data
  (ceridwen@users.noreply.github.com)

* Fri Nov 03 2017 Jason Montleon <jmontleo@redhat.com> 0.3.4-2
- Update version 

* Fri Nov 03 2017 Jason Montleon <jmontleo@redhat.com> 0.3.3-8
- Bug 1508969 - Add foreground propagation policy (david.j.zager@gmail.com)
- Document how to use the Dockerfile (david.j.zager@gmail.com)
- Add Dockerfile (david.j.zager@gmail.com)
- add unit test for watch (fabian@fabianism.us)
- Bump version (fabian@fabianism.us)
- Support watching openshift resources (fabian@fabianism.us)

* Fri Oct 13 2017 Jason Montleon <jmontleo@redhat.com> 0.3.3-7
- add python-requests rpm dep

* Fri Oct 13 2017 Jason Montleon <jmontleo@redhat.com> 0.3.3-6
- Fix module Python interpreter (chousekn@redhat.com)
- Version bump (fabian@fabianism.us)
- fix version regex and api_version formatting to prevent filtering out valid
  APIs (fabian@fabianism.us)

* Fri Oct 06 2017 Jason Montleon <jmontleo@redhat.com> 0.3.2-5
- ignore requirements.txt in packaging

* Fri Oct 06 2017 Jason Montleon <jmontleo@redhat.com> 0.3.2-4
- 

* Fri Oct 06 2017 Jason Montleon <jmontleo@redhat.com> 0.3.2-3
- make source name match package name

* Fri Oct 06 2017 Jason Montleon <jmontleo@redhat.com> 0.3.2-2
- Fix source name 

* Fri Oct 06 2017 Jason Montleon <jmontleo@redhat.com> 0.3.2-1
- new package built with tito

* Wed May 10 2017 Jason Montleon <jmontleo@redhat.com> 1.0.0-0.3
- Initial Build

