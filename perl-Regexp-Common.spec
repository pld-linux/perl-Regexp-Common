#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%define		pdir	Regexp
%define		pnam	Common
Summary:	Regexp::Common Perl module - commonly requested regular expressions
Summary(pl.UTF-8):	Moduł Perla Regexp::Common - często używane wyrażenia regularne
Name:		perl-Regexp-Common
Version:	2017060201
Release:	1
License:	Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Regexp/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	b1bb40759b84154990f36a160160fb94
URL:		http://search.cpan.org/dist/Regexp-Common/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	rpmbuild(macros) >= 1.663
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

# not recognized for unknown reason
%define		_noautoreq_perl	Regexp::Common::URI

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
%{perl_vendorlib}/Regexp/Common.pm
%{perl_vendorlib}/Regexp/Common
%{_mandir}/man3/Regexp::Common*.3pm*
