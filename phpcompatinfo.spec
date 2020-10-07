# License: MIT
# http://opensource.org/licenses/MIT

Name: phpcompatinfo
Version: 5.4.1
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
* Wed Oct 07 2020 Danila Vershinin <info@getpagespeed.com> 5.4.1-1
- release 5.4.1

* Fri Oct 02 2020 Danila Vershinin <info@getpagespeed.com> 5.4.0-1
- release 5.4.0

* Thu Jul 09 2020 Danila Vershinin <info@getpagespeed.com> 5.3.0-1
- release 5.3.0

* Thu Apr 30 2020 Danila Vershinin <info@getpagespeed.com> 5.2.3-1
- release 5.2.3

* Thu Nov 07 2019 Danila Vershinin <info@getpagespeed.com> 5.2.1-1
- upstream version auto-updated to 5.2.1

* Sun Jun 02 2019 Danila Vershinin <info@getpagespeed.com> 5.2.0-1
- upstream version auto-updated to 5.2.0

* Fri Dec 07 2018 Danila Vershinin <info@getpagespeed.com> 5.1.0-1
- upstream version auto-updated to 5.1.0

* Sat May 12 2018 Danila Vershinin <info@getpagespeed.com> 5.0.12-1
- upstream version auto-updated to 5.0.12

* Sat May 12 2018 Danila Vershinin <info@getpagespeed.com> 5.0.11-1
- first release

