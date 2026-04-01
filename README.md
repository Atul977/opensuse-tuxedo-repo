# 🦎 Tuxedo Hardware Control for Acer & Clevo Laptops (openSUSE)

> [!CAUTION]
> **openSUSE TUMBLEWEED ONLY:** This repository provides prebuilt `.rpm` binaries specifically for openSUSE Tumbleweed. These packages will **NOT** work on Ubuntu, Fedora, Debian, or Arch Linux.

This project hosts a custom openSUSE binary repository that enables native control over:
* 🎨 **RGB Keyboard Backlighting**
* 🌬️ **Fan Speed Curves**
* ⚡ **Power & Performance Profiles**

---

### 💻 Supported Devices
Specifically optimized and patched for:
* **Acer Aspire A715-79G Series**
* **Acer ALG Series**
* Any laptop using **Clevo internal hardware** that requires `tuxedo-drivers`.

**🧪 Tested Build Environment:**
* **CPU:** Intel Core i5-13420H
* **GPU:** NVIDIA GeForce RTX 3050 (6GB)
* **OS:** openSUSE Tumbleweed

---

### 📦 Included Packages
Unlike the upstream split, this repository unifies the Rust tools for a cleaner RPM installation.

| Package | Description |
| :--- | :--- |
| `tuxedo-drivers-dkms` | 🔧 Patched DKMS kernel drivers for Acer compatibility. |
| `tuxedo-rs` | ⚙️ Unified package containing both the `tailord` hardware daemon and the GTK4 `tailor_gui` (Patched with the Niri color picker fix). |

---

### 🚀 Quick Installation

Copy and paste these commands into your terminal to add the repository, install the packages, and start the hardware daemon:

```bash
# 1. Add the custom repository (URL is case-sensitive!)
sudo zypper ar -f [https://atul977.github.io/OpenSuse-Tuxedo-Repo/tuxedo.repo](https://atul977.github.io/OpenSuse-Tuxedo-Repo/tuxedo.repo)

# 2. Refresh Zypper and install the patched drivers and control suite
sudo zypper refresh
sudo zypper install tuxedo-drivers-dkms tuxedo-rs

# 3. Enable and start the hardware daemon to run on boot
sudo systemctl enable --now tailord.service
