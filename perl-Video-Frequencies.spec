%define upstream_version	0.03
%define module	Video-Frequencies

Name:		perl-%{module}
Summary:	Perl interface to the Video4linux tuner frequencies
Group:		Development/Perl
Version:	%perl_convert_version %{upstream_version}
Release:       	14
License:	GPL or Artistic
URL:		https://ivtvdriver.org/
Source0:	http://dl.ivtvdriver.org/supporting-tools/Video-Frequencies-%{upstream_version}.tar.gz
BuildArch:	noarch
#Requires: perl, perl-base
BuildRequires:	perl-devel

%description
This package provides a table of hashes that represent all the current
frequency mappings that are used by Video4Linux programs.

Do perldoc Video::Frequencies to get complete instructions, etc.

%prep
%setup -q -n %{module}-%{upstream_version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%{__make}
make test

%install
%{makeinstall_std}

%files
%doc README COPYING Changes
%{perl_vendorlib}/Video/Frequencies.pm
%{_mandir}/man3/Video::Frequencies.3pm*




%changelog
* Mon Sep 14 2009 Thierry Vignaud <tvignaud@mandriva.com> 0.03-11mdv2010.0
+ Revision: 440722
- rebuild

* Fri Mar 06 2009 Antoine Ginies <aginies@mandriva.com> 0.03-10mdv2009.1
+ Revision: 350221
- 2009.1 rebuild

* Thu Jul 31 2008 Thierry Vignaud <tvignaud@mandriva.com> 0.03-9mdv2009.0
+ Revision: 258756
- rebuild

* Thu Jul 24 2008 Thierry Vignaud <tvignaud@mandriva.com> 0.03-8mdv2009.0
+ Revision: 246692
- rebuild

* Fri Dec 21 2007 Olivier Blin <oblin@mandriva.com> 0.03-6mdv2008.1
+ Revision: 136364
- restore BuildRoot

  + Thierry Vignaud <tvignaud@mandriva.com>
    - kill re-definition of %%buildroot on Pixel's request


* Wed Jan 03 2007 Stefan van der Eijk <stefan@mandriva.org> 0.03-6mdv2007.0
+ Revision: 103828
- Import perl-Video-Frequencies

* Sun Feb 05 2006 Stefan van der Eijk <stefan@eijk.nu> 0.03-6mdk
- fix URLs

* Fri Jun 03 2005 Stefan van der Eijk <stefan@eijk.nu> 0.03-5mdk
- yearly rebuild
- rpmlint fixes
- %%mkrel

* Fri Jun 25 2004 Stefan van der Eijk <stefan@mandrake.org> 0.03-4mdk
- initial Mandrake package


