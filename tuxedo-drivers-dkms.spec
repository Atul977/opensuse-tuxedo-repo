Name:           tuxedo-drivers-dkms
Version:        4.21.3
Release:        0
Summary:        TUXEDO Computers kernel module drivers
License:        GPL-2.0-or-later
URL:            https://github.com/Atul977/tuxedo-drivers
Source0:        main.zip
Source1:        tuxedo-drivers.dkms
BuildArch:      noarch

Requires:       dkms

%description
TUXEDO kernel module drivers for keyboard, keyboard backlight & general hardware I/O using the SysFS interface.

%prep
%autosetup -n tuxedo-drivers-main

%build
# DKMS handles the actual building on the end-user's machine

%install
# Install your locally tracked DKMS file
mkdir -p %{buildroot}/usr/src/tuxedo-drivers-%{version}/
install -Dm644 %{SOURCE1} %{buildroot}/usr/src/tuxedo-drivers-%{version}/dkms.conf
sed -i "s/#MODULE_VERSION#/%{version}/g" %{buildroot}/usr/src/tuxedo-drivers-%{version}/dkms.conf

# Grab the configs from their new 'files/' location upstream
install -Dm644 files/usr/lib/modprobe.d/*.conf -t %{buildroot}/usr/lib/modprobe.d/
install -Dm644 files/usr/lib/udev/rules.d/*.rules -t %{buildroot}/usr/lib/udev/rules.d/
install -Dm644 files/usr/lib/udev/hwdb.d/*.hwdb -t %{buildroot}/usr/lib/udev/hwdb.d/

# Copy the actual source files for DKMS to compile
cp -r src/* %{buildroot}/usr/src/tuxedo-drivers-%{version}/

%post
dkms add -m tuxedo-drivers -v %{version} --rpm_safe_upgrade || :
dkms build -m tuxedo-drivers -v %{version} || :
dkms install -m tuxedo-drivers -v %{version} || :

%preun
dkms remove -m tuxedo-drivers -v %{version} --all --rpm_safe_upgrade || :

%files
/usr/src/tuxedo-drivers-%{version}/
/usr/lib/modprobe.d/*.conf
/usr/lib/udev/rules.d/*.rules
/usr/lib/udev/hwdb.d/*.hwdb
