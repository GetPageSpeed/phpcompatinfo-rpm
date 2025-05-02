# License: MIT
# http://opensource.org/licenses/MIT

Name: phpcompatinfo
Version: 7.2.3
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
* Fri May 02 2025 Danila Vershinin <info@getpagespeed.com> 7.2.3-1
- release 7.2.3

* Thu Apr 25 2024 Danila Vershinin <info@getpagespeed.com> 7.1.4-1
- release 7.1.4

* Wed Mar 20 2024 Danila Vershinin <info@getpagespeed.com> 7.1.3-1
- release 7.1.3

* Fri Feb 09 2024 Danila Vershinin <info@getpagespeed.com> 7.1.2-1
- release 7.1.2

* Fri Jan 19 2024 Danila Vershinin <info@getpagespeed.com> 7.1.1-1
- release 7.1.1

* Tue Jan 02 2024 Danila Vershinin <info@getpagespeed.com> 7.1.0-1
- release 7.1.0

* Sun Dec 31 2023 Danila Vershinin <info@getpagespeed.com> 7.0.3-1
- release 7.0.3

* Thu Dec 07 2023 Danila Vershinin <info@getpagespeed.com> 7.0.2-1
- release 7.0.2

* Wed Nov 15 2023 Danila Vershinin <info@getpagespeed.com> 7.0.1-1
- release 7.0.1

* Sat May 13 2023 Danila Vershinin <info@getpagespeed.com> 7.0.0-1
- release 7.0.0

* Thu Dec 15 2022 Danila Vershinin <info@getpagespeed.com> 6.5.4-1
- release 6.5.4

* Sun Nov 06 2022 Danila Vershinin <info@getpagespeed.com> 6.5.3-1
- release 6.5.3

* Wed Oct 26 2022 Danila Vershinin <info@getpagespeed.com> 6.5.2-1
- release 6.5.2

* Tue Oct 25 2022 Danila Vershinin <info@getpagespeed.com> 6.5.1-1
- release 6.5.1

* Wed Sep 28 2022 Danila Vershinin <info@getpagespeed.com> 6.4.2-1
- release 6.4.2

* Fri Apr 08 2022 Danila Vershinin <info@getpagespeed.com> 6.4.1-1
- release 6.4.1

* Thu Apr 07 2022 Danila Vershinin <info@getpagespeed.com> 6.4.0-1
- release 6.4.0

* Mon Mar 07 2022 Danila Vershinin <info@getpagespeed.com> 6.3.0-1
- release 6.3.0

* Mon Feb 07 2022 Danila Vershinin <info@getpagespeed.com> 6.2.0-1
- release 6.2.0

* Sat Jan 29 2022 Danila Vershinin <info@getpagespeed.com> 6.1.2-1
- release 6.1.2

* Wed Jan 19 2022 Danila Vershinin <info@getpagespeed.com> 6.1.1-1
- release 6.1.1

* Fri Jan 07 2022 Danila Vershinin <info@getpagespeed.com> 6.1.0-1
- release 6.1.0

* Thu Jan 06 2022 Danila Vershinin <info@getpagespeed.com> 6.0.3-1
- release 6.0.3

* Tue Dec 28 2021 Danila Vershinin <info@getpagespeed.com> 6.0.2-1
- release 6.0.2

* Tue Dec 14 2021 Danila Vershinin <info@getpagespeed.com> 6.0.1-1
- release 6.0.1

* Sun Dec 12 2021 Danila Vershinin <info@getpagespeed.com> 6.0.0-1
- release 6.0.0

* Sat Dec 11 2021 Danila Vershinin <info@getpagespeed.com> 5.5.4-1
- release 5.5.4

* Tue May 04 2021 Danila Vershinin <info@getpagespeed.com> 5.5.3-1
- release 5.5.3

* Tue Apr 13 2021 Danila Vershinin <info@getpagespeed.com> 5.5.2-1
- release 5.5.2

* Sun Mar 14 2021 Danila Vershinin <info@getpagespeed.com> 5.5.1-1
- release 5.5.1

* Tue Feb 23 2021 Danila Vershinin <info@getpagespeed.com> 5.4.4-1
- release 5.4.4

* Sat Feb 13 2021 Danila Vershinin <info@getpagespeed.com> 5.4.3-1
- release 5.4.3

* Sat Nov 21 2020 Danila Vershinin <info@getpagespeed.com> 5.4.2-1
- release 5.4.2

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

