Name: u-boot-tools
Version: 2018.11
Release: alt1

Summary: Das U-Boot
License: GPL
Group: System/Kernel and hardware

Provides: uboot-tools = %version-%release
Obsoletes: uboot-tools

Source: %name-%version-%release.tar

BuildRequires: flex libssl-devel libSDL-devel

%description
boot loader for embedded boards based on PowerPC, ARM, MIPS and several
other processors, which can be installed in a boot ROM and used to
initialize and test the hardware or to download and run application code.
This package contains sandboxed U-Boot and tools.

%prep
%setup

%build
echo CONFIG_HOST_32BIT=y >> configs/sandbox_defconfig
echo CONFIG_TOOLS_DEBUG=y >> configs/sandbox_defconfig 
%make_build sandbox_defconfig all

%install
install -pm0755 -D u-boot %buildroot%_bindir/u-boot
install -pm0755 tools/{dumpimage,fdtgrep,gen_eth_addr,mkimage,mkenvimage}  %buildroot%_bindir/

%files
%doc README board/sandbox/README.sandbox
%_bindir/*

%changelog
* Fri Jan 11 2019 Sergey Bolshakov <sbolshakov@altlinux.ru> 2018.11-alt1
- initial
