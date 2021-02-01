Name: u-boot-tools
Version: 2020.10
Release: alt2

Summary: Das U-Boot
License: GPLv2+
Group: System/Kernel and hardware

ExclusiveArch: armh aarch64 %ix86 x86_64

Provides: uboot-tools = %version-%release
Obsoletes: uboot-tools

Source: %name-%version-%release.tar

BuildRequires: flex libssl-devel

%def_without sandbox

%ifarch mipsel
%define config_name qemu_mipsel_defconfig
%else
%define config_name sandbox_defconfig
%endif

%description
boot loader for embedded boards based on PowerPC, ARM, MIPS and several
other processors, which can be installed in a boot ROM and used to
initialize and test the hardware or to download and run application code.
This package contains sandboxed U-Boot and tools.

%prep
%setup

%build
%make_build sandbox_defconfig %{?_with_sandbox:all NO_SDL=1}%{!?_with_sandbox:tools} envtools

%install
mkdir -p %buildroot%_sysconfdir
mkdir -p %buildroot%_bindir
install -pm0755 tools/{dumpimage,fdtgrep,gen_eth_addr,mkimage,mkenvimage,/env/fw_printenv} %{?_with_sandbox:u-boot} %buildroot%_bindir/
install -pm0644 fw_env.config %buildroot%_sysconfdir
ln -rs %buildroot%_bindir/fw_printenv %buildroot%_bindir/fw_setenv

%files
%_bindir/*
%config(noreplace) %_sysconfdir/fw_env.config

%changelog
* Mon Feb 01 2021 Voropaev Dmitriy <voropaevdmtr@altlinux.org> 2020.10-alt2
- added utilities fw_printenv and fw_setenv
- added mipsel support

* Tue Oct 06 2020 Sergey Bolshakov <sbolshakov@altlinux.ru> 2020.10-alt1
- 2020.10 released

* Fri Jul 10 2020 Sergey Bolshakov <sbolshakov@altlinux.ru> 2020.07-alt1
- 2020.07 released

* Tue Apr 14 2020 Sergey Bolshakov <sbolshakov@altlinux.ru> 2020.04-alt1
- 2020.04 released

* Thu Jan 09 2020 Sergey Bolshakov <sbolshakov@altlinux.ru> 2020.01-alt1
- 2020.01 released

* Tue Oct 08 2019 Sergey Bolshakov <sbolshakov@altlinux.ru> 2019.10-alt1
- 2019.10 released

* Fri Jul 19 2019 Sergey Bolshakov <sbolshakov@altlinux.ru> 2019.07-alt1
- 2019.07 released

* Fri Apr 19 2019 Sergey Bolshakov <sbolshakov@altlinux.ru> 2019.04-alt1
- 2019.04 released

* Tue Jan 22 2019 Sergey Bolshakov <sbolshakov@altlinux.ru> 2019.01-alt1
- 2019.01 released

* Fri Jan 11 2019 Sergey Bolshakov <sbolshakov@altlinux.ru> 2018.11-alt1
- initial
