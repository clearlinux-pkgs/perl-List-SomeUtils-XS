#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-List-SomeUtils-XS
Version  : 0.58
Release  : 19
URL      : https://www.cpan.org/authors/id/D/DR/DROLSKY/List-SomeUtils-XS-0.58.tar.gz
Source0  : https://www.cpan.org/authors/id/D/DR/DROLSKY/List-SomeUtils-XS-0.58.tar.gz
Summary  : 'XS implementation for List::SomeUtils'
Group    : Development/Tools
License  : Artistic-2.0
Requires: perl-List-SomeUtils-XS-lib = %{version}-%{release}
Requires: perl-List-SomeUtils-XS-license = %{version}-%{release}
BuildRequires : buildreq-cpan
BuildRequires : perl(Test::Warnings)

%description
# NAME
List::SomeUtils::XS - XS implementation for List::SomeUtils
# VERSION
version 0.58

%package dev
Summary: dev components for the perl-List-SomeUtils-XS package.
Group: Development
Requires: perl-List-SomeUtils-XS-lib = %{version}-%{release}
Provides: perl-List-SomeUtils-XS-devel = %{version}-%{release}

%description dev
dev components for the perl-List-SomeUtils-XS package.


%package lib
Summary: lib components for the perl-List-SomeUtils-XS package.
Group: Libraries
Requires: perl-List-SomeUtils-XS-license = %{version}-%{release}

%description lib
lib components for the perl-List-SomeUtils-XS package.


%package license
Summary: license components for the perl-List-SomeUtils-XS package.
Group: Default

%description license
license components for the perl-List-SomeUtils-XS package.


%prep
%setup -q -n List-SomeUtils-XS-0.58

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/perl-List-SomeUtils-XS
cp LICENSE %{buildroot}/usr/share/package-licenses/perl-List-SomeUtils-XS/LICENSE
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)
/usr/lib/perl5/vendor_perl/5.28.1/x86_64-linux-thread-multi/List/SomeUtils/XS.pm

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/List::SomeUtils::XS.3

%files lib
%defattr(-,root,root,-)
/usr/lib/perl5/vendor_perl/5.28.1/x86_64-linux-thread-multi/auto/List/SomeUtils/XS/XS.so

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/perl-List-SomeUtils-XS/LICENSE
