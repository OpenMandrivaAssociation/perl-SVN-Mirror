%define	module	SVN-Mirror

%if %{_use_internal_dependency_generator}
%define __noautoreq 'perl\\(VCP(.*)\\)'
%else
%define _requires_exceptions 'perl(VCP.*'
%endif

Name:		perl-%{module}
Version:	0.75
Release:	4
License:	GPL or Artistic
Group:		Development/Perl
Summary:	Perl modules to mirror remote subversion repositories to local ones
Source0:	http://search.cpan.org/CPAN/authors/id/C/CL/CLKAO/%{module}-%{version}.tar.bz2
Url:		http://search.cpan.org/dist/%{module}/

BuildRequires:	perl-devel
BuildRequires:	perl-SVN
BuildRequires:	perl-SVN-Simple
BuildRequires:	perl(Date::Format)
BuildRequires:	perl(File::chdir)
BuildRequires:	perl(URI)
BuildRequires:	perl(Class::Accessor)
BuildRequires:	perl(YAML)
#BuildRequires:	perl(SVK)
# for test 
BuildRequires:	subversion 
BuildRequires:	subversion-tools
BuildConflicts:	perl-VCP-Dest-svk

BuildArch:	noarch

#Requires:	perl(SVK)
Requires:	perl(Class::Accessor)
Requires:	perl(Data::UUID)
Requires:	perl(Term::ReadKey)


%description
SVN::Mirror allows you to mirror a remote repository to your local subversion
repository. It supports remote subversion and Git repositories.

%package -n	svm
Summary:	A tool to mirror a remote subversion repository
Group:		Development/Perl

%description -n	svm
svm (subversion mirror) is a command-line tool that allows you to mirror a
remote subversion repository on a local repository.

%prep
%setup -q -n %{module}-%{version}

%build
PERL_EXTUTILS_AUTOINSTALL=--skipdeps perl Makefile.PL INSTALLDIRS=vendor
%make

cat > README.Mdv << EOF
This version was not built with VCP support (for CVS and Perforce mirroring)
since it requires to package too much other perl modules.
EOF

%check
# Some fail with new subversion
#LC_ALL=C make test

%install
%makeinstall_std

