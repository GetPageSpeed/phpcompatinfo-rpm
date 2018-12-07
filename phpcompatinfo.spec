# License: MIT
# http://opensource.org/licenses/MIT

Name: phpcompatinfo
Version: 5.1.0
Release: 1%{?dist}
Summary: Find the minimum version and the extensions required for a piece of PHP code to run

License: BSD-3-clauses License
URL: http://php5.laurent-laville.org/compatinfo/
Source0: http://bartlett.laurent-laville.org/get/phpcompatinfo-%{version}.phar

BuildArch: noarch

Requires:  php(language) >= 5.5

%description
PHP CompatInfo is a library that can find the minimum version 
and the extensions required for a piece of code to run.


%prep
# Nothing to do


%build
# Nothing to do


%install
%{__rm} -rf $RPM_BUILD_ROOT
%{__mkdir} -p $RPM_BUILD_ROOT%{_bindir}
%{__install} -m 755 -p %SOURCE0 $RPM_BUILD_ROOT%{_bindir}/%{name}

%files
%defattr(-,root,root)
%{_bindir}/%{name}

%changelog
* Fri Dec 07 2018 Danila Vershinin <info@getpagespeed.com> 5.1.0-1
- upstream version auto-updated to 5.1.0

* Sat May 12 2018 Danila Vershinin <info@getpagespeed.com> 5.0.12-1
- upstream version auto-updated to 5.0.12

* Sat May 12 2018 Danila Vershinin <info@getpagespeed.com> 5.0.11-1
- first release

