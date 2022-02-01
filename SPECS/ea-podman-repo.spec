Name:           ea-podman-repo
Version:        1.0
# Doing release_prefix this way for Release allows for OBS-proof versioning, See EA-4552 for more details
%define release_prefix 2
Release:        %{release_prefix}%{?dist}.cpanel
Summary:        Ensure podman is available to the system
License:        GPL
Group:          System Environment/Libraries
URL:            http://www.cpanel.net
Vendor:         cPanel, Inc.
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-buildroot
AutoReqProv:    no

Source0:        pkg.preinst

%description
Installs pkg repository necessary for some OSs to have a proper podman.

%build
echo "Nothing to build"

%install
mkdir -p %{buildroot}/opt/cpanel/ea-podman-repo
install %{SOURCE0} %{buildroot}/opt/cpanel/ea-podman-repo/initrepo.sh

echo "If your current transaction fails you may need to re-run now that it is configured"
%if 0%{?rhel} == 0
echo 'Before you do that please run `apt update`'
%endif

%pre
%include %{SOURCE0}

%files
%attr(755,root,root) /opt/cpanel/ea-podman-repo/initrepo.sh

%changelog
* Tue Feb 01 2022 Dan Muey <dan@cpanel.net> - 1.0-2
- ZC-9689: Add README.md and remove no-longer-relevant comment

* Thu Jan 20 2022 Daniel Muey <dan@cpanel.net> - 1.0-1
- ZC-9651: Initial version
