#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	URI
%define	pnam	Find
Summary:	URI::Find - Find URIs in arbitrary text
#Summary(pl.UTF-8):	
Name:		perl-URI-Find
Version:	0.16
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-authors/id/R/RO/ROSCH/URI-Find-0.16.tar.gz
# Source0-md5:	339279e268cf37e629f54c1091f99a13
URL:		http://search.cpan.org/dist/URI-Find/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-URI >= 1.00
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module does one thing: Finds URIs and URLs in plain text.  It finds
them quickly and it finds them all (or what URI::URL considers a URI
to be.)  It only finds URIs which include a scheme (http:// or the
like), for something a bit less strict have a look at
URI::Find::Schemeless.

# %description -l pl.UTF-8
# TODO

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
%doc Changes README TODO
%{perl_vendorlib}/URI/*.pm
%{perl_vendorlib}/URI/Find
%{_mandir}/man3/*
