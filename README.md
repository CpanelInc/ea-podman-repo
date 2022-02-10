# What is this package for?

It ensures that CentOS 7, AlmaLinux 8, and Ubuntu 20.04 have access to a `podman` that `ea-podman` requires.

It is not available on OSs that do not need it.

## I didn’t realize that and undid the configuration that it setup!

No problem, just run `/opt/cpanel/ea-podman-repo/initrepo.sh` and follow any instructions (No output means you’re already setup).

## First Time Caveat

`ea-podman` requires this package. Unless what this package does is already set up the first attempt at `ea-podman` will fail.

It may work the second time (unless a manual step like `apt update` was not done).

If all else fails:

1. install `ea-podman-repo` directly
2. run `/opt/cpanel/ea-podman-repo/initrepo.sh` and follow any instructions
   * No output means you’re already setup.
