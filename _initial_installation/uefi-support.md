---
layout: article
title: UEFI Support in AII
author: Michel Jouvin
menu: UEFI Support
redirect_from: /documentation/2017/02/27/uefi-support.html
---

# {{ page.title }}

Quattor 17.3 introduced UEFI support in AII. It is based on using the Grub2 EFI loader instead of PXELINUX/SYSLINUX. This page describes 
how to enable it, when you have an AII working configuration for legacy BIOS.


## Changes to AII Server Configuration

By default, AII server configuration requires no change to enable the UEFI support (the UEFI boot configuration files are produced in 
addition to the PXELINUX ones) but a few additional files must be installed on the TFTP server, in a directory called by default `grub-efi`, 
in the same location where your `pxelinux.cfg` directory is. The required files are:

* Grub2 EFI loader: see the section below
* `localboot.cfg` for Grub2 EFI: recommended file is provided by `aii-pxelinux` RPM and installed in `/usr/share/doc/aii-pxelinux-VERSION/eg` 
  (`localboot.cfg.grub2`).

Also the DHCP server configuration must be updated to recognize the UEFI vendor class and use the appropriate boot loader and configuration files. 
On an ISC DHCP server, this is typically done by adding in the `dhcpd` configuration (in the file dedicated to Quattor-managed machines for 
example) something like:

```
option space PXE;
option PXE.mtftp-ip    code 1 = ip-address;
option PXE.mtftp-cport code 2 = unsigned integer 16;
option PXE.mtftp-sport code 3 = unsigned integer 16;
option PXE.mtftp-tmout code 4 = unsigned integer 8;
option PXE.mtftp-delay code 5 = unsigned integer 8;
option arch code 93 = unsigned integer 16; # RFC4578

# This should be the group where you have the Quattor-related dhcpd parameters.
group {

  # grubx64.efi path (quattor/grub2-efi) should be adjusted to reflect its path
  # relative to the TFTP server root. This must be the directory where the Grub2
  # configuration files are located (and not its parent as for PXELINUX).
  if option arch = 00:07 {
    filename "quattor/grub2-efi/grubx64.efi";
  } else if option arch = 00:09 {
    filename "quattor/grub2-efi/grubx64.efi";
  } else {
    filename "quattor/pxelinux.0";
  }

  .... (your existing configuration)
  
```

See [SYSLINUX documentation](http://www.syslinux.org/wiki/index.php?title=PXELINUX#UEFI) for more details on the DHCP server configuration.

### Building the Grub2 UEFI boot loader

EL7 provides a `grub2-efi` package (there is no Grub2 package for EL6): the boot loader is `/boot/efi/EFI/centos/grubx64.efi`. Unfortunately, it 
is hardly usable without being rebuilt, as the default paths it uses are generally inappropriate and it may also lack the support for installing 
an EL6 machine (EL6 cannot be installed with the `linuxefi` command and requires the `linux` command to be used).

*Note: the Grub2 UEFI boot loader provided by EL7 can be used on an AII server running EL6.*

To rebuild your own Grub2 boot loader, install the the packages `grub2-tools` (commands to manage Grub2) and `grub2-efi-modules` (Grub2 modules). 
There are several possibilities but the recommended method is to use is `grub2-mkimage` command to build a boot loader image tailored for your 
configuration. `grub2-mkimage` important options are:

* `--prefix`: defines where the additional Grub modules (if any) are located. You need 
  to start this path with `(pxe)` which means that the modules are reachable through 
  the TFTP server and that the following path is relative to the TFTP server root. For 
  example, `(pxe)/grub2-modules` means that the Grub2 modules are located in directory 
  `grub2/modules` under the TFTP server root. Note that if you rebuild the Grub2 boot 
  loader as suggested here, this directory is not used.
* List of modules to add to the boot loader image: they are passed as parameters to `grub2-mkimage`. 
  You typically need `efi_gop efi_uga efinet linux linux16 linuxefi`: `linux` is not needed if you 
  don't intend to install EL6 machine with Grub2 UEFI (but this is 
  harmless to add them if you have some control over the persons who can trigger the installtion).
* `--format=x86_64-efi`: required for the boot loader to be usable with a UEFI firmware.
* `--output`: name of the boot loader file produced by the command. This is the file that 
  you need to copy to your TFTP server directory where the Grub2 configuration files will be generated 
  by `aii-shellfe --conigure` (this directory must match your DHCP server configuration, see above).

A typical `grub2-mkimage` command with the prefix example explained above (to be update according to your configuration) is:

```
grub2-mkimage --format=x86_64-efi --output=grubx64.efi --prefix='(pxe)/grub2-modules' efi_gop efi_uga efinet linux linuxefi
```

See the [Grub2 manual](https://www.gnu.org/software/grub/manual/grub.html) for details.

### New aii-shellfe Configuration Options

New `aii-shellfe` configuration options have been introduced with the UEFI support. Look at 
`/usr/share/doc/aii-server-VERSION/eg/aii-shellfe.conf` file for a list of all these options 
and their expected values.

UEFI support has been designed to work without any change to the configuration. One exception 
is `grub2_efi_kernel_root` that controls the path to the kernel to be loaded. Grub2 EFI interprets 
the path differently from PXELINUX: the path must be an absolute path (starting with a `/`) which 
is the path relative to the TFTP server root. If you use the default directory name for Grub2 
configuration files (`grub2-efi`) and if your Quattor TFTP server directory is two levels under 
`/` (like in `/tftproot/quattor` when `/tftproot` is the TFTP server root), the default value should 
be appropriate. Else you may need to adjust the path with `grub2_efi_kernel_root`. Enable TFTP 
server verbose mode to troubleshoot problems related to this path.

## Changes to Host Profiles

There is no change required to activate the use of UEFI for a given machine. Grub2 UEFI boot will 
be used if the machine firmware is configured to use UEFI, PXELINUX will be used if the firmware is 
configured to use legacy BIOS. The DHCP request will contain the information and the appropriate 
configuration will be selected.

Nevertheless, to be able to successfully install the machine through Grub2 UEFI, the first partition 
of the system disk must dedicated to Grub2. If you use the template library, this partition is 
automatically added if you define the variable `DISK_BIOS_TYPE_UEFI` to true. Else, you need to 
ensure that the first partition created has a size of 200 MB and has its flag set to `bios_grub`.

*Note: it is harmless to define variable `DISK_BIOS_TYPE_UEFI` on every machine, even if it is still 
using the legacy BIOS. The only exception is if you want to boot a disk larger than 2 GB with the 
legacy BIOS: in this case the variable `DISK_BOOT_ADD_BIOSBOOT_PART` must be defined instead 
(and the partition flag is not the one expected by Grub2 UEFI).*
