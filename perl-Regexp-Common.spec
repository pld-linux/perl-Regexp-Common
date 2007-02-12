#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Regexp
%define		pnam	Common
Summary:	Regexp::Common Perl module - commonly requested regular expressions
Summary(pl.UTF-8):   Moduł Perla Regexp::Common - często używane wyrażenia regularne
Name:		perl-Regexp-Common
Version:	2.120
Release:	1
License:	Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	a14f2a3c3f2718a567ec26f57a2bae13
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

# not recognized for unknown reason
%define		_noautoreq	'perl(Regexp::Common::URI)'

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

%description -l pl.UTF-8
Ten pakiet zawiera moduł Regexp::Common, który zawiera lub generuje
często potrzebne wyrażenia regularne. Aktualnie zawiera wzorce dla:
 * zrównoważonych nawiasów
 * ograniczonego tekstu (z cytowaniem)
 * liczb całkowitych i zmiennoprzecinkowych o dowolnej podstawie (do 36)
 * komentarzy w C, C++, Perlu i shellu
 * słów obraźliwych (w języku angielskim)
 * list o dowolnym wzorcu
 * adresów IPv4.
 * URI

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%{__perl} -pi -e 's/^(use 5.004)(73;)(.*)$/$1_$2$3/' lib/Regexp/Common.pm

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README TODO
%{perl_vendorlib}/Regexp/*.pm
%{perl_vendorlib}/Regexp/Common
%{_mandir}/man3/*
