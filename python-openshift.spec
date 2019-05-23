%if 0%{?rhel} == 7
%bcond_with    python3
%bcond_without python2
%else
%bcond_with    python2
%bcond_without python3
%endif

%global library openshift

%if 0%{?rhel} == 7

%global py3 python%{python3_pkgversion}
%else
%global py3 python3
%endif

Name:       python-%{library}
Version:    0.9.0a3
Release:    1%{?dist}
Summary:    Python client for the OpenShift API  
License:    ASL 2.0
URL:        https://github.com/openshift/openshift-restclient-python
Source0:    https://github.com/openshift/openshift-restclient-python/archive/v%{version}.tar.gz
BuildArch:  noarch
Epoch:      1

%if 0%{?with_python2}
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
%endif

%if 0%{?with_python3}
%package -n %{py3}-%{library}
Summary: Python client for the OpenShift API 
BuildRequires: %{py3}-devel
BuildRequires: %{py3}-setuptools
BuildRequires: git

Requires: %{py3}
Requires: %{py3}-dictdiffer
Requires: %{py3}-kubernetes
Requires: %{py3}-string_utils
Requires: %{py3}-requests
Requires: %{py3}-ruamel-yaml
Requires: %{py3}-six
Requires: %{py3}-jinja2

%description -n %{py3}-%{library}
Python client for the OpenShift API 
%endif # with_python3

#recommonmark not available for docs in EPEL
%if 0%{?fedora}
%package doc
Summary: Documentation for %{name}.
Provides: %{name}-doc
%if 0%{?with_python3}
BuildRequires: %{py3}-sphinx
BuildRequires: %{py3}-recommonmark
%else
BuildRequires: python2-sphinx
BuildRequires: python2-recommonmark
%endif
%description doc
%{summary}
%endif

%description
Python client for the OpenShift API 

%prep
%autosetup -n openshift-restclient-python-%{version} -S git
#there is no include in RHEL7 setuptools find_packages
#the requirements are also done in an non-backwards compatible way
%if 0%{?rhel}
sed -i -e "s/find_packages(include='openshift.*')/['openshift', 'openshift.dynamic', 'openshift.helper']/g" setup.py
sed -i -e '30s/^/REQUIRES = [\n    "dictdiffer",\n    "jinja2",\n    "kubernetes",\n    "setuptools",\n    "six",\n    "ruamel.yaml",\n    "python-string-utils",\n]\n/g' setup.py
sed -i -e "s/extract_requirements('requirements.txt')/REQUIRES/g" setup.py
#sed -i -e '14,21d' setup.py
%endif

%build
%if 0%{?with_python2}
%py2_build
%endif
%if 0%{?with_python3}
%py3_build
%endif

%if 0%{?fedora}
sphinx-build doc/source/ html
%{__rm} -rf html/.buildinfo
%endif

%install
%if 0%{?with_python2}
%py2_install
%endif
%if 0%{?with_python3}
%py3_install
%endif

%check
#test dependencies are unpackaged

%if 0%{?with_python2}
%files -n python2-%{library}
%license LICENSE
%{python2_sitelib}/%{library}/*
%{python2_sitelib}/%{library}-*.egg-info
%exclude %{python2_sitelib}/scripts
%exclude /usr/requirements.txt/requirements.txt
%{_bindir}/openshift-ansible-gen
%endif

%if 0%{?with_python3}
%files -n %{py3}-%{library}
%license LICENSE
%{python3_sitelib}/%{library}/*
%{python3_sitelib}/%{library}-*.egg-info
%exclude %{python3_sitelib}/scripts
%exclude /usr/requirements.txt/requirements.txt
%{_bindir}/openshift-ansible-gen
%endif

%if 0%{?fedora}
%files doc
%license LICENSE
%doc html
%endif

%changelog
* Tue Dec 4 2018 Jason Montleon <jmontleo@redhat.com> 0.9.0-1
- Bump Version to 0.9.0
- Disable python 2 and enable python 3 builds for Fedora

* Tue Nov 06 2018 Jason Montleon <jmontleo@redhat.com> 0.8.0-1
- Fix tag condition (fabian@fabianism.us)
- Add watch to dynamic client (#221) (fabian@fabianism.us)
- Pin flake8 (fabian@fabianism.us)
- Do not decode response data in Python2 (#225)
  (16732494+wallecan@users.noreply.github.com)
- ResourceContainer does not contain delete method (#227)
  (mosonkonrad@gmail.com)
- Add basic documentation for dynamic client verbs to README (#222)
  (fabian@fabianism.us)
- Add support for *List kinds (#213) (fabian@fabianism.us)
- Add validate helper function (#199) (will@thames.id.au)
- DynamicApiError: add a summary method (#211) (pierre-louis@libregerbil.fr)
- Allow less strict kubernetes version requirements (#207) (will@thames.id.au)
- Add behavior-based tests for dynamic client (#208) (fabian@fabianism.us)
- Provide 'append_hash' for ConfigMaps and Secrets (#196) (will@thames.id.au)
- Allow creates on subresources properly (#201) (fabian@fabianism.us)
- Rename async to async_req for compatibility with python3 and kubernetes 7
  (#197) (fabian@fabianism.us)
- Update kube_config to support concurrent clusters (#193)
  (tdecacqu@redhat.com)

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

