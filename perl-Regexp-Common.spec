#
# Conditional build:
# _without_tests - do not perform "make test"
%include	/usr/lib/rpm/macros.perl
%define	pdir	Regexp
%define	pnam	Common
Summary:	Regexp::Common perl module - commonly requested regular expressions
Summary(pl):	Modu³ perla Regexp::Common - czêsto u¿ywane wyra¿enia regularne
Name:		perl-Regexp-Common
Version:	1.20
Release:	1
License:	Artistic
Group:		Development/Languages/Perl
Source0:	ftp://ftp.cpan.org/pub/CPAN/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	perl >= 5.6
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package contains Regexp::Common module that stores or generates
commonly needed regular expressions. Patterns currently provided
include:
 * balanced parentheses and brackets
 * delimited text (with escapes)
 * integers and floating-point numbers in any base (up to 36)
 * comments in C, C++, Perl, and shell
 * offensive language
 * lists of any pattern
 * IPv4 addresses
 * URIs

%description -l pl
Ten pakiet zawiera modu³ Regexp::Common, który zawiera lub generuje
czêsto potrzebne wyra¿enia regularne. Aktualnie zawiera wzorce dla:
 * zrównowa¿onych nawiasów
 * ograniczonego tekstu (z cytowaniem)
 * liczb ca³kowitych i zmiennoprzecinkowych o dowolnej podstawie (do 36)
 * komentarzy w C, C++, Perlu i shellu
 * s³ów obra¼liwych (w jêzyku angielskim)
 * list o dowolnym wzorcu
 * adresów IPv4.
 * URI
 
%prep
%setup -q -n %{pdir}-%{pnam}-%{version}
perl -pi -e 's/5\.00473/5.004_73/' lib/Regexp/Common.pm

%build
perl Makefile.PL
%{__make}
%{!?_without_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_sitelib}/%{pdir}/*.pm
%{perl_sitelib}/%{pdir}/%{pnam}
%{_mandir}/man3/*
