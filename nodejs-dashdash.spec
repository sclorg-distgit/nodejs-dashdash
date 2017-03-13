%{?scl:%scl_package nodejs-%{srcname}}
%{!?scl:%global pkg_name %{name}}

%{?nodejs_find_provides_and_requires}

%global enable_tests 0
%global srcname dashdash

%global owner trentm

Name:           %{?scl_prefix}nodejs-%{srcname}
Version:        1.13.1
Release:        1%{?dist}
Summary:        A light, featureful and explicit option parsing library for node.js
License:        MIT
URL:            https://github.com/trentm/node-dashdash
Source0:        https://github.com/%{owner}/node-%{srcname}/archive/%{version}.tar.gz

BuildArch:      noarch

ExclusiveArch:  %{nodejs_arches} noarch

BuildRequires:  %{?scl_prefix}nodejs-devel

%if 0%{?enable_tests}
BuildRequires:  %{?scl_prefix}npm(nodeunit)
BuildRequires:  %{?scl_prefix}npm(assert-plus)
%endif

%description
%{summary}.

%prep
%setup -n %{pkg_name}-%{version} -qn node-%{srcname}-%{version}
#%nodejs_fixdep assert-plus
rm -rf node_modules

%build
#nothing to do

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/%{srcname}

cp -pr package.json lib/ \
    %{buildroot}%{nodejs_sitelib}/%{srcname}

%nodejs_symlink_deps

%if 0%{?enable_tests}

%check
%nodejs_symlink_deps --check
nodeunit test/*.test.js
%endif

%files
%doc CHANGES.md AUTHORS README.md TODO.txt examples
%license LICENSE.txt
%{nodejs_sitelib}/%{srcname}

%changelog
* Thu Sep 22 2016 Zuzana Svetlikova <zsvetlik@redhat.com> - 1.13.1-1
- Update

* Thu Sep 22 2016 Zuzana Svetlikova <zsvetlik@redhat.com> - 1.10.1-5
- Add requires and provides macro

* Thu Sep 22 2016 Zuzana Svetlikova <zsvetlik@redhat.com> - 1.10.1-4
- Built for scl

* Sun Aug 28 2016 Piotr Popieluch <piotr1212@gmail.com> - - 1.10.1-3
- fixdep assert-plus

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.10.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sun Dec 13 2015 Piotr Popieluch <piotr1212@gmail.com> - 1.10.1-1
- Initial package
