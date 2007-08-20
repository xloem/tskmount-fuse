%define name     tskmount-fuse
%define version  0.03
%define release  %mkrel 1

Summary: TSKmount-Fuse filesystem to recover deleted files
Name:    %{name}
Version: %{version}
Release: %{release}
License: GPL
Group:   File tools
URL:     http://tskmount-fuse.sourceforge.net/
Source:  http://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.gz
Packager:  Jean Diraison <jean.diraison@ac-versailles.fr>
Requires:  perl-Fuse, sleuthkit
BuildRoot: %{_tmppath}/%{name}-%{version}-root

%description
TSKmount is a Fuse filesystem written in perl and based on The Sleuth Kit
tools. It is intended to provide an easy way to recover deleted files over
ext2, fat and ntfs filesystems.

TSKmount runs on Linux, BSD and other Unix systems, see requirements for
details.

TSKmount-Fuse is a free software; you can freely use, modify and redistribute
it under the terms of GNU GPL version 2 license.

%prep
%setup -q

%build
make

%install
rm -rf ${RPM_BUILD_ROOT}
make install DESTDIR=${RPM_BUILD_ROOT} BINDIR=%{_bindir} MANDIR=%{_mandir}

%clean
rm -rf ${RPM_BUILD_ROOT}

%files
%defattr(-,root,root)
%doc COPYING README ChangeLog docs/html/tskmount.8.html
%{_bindir}/tskmount
%{_mandir}/man8/tskmount.8*

%changelog
* Mon Aug 20 2007 Jean Diraison <jean.diraison@ac-versailles.fr>
- add debian package creation capacity
- release 0.03

* Sun Aug 19 2007 Jean Diraison <jean.diraison@ac-versailles.fr>
- add enhance option to improve deleted files search
- add option to pass arguments to Fuse
- improve inodes management
- add some documentation (man, html, smgl)
- release 0.02

* Mon Aug 13 2007 Jean Diraison <jean.diraison@ac-versailles.fr>
- first release 0.01

