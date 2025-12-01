%if 0%{?rhel} && 0%{?rhel} <= 7
%{!?py2_build: %global py2_build %{__python2} setup.py build}
%{!?py2_install: %global py2_install %{__python2} setup.py install --skip-build --root %{buildroot}}
%endif

%if (0%{?fedora} >= 21 || 0%{?rhel} >= 8)
%global with_python3 1
%endif

%define srcname check-cluster-state-dependent
%define project check_cluster_state_dependent
%define version 0.13
%define release 1
%define sum Cygnus Networks GmbH %{srcname} package

Name:           %{srcname}
Version:        %{version}
Release:        %{release}%{?dist}
Summary:        %{sum}
License:        proprietary
Source0:        %{srcname}-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  python2-devel, python-setuptools
%if 0%{?with_check}
BuildRequires:  pytest
%endif # with_check
Requires:       python-setuptools

%{?python_provide:%python_provide python-%{project}}

%if 0%{?with_python3}
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
%if 0%{?with_check}
BuildRequires:  python3-pytest
%endif # with_check
%endif # with_python3

%description
%{sum}

%if 0%{?with_python3}
%package -n python3-%{project}
Summary:        %{sum}
%{?python_provide:%python_provide python3-%{project}}
Requires:       python3-setuptools

%description -n python3-%{project}
%{sum}
%endif # with_python3

%prep
%setup -q -n %{srcname}-%{version}

%build
%py2_build

%if 0%{?with_python3}
%py3_build
%endif # with_python3


%install
%py2_install

%if 0%{?with_python3}
%py3_install
%endif # with_python3

%if 0%{?with_check}
%check
LANG=en_US.utf8 py.test-%{python2_version} -vv tests

%if 0%{?with_python3}
LANG=en_US.utf8 py.test-%{python3_version} -vv tests
%endif # with_python3
%endif # with_check

%files
%{_bindir}/check_cluster_state_dependent
%{python2_sitelib}/check_cluster_state_dependent-%{version}-py2.*.egg-info
%if 0%{?with_python3}
%files -n python3-%{project}
%{_bindir}/check_cluster_state_dependent
%{python3_sitelib}/check_cluster_state_dependent-%{version}-py3.*.egg-info
%endif # with_python3
