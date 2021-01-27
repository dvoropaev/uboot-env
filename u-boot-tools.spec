Name: u-boot-tools-env
Version: 2020.10
Release: alt1

Summary: Access to the uboot environment from userspace.
License: GPLv2+
Group: System/Kernel and hardware

ExclusiveArch: armh aarch64 %ix86 x86_64 mipsel

%ifarch mipsel
%define config_name qemu_mipsel_defconfig
%else
%define config_name sandbox_defconfig
%endif

Provides: uboot-tools-env = %version-%release
Obsoletes: uboot-tools-env

Source: %name-%version-%release.tar

BuildRequires: flex libssl-devel


%description
This package includes tools to read (fw_printenv) and modify
(fw_setenv) U-Boot bootloader environment.

%prep
%setup

%build
%make_build %config_name envtools

%install
mkdir -p %buildroot%_sysconfdir
mkdir -p %buildroot%_bindir
install -pm0644 fw_env.config %buildroot%_sysconfdir
install -pm0755 tools/env/fw_printenv %buildroot%_bindir/
ln -s %_bindir/fw_printenv %buildroot%_bindir/fw_setenv


%files
%_bindir/fw_*
%config(noreplace) %_sysconfdir/fw_env.config

%changelog
* Tue Jan 26 2021 Dmitriy Voropaev <voropaevdmtr@altlinux.org> 2020.10-alt1
- build envtools as a separate package


