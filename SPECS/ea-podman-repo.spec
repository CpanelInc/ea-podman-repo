Name:           ea-podman-repo
Version:        1.0
# Doing release_prefix this way for Release allows for OBS-proof versioning, See EA-4552 for more details
%define release_prefix 1
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
echo "If your current transaction fails you may need to re-run now that it is configured"
%if 0%{?rhel} == 0
echo "Before you do that please run `apt update`" 
%endif

%pre
%include %{SOURCE0}

%changelog
* Thu Jan 20 2022 Daniel Muey <dan@cpanel.net> - 1.0-1
- ZC-9651: Initial version
