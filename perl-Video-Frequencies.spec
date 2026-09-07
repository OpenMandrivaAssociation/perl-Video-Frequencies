%define upstream_version 0.902
%define module	Video-Frequencies

Name:		perl-%{module}
Summary:	Perl interface to the Video4linux tuner frequencies
Group:		Development/Perl
Version:	0.902
Release:	3
License:	GPL or Artistic
URL:		https://ivtvdriver.org/
Source0:	https://cpan.metacpan.org/authors/id/M/ML/MLEHMANN/Video-Capture-V4l-0.902.tar.gz
BuildArch:	noarch
#Requires: perl, perl-base
BuildRequires:	make
BuildRequires:	perl-devel

%description
This package provides a table of hashes that represent all the current
frequency mappings that are used by Video4Linux programs.

Do perldoc Video::Frequencies to get complete instructions, etc.

%prep
%setup -q -n Video-Capture-V4l-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%{__make}
make test || :

%install
%{makeinstall_std}

find %{buildroot} -type f -name '*.pm' -exec chmod -x {} +
if [ -d %{buildroot}%{_bindir} ]; then find %{buildroot}%{_bindir} -type f -exec chmod 755 {} +; fi
%files
%doc README COPYING Changes
%{perl_vendorlib}/Video/Frequencies.pm
%{_mandir}/man3/Video::Frequencies.3pm*




