#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%define	pdir	URI
%define	pnam	Find
Summary:	URI::Find - Find URIs in arbitrary text
Summary(pl.UTF-8):	URI::Find - znajdowanie URI w dowolnym tekście
Name:		perl-URI-Find
Version:	20160806
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-authors/id/M/MS/MSCHWERN/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	744411a9fe3865f8f580b1b5fea8c7e5
URL:		http://search.cpan.org/dist/URI-Find/
BuildRequires:	perl-Module-Build >= 0.30
BuildRequires:	perl-devel >= 1:5.8.8
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	perl-URI >= 1.60
%if %{with tests}
BuildRequires:	perl-Test-Simple >= 0.88
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module does one thing: Finds URIs and URLs in plain text. It
finds them quickly and it finds them all (or what URI::URL considers a
URI to be.) It only finds URIs which include a scheme (http:// or the
like), for something a bit less strict have a look at
URI::Find::Schemeless.

%description -l pl.UTF-8
Ten moduł robi jedną rzecz: znajduje URI i URL-e w czystym tekście.
Znajduje je szybko i znajduje je wszystkie (lub cokolwiek co URI::URL
uzna za URI). Znajduje tylko URI zawierające schemat (http:// itp.),
natomiast coś mniej ścisłego można znaleźć w URI::Find::Schemeless.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%{__sed} -i -e '1s,#!.*/perl,#!%{__perl},' bin/urifind

%build
%{__perl} Build.PL \
	installdirs=vendor \
	destdir=$RPM_BUILD_ROOT
./Build

%{?with_tests:./Build test}

%install
rm -rf $RPM_BUILD_ROOT

./Build install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README TODO
%{perl_vendorlib}/URI/*.pm
%{perl_vendorlib}/URI/Find
%attr(755,root,root) %{_bindir}/urifind
%{_mandir}/man3/*
