Name: nornet-nn
Version: 0.1.0
Release: 1
Summary: NorNet Node and Slice Tools
Group: Applications/Internet
License: GPLv3

AutoReqProv: on
BuildArch: noarch
BuildRoot: %{_tmppath}/%{name}-%{version}-build
BuildRequires: python
Requires: python

%description
NorNet Node and Slice Tools contain some tools for NorNet LXC-based research nodes, to be used by nodes and slices.

%prep 
%setup -q
%patch -p1

%build 
%configure 
%make

%install
[ "$RPM_BUILD_ROOT" -a "$RPM_BUILD_ROOT" != / ] && rm -rf "$RPM_BUILD_ROOT"
mkdir -p "$RPM_BUILD_ROOT"/usr/bin
mkdir -p "$RPM_BUILD_ROOT"/usr/share/man/man1/
cp System-Info "$RPM_BUILD_ROOT"/usr/bin
cp System-Info.1 "$RPM_BUILD_ROOT"/usr/share/man/man1/

%clean
[ "$RPM_BUILD_ROOT" -a "$RPM_BUILD_ROOT" != / ] && rm -rf "$RPM_BUILD_ROOT"

%files
%{_bindir}/System-Info
%{_mandir}/man1/SystemInfo.1.gz

%doc

%changelog
* Thu Apr 10 2014 Thomas Dreibholz <dreibh@iem.uni-due.de> - 0.1.0
- Created RPM package.
