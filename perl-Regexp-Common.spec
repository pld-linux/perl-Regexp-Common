#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	Regexp
%define	pnam	Common
Summary:	Regexp::Common Perl module - commonly requested regular expressions
Summary(pl):	Modu³ Perla Regexp::Common - czêsto u¿ywane wyra¿enia regularne
Name:		perl-Regexp-Common
Version:	2.115
Release:	2
License:	Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	2cf0788ca410d863ebf6251f20aa0892
Patch0:		%{name}-test.patch
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
%patch0 -p1

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
