Name:           ea-podman-repo
Version:        1.0
# Doing release_prefix this way for Release allows for OBS-proof versioning, See EA-4552 for more details
%define release_prefix 7
Release:        %{release_prefix}%{?dist}.cpanel
Summary:        Ensure podman is available to the system
License:        GPL
Group:          System Environment/Libraries
URL:            http://www.cpanel.net
Vendor:         cPanel, Inc.
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-buildroot
AutoReqProv:    no

Source0:        pkg.preinst
Source1:        initrepo.sh

%description
Installs pkg repository necessary for some OSs to have a proper podman.

%build
echo "Nothing to build"

%install
mkdir -p %{buildroot}/opt/cpanel/ea-podman-repo
install %{SOURCE1} %{buildroot}/opt/cpanel/ea-podman-repo/initrepo.sh

echo "If your current transaction fails you may need to re-run now that it is configured"
%if 0%{?rhel} == 0
echo 'Before you do that please run `apt update`'
%endif

%pre
%include %{SOURCE0}

%files
%attr(755,root,root) /opt/cpanel/ea-podman-repo/initrepo.sh

%changelog
* Tue Mar 05 2024 Dan Muey <dan@cpanel.net> - 1.0-7
- ZC-11673: Add Cloudlinux support

* Thu Oct 26 2023 Julian Brown <julian.brown@cpanel.net> - 1.0-6
- ZC-11296: Add new podman repo for U22

* Tue Oct 04 2022 Dan Muey <dan@cpanel.net> - 1.0-5
- ZC-10348: Updates for Alma 9 support

* Tue Jun 07 2022 Dan Muey <dan@cpanel.net> - 1.0-4
- ZC-10010: enable powertools on Rocky 8

* Tue Feb 08 2022 Dan Muey <dan@cpanel.net> - 1.0-3
- ZC-9729: enable powertools on Alma 8

* Tue Feb 01 2022 Dan Muey <dan@cpanel.net> - 1.0-2
- ZC-9689: Add README.md and remove no-longer-relevant comment

* Thu Jan 20 2022 Daniel Muey <dan@cpanel.net> - 1.0-1
- ZC-9651: Initial version
