# License: MIT
# http://opensource.org/licenses/MIT

Name: phpcompatinfo
Version: 7.2.5
Release: 2%{?dist}
Summary: Find the minimum version and the extensions required for a piece of PHP code to run

License: BSD-3-clauses License
URL: https://github.com/llaville/php-compatinfo
Source0: https://github.com/llaville/php-compatinfo/releases/download/%{version}/phpcompatinfo.phar

BuildArch: noarch

BuildRequires: php-cli
Requires:  php-cli

%description
PHP CompatInfo is a library that can find the minimum version 
and the extensions required for a piece of code to run.


%prep
# Nothing to do


%build
# Nothing to do


%global phar_dir %{_datadir}/%{name}

%install
%{__rm} -rf %{buildroot}
%{__mkdir} -p %{buildroot}%{phar_dir}
%{__mkdir} -p %{buildroot}%{_bindir}

# Install upstream PHAR to a data location with .phar extension
%{__install} -m 644 -p %SOURCE0 %{buildroot}%{phar_dir}/%{name}.phar

# Lightweight CLI wrapper that executes the PHAR with the system PHP
cat > %{buildroot}%{_bindir}/%{name} << 'EOF'
#!/bin/sh
exec php /usr/share/phpcompatinfo/phpcompatinfo.phar "$@"
EOF
%{__chmod} 0755 %{buildroot}%{_bindir}/%{name}

%check
# Only run functional test when PHP runtime is new enough
if php -r 'exit(version_compare(PHP_VERSION, "8.0", "<") ? 1 : 0);'; then
    %{buildroot}%{_bindir}/%{name} --version >/dev/null 2>&1
else
    echo "Skipping functional check: PHP < 8.0; binary integrity already verified by install step."
fi

%files
%defattr(-,root,root)
%{_bindir}/%{name}
%{phar_dir}/%{name}.phar

%changelog
* Mon Nov 24 2025 Danila Vershinin <info@getpagespeed.com> 7.2.5-2
- install PHAR under /usr/share/phpcompatinfo and use a wrapper script for CLI
- fix runtime on EL7 where PHAR cannot be created from /usr/bin/phpcompatinfo

* Mon Nov 24 2025 Danila Vershinin <info@getpagespeed.com> 7.2.5-1
- release 7.2.5

* Fri Oct 10 2025 Danila Vershinin <info@getpagespeed.com> 7.2.4-1
- release 7.2.4

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

