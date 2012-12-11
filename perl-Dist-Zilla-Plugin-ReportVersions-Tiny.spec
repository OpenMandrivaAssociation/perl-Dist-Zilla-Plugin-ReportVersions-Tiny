%define upstream_name    Dist-Zilla-Plugin-ReportVersions-Tiny
%define upstream_version 1.02

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	3

Summary:	Reports dependency versions during testing
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Dist/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(Dist::Zilla)
BuildRequires:	perl(Dist::Zilla::File::FromCode)
BuildRequires:	perl(Dist::Zilla::Role::FileGatherer)
BuildRequires:	perl(Dist::Zilla::Role::TextTemplate)
BuildRequires:	perl(File::Find)
BuildRequires:	perl(File::Temp)
BuildRequires:	perl(Moose)
BuildRequires:	perl(Test::Differences)
BuildRequires:	perl(Test::Exception)
BuildRequires:	perl(Test::MockObject)
BuildRequires:	perl(Test::More)
BuildRequires:	perl(vars)
BuildArch:	noarch

%description
This module integrates with the Dist::Zilla manpage to automatically add an
additional test to your released software. Rather than testing features of
the software, this reports the versions of all static module dependencies,
and of Perl, at the time the tests are run.

The value of this is that when someone submits a test failure report you
can see which versions of the modules were installed and, hopefully, be
able to reproduce problems that are dependent on a specific set of module
versions.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std

%files
%doc META.yml META.json LICENSE README
%{_mandir}/man3/*
%{perl_vendorlib}/*

