%define version	0.03
%define release	%mkrel 6
%define module	Video-Frequencies

Name:		perl-%{module}
Summary:	Perl interface to the Video4linux tuner frequencies
Group:		Development/Perl
Version:	%{version}
Release:       	%{release}
License:	GPL or Artistic
URL:		http://ivtvdriver.org/
Source0:	http://dl.ivtvdriver.org/supporting-tools/%{module}-%{version}.tar.bz2
BuildRoot:	%{_tmppath}/%{name}-root
BuildArch:	noarch
#Requires: perl, perl-base
BuildRequires:	perl-devel

%description
This package provides a table of hashes that represent all the current
frequency mappings that are used by Video4Linux programs.

Do perldoc Video::Frequencies to get complete instructions, etc.

%prep
%setup -q -n %{module}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%{__make}
make test

%install
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}
%{makeinstall_std}

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%doc README COPYING Changes
%{perl_vendorlib}/Video/Frequencies.pm
%{_mandir}/man3/Video::Frequencies.3pm*