%files
%doc CHANGES README README.Mdv TODO
%{perl_vendorlib}/SVN
%{_mandir}/man3/*

%files -n svm
%doc README.Mdv
%{_bindir}/*
%{_mandir}/man1/*


%changelog
* Sat Oct 11 2008 Guillaume Rousse <guillomovitch@mandriva.org> 0.75-1mdv2009.1
+ Revision: 292349
- update to new version 0.75

* Fri Aug 08 2008 Thierry Vignaud <tvignaud@mandriva.com> 0.74-2mdv2009.0
+ Revision: 268719
- rebuild early 2009.0 package (before pixel changes)

* Mon Jun 02 2008 Guillaume Rousse <guillomovitch@mandriva.org> 0.74-1mdv2009.0
+ Revision: 214419
- update to new version 0.74

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tvignaud@mandriva.com>
    - kill re-definition of %%buildroot on Pixel's request

* Mon Aug 20 2007 Thierry Vignaud <tvignaud@mandriva.com> 0.73-2mdv2008.0
+ Revision: 67568
- rebuild

* Wed May 02 2007 Olivier Thauvin <nanardon@mandriva.org> 0.73-1mdv2008.0
+ Revision: 20338
- 0.73


* Fri Dec 15 2006 Guillaume Rousse <guillomovitch@mandriva.org> 0.72-1mdv2007.0
+ Revision: 97356
- new version

* Fri Nov 03 2006 Michael Scherer <misc@mandriva.org> 0.71-1mdv2007.1
+ Revision: 76148
- version 0.71

* Sun Sep 03 2006 Olivier Thauvin <nanardon@mandriva.org> 0.70-1mdv2007.0
+ Revision: 59642
- 0.70

* Tue Aug 08 2006 Olivier Thauvin <nanardon@mandriva.org> 0.68-4mdv2007.0
+ Revision: 54065
- rebuild
- Import perl-SVN-Mirror

* Tue Jan 03 2006 Rafael Garcia-Suarez <rgarciasuarez@mandriva.com> 0.68-3mdk
- Add missing requires according to the Makefile.PL

* Wed Dec 28 2005 Guillaume Rousse <guillomovitch@mandriva.org> 0.68-2mdk
- spe cleanup
- fix directory ownership

* Tue Dec 13 2005 Rafael Garcia-Suarez <rgarciasuarez@mandriva.com> 0.68-1mdk
- 0.68

* Fri Oct 07 2005 Rafael Garcia-Suarez <rgarciasuarez@mandriva.com> 0.67-1mdk
- 0.67
- Fix BuildRequires due to subversion packages reorganisation

* Sat Aug 20 2005 Rafael Garcia-Suarez <rgarciasuarez@mandriva.com> 0.66-1mdk
- 0.66

* Wed Aug 17 2005 Rafael Garcia-Suarez <rgarciasuarez@mandriva.com> 0.65-1mdk
- 0.65

* Sat Jul 16 2005 Rafael Garcia-Suarez <rgarciasuarez@mandriva.com> 0.64-1mdk
- 0.64

* Thu Jun 30 2005 Rafael Garcia-Suarez <rgarciasuarez@mandriva.com> 0.63-1mdk
- 0.63

* Fri Jun 24 2005 Rafael Garcia-Suarez <rgarciasuarez@mandriva.com> 0.62-1mdk
- 0.62
- Rename README.Mdk to README.Mdv, add info in it.
- Improve description
- Require perl-SVK manually (for SVK::Util)

* Tue May 10 2005 Rafael Garcia-Suarez <rgarciasuarez@mandriva.com> 0.61-1mdk
- 0.61

* Tue May 03 2005 Rafael Garcia-Suarez <rgarciasuarez@mandriva.com> 0.60-1mdk
- 0.60

* Sat Apr 23 2005 Rafael Garcia-Suarez <rgarciasuarez@mandriva.com> 0.58-1mdk
- 0.58

* Wed Mar 30 2005 Rafael Garcia-Suarez <rgarciasuarez@mandrakesoft.com> 0.57-1mdk
- 0.57

* Tue Mar 01 2005 Michael Scherer <misc@mandrake.org> 0.56-1mdk
- New release 0.56
- complete buildRequires

* Thu Feb 03 2005 Michael Scherer <misc@mandrake.org> 0.55-1mdk
- New release 0.55

* Tue Dec 21 2004 Rafael Garcia-Suarez <rgarciasuarez@mandrakesoft.com> 0.51-1mdk
- New release 0.51
- Update summaries and descriptions

* Fri Nov 12 2004 Michael Scherer <misc@mandrake.org> 0.50-1mdk
- New release 0.50

* Thu Oct 21 2004 Michael Scherer <misc@mandrake.org> 0.49-1mdk
- New release 0.49
- BuildRequires

* Wed Oct 06 2004 Michael Scherer <misc@mandrake.org> 0.48-1mdk
- New release 0.48

* Sat Sep 25 2004 Michael Scherer <misc@mandrake.org> 0.47-1mdk
- New release 0.47

* Sun Sep 12 2004 Michael Scherer <misc@mandrake.org> 0.44-1mdk
- New release 0.44

* Tue Aug 24 2004 Michael Scherer <misc@mandrake.org> 0.43-1mdk
- New release 0.43

* Wed Aug 18 2004 Michael Scherer <misc@mandrake.org> 0.42-1mdk
- New release 0.42

* Fri Aug 06 2004 Michael Scherer <misc@mandrake.org> 0.40-1mdk
- New release 0.40

* Sun Jul 18 2004 Per Øyvind Karlsen <peroyvind@linux-mandrake.com> 0.38-1mdk
- 0.38

* Thu Jul 01 2004 Michael Scherer <misc@mandrake.org> 0.37-1mdk
- New release 0.37

* Sun Jun 13 2004 Michael Scherer <misc@mandrake.org> 0.36-3mdk
- BuildRequires once again

* Sun Jun 06 2004 Michael Scherer <misc@mandrake.org> 0.36-2mdk 
- BuildRequires
- reenable test

* Fri Jun 04 2004 Per Øyvind Karlsen <peroyvind@linux-mandrake.com> 0.36-1mdk
- 0.36
- skip test for now

* Thu Apr 29 2004 Michael Scherer <misc@mandrake.org> 0.35-1mdk
- New release 0.35

* Sat Apr 03 2004 Michael Scherer <misc@mandrake.org> 0.31-1mdk 
- First MandrakeSoft Package

