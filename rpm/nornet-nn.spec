Name:          nornet-nn
Version:       0.4.4
Release:       1
Summary:       NorNet Node and Slice Tools
Group:         Applications/Internet
License:       GPLv3
Source:        %{name}-%{version}.tar.gz

AutoReqProv:   on
BuildArch:     noarch
BuildRoot:     %{_tmppath}/%{name}-%{version}-build

%description
NorNet Node and Slice Tools contain some tools for NorNet LXC-based research nodes, to be used by nodes and slices.

%prep 
%setup -q

%build 

#%configure 
#true

%install
[ "$RPM_BUILD_ROOT" -a "$RPM_BUILD_ROOT" != / ] && rm -rf "$RPM_BUILD_ROOT"
mkdir -p "$RPM_BUILD_ROOT"/usr/bin/
mkdir -p "$RPM_BUILD_ROOT"/etc/profile.d/
mkdir -p "$RPM_BUILD_ROOT"/usr/share/man/man1/
mkdir -p "$RPM_BUILD_ROOT"/usr/lib/systemd/system/
cp src/systeminfo.sh src/systeminfo.csh "$RPM_BUILD_ROOT"/etc/profile.d/
cp src/System-Info                      "$RPM_BUILD_ROOT"/usr/bin/
cp src/System-Info.1                    "$RPM_BUILD_ROOT"/usr/share/man/man1/
cp src/nornet-research-node-initializer "$RPM_BUILD_ROOT"/usr/bin/
cp src/nornet-research-node.service     "$RPM_BUILD_ROOT"/usr/lib/systemd/system/

%post
systemctl enable nornet-research-node.service
systemctl restart nornet-research-node.service

%prerun
if [ $1 -eq 0 ] ; then
   systemctl disable nornet-research-node.service
fi

%clean
[ "$RPM_BUILD_ROOT" -a "$RPM_BUILD_ROOT" != / ] && rm -rf "$RPM_BUILD_ROOT"

%files
%{_bindir}/System-Info
%{_bindir}/nornet-research-node-initializer
/usr/lib/systemd/system/nornet-research-node.service
/etc/profile.d/systeminfo.sh
/etc/profile.d/systeminfo.csh
%{_mandir}/man1/System-Info.1.gz

%doc

%changelog
* Thu Apr 10 2014 Thomas Dreibholz <dreibh@iem.uni-due.de> - 0.1.0
- Created RPM package.
