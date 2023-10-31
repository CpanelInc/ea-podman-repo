#!/bin/bash

# This is not in ea-podman because deb dependencies happen before preinst and universal hooks.

if [ -f /etc/os-release ]; then
    source /etc/os-release

    if [ "$ID" == "rocky" ] && [ "${VERSION_ID:0:1}" == "8" ]; then
        echo "Rocky Linux 8 needs powertools enabled in order to do podman, ensuring it is enabled …"

        set -x
        dnf config-manager --set-enabled powertools
        set +x
    fi

    if [ "$ID" == "almalinux" ] && [ "${VERSION_ID:0:1}" == "8" ]; then
        echo "AlmaLinux 8 needs powertools enabled in order to do podman, ensuring it is enabled …"

        set -x
        dnf config-manager --set-enabled powertools
        set +x
    fi

    if [ "$ID" == "almalinux" ] && [ "${VERSION_ID:0:1}" == "9" ]; then
        echo "AlmaLinux 9 needs crb enabled in order to do libnsl2-devel for ea-podman, ensuring it is enabled …"

        set -x
        dnf config-manager --set-enabled crb
        set +x
    fi

    if [ "$ID" == "centos" ] && [ "$VERSION_ID" == "7" ] && [ ! -s /etc/yum.repos.d/devel:kubic:libcontainers:stable.repo ]; then
        echo "CentOS 7 needs a specific repo to make a newer podman available, attempting to install …"

        set -x
        curl -s http://download.opensuse.org/repositories/devel:/kubic:/libcontainers:/stable/CentOS_7/devel:kubic:libcontainers:stable.repo -o /etc/yum.repos.d/devel:kubic:libcontainers:stable.repo
        set +x
    fi

    if [ "$ID" == "ubuntu" ] && [ "$VERSION_ID" == "20.04" ] && [ ! -s /etc/apt/sources.list.d/devel:kubic:libcontainers:stable.list ]; then
        echo "Ubuntu 20.04 needs a specific source to make podman available, attempting to install …"
        export APT_KEY_DONT_WARN_ON_DANGEROUS_USAGE="There is currently no other way to make this happen so we want to silence the warning."

        set -x
        echo "deb http://download.opensuse.org/repositories/devel:/kubic:/libcontainers:/stable/xUbuntu_$VERSION_ID/ ./" > /etc/apt/sources.list.d/devel:kubic:libcontainers:stable.list
        wget -nv https://download.opensuse.org/repositories/devel:kubic:libcontainers:stable/xUbuntu_$VERSION_ID/Release.key -O- | apt-key add -
        set +x

        echo 'Please run this command to have it take effect: `apt update`'
    fi

    if [ "$ID" == "ubuntu" ] && [ "$VERSION_ID" == "22.04" ] && [ ! -s /etc/apt/sources.list.d/devel:kubic:libcontainers:unstable.list ]; then
        echo "Ubuntu $VERSION_ID needs a specific source to make podman available, attempting to install …"
        export APT_KEY_DONT_WARN_ON_DANGEROUS_USAGE="There is currently no other way to make this happen so we want to silence the warning."

        set -x

        key_url="https://download.opensuse.org/repositories/devel:/kubic:/libcontainers:/unstable/xUbuntu_${VERSION_ID}/Release.key"
        sources_url="https://download.opensuse.org/repositories/devel:/kubic:/libcontainers:/unstable/xUbuntu_${VERSION_ID}"

        echo "deb $sources_url/ ./" > /etc/apt/sources.list.d/devel:kubic:libcontainers:unstable.list
        curl -fsSL $key_url | gpg --dearmor | tee /etc/apt/trusted.gpg.d/devel_kubic_libcontainers_unstable.gpg > /dev/null

        set +x

        echo 'Please run this command to have it take effect: `apt update`'
    fi
fi
