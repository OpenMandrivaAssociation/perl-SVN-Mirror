%define	module	SVN-Mirror
%define	name	perl-%{module}
%define version 0.73
%define release %mkrel 1
%define _requires_exceptions 'perl(VCP.*'

Name:		%{name}
Version:	%{version}
Release:	%{release}
License:	GPL or Artistic
Group:		Development/Perl
Summary:	Perl modules to mirror remote subversion repositories to local ones
Source0:	http://search.cpan.org/CPAN/authors/id/C/CL/CLKAO/%{module}-%{version}.tar.bz2
Url:		http://search.cpan.org/dist/%{module}/
%if %{mdkversion} < 1010
BuildRequires:	perl-devel
%endif
Requires:	perl-SVK
Requires:	perl(Class::Accessor)
Requires:	perl(Data::UUID)
Requires:	perl(Term::ReadKey)
BuildRequires:	perl-SVN
BuildRequires:	perl-URI
BuildRequires:	perl-Class-Accessor
BuildRequires:	perl-SVN-Simple
BuildRequires:	perl-YAML
BuildRequires:	perl-SVK
# for test 
BuildRequires:  subversion 
BuildRequires:  subversion-tools
BuildConflicts:	perl-VCP-Dest-svk
BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}


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
PERL_EXTUTILS_AUTOINSTALL=--skipdeps %{__perl} Makefile.PL INSTALLDIRS=vendor
%make

cat > README.Mdv << EOF
This version was not built with VCP support (for CVS and Perforce mirroring)
since it requires to package too much other perl modules.
EOF

%check
LC_ALL=C %{__make} test

%install
rm -rf %{buildroot}
%{makeinstall_std}

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc CHANGES README README.Mdv TODO
%{perl_vendorlib}/SVN
%{_mandir}/man3/*

%files -n svm
%defattr(-,root,root)
%doc README.Mdv
%{_bindir}/*
%{_mandir}/man1/*


