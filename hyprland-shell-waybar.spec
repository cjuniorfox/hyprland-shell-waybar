%global srcname hyprland-shell-waybar
%define debug_package %{nil}

Name:           hyprland-shell-waybar
Version:        1.0.31
Release:        1%{?dist}
Summary:        Waybar config and themes made for using with Hyprland
Url:            https://pagure.io/%{srcname}
# Sources can be obtained by
# git clone https://pagure.io/hyprland-shell-waybar
# cd hyprland-shell-waybar
# tito build --tgz
License:        GPLv3

BuildRequires:  systemd-rpm-macros
BuildArch:      noarch
Requires:       jq, waybar, (fontawesome-6-free-fonts or fontawesome6-free), rofi-shutdown-menu, rofi-audio-output-selector, hyprland-keyboard-changer

Source0:        %{name}-%{version}.tar.gz

%description
Waybar theme for using with Hyprland made for hyprland-shell.

%prep
%define xdgWaybar %{_sysconfdir}/xdg/waybar
%autosetup

%build

%install
install -d $RPM_BUILD_ROOT%{xdgWaybar}/scripts/
install -d $RPM_BUILD_ROOT%{_bindir}
install hyprland.css                 $RPM_BUILD_ROOT%{xdgWaybar}
install hyprland.json                $RPM_BUILD_ROOT%{xdgWaybar}
install modules.json                 $RPM_BUILD_ROOT%{xdgWaybar}
install -m 755 dunst_notify          $RPM_BUILD_ROOT%{xdgWaybar}/scripts/
install -m 755 keys_blocked          $RPM_BUILD_ROOT%{xdgWaybar}/scripts/
install -m 755 close_window          $RPM_BUILD_ROOT%{xdgWaybar}/scripts/
install -m 755 start_waybar_hyprland $RPM_BUILD_ROOT%{_bindir}

%files
%{xdgWaybar}/hyprland.json
%{xdgWaybar}/hyprland.css
%{xdgWaybar}/modules.json
%{xdgWaybar}/scripts/dunst_notify
%{xdgWaybar}/scripts/keys_blocked
%{xdgWaybar}/scripts/close_window
%{_bindir}/start_waybar_hyprland

%changelog
* Thu Aug 29 2024 Junior_FOX <cjuniorfox@gmail.com> 1.0.31-1
- removed formatted value from here (cjuniorfox@gmail.com)

* Thu Aug 29 2024 Junior_FOX <cjuniorfox@gmail.com> 1.0.30-1
- added click function for updates (cjuniorfox@gmail.com)

* Thu Aug 29 2024 Junior_FOX <cjuniorfox@gmail.com> 1.0.29-1
- fixed return type (cjuniorfox@gmail.com)

* Fri Aug 23 2024 Junior_FOX <cjuniorfox@gmail.com> 1.0.28-1
- added arrows for the update (cjuniorfox@gmail.com)

* Wed Aug 14 2024 Junior <cjuniorfox@gmail.com> 1.0.27-1
- added type as json (cjuniorfox@gmail.com)

X# Create your changelog entry below:
* Wed Aug 14 2024 Junior <cjuniorfox@gmail.com> 1.0.26-1
- fix left click for checkupdate (cjuniorfox@gmail.com)

* Wed Aug 14 2024 Junior_FOX <cjuniorfox@gmail.com> 1.0.25-1
- updated the checkupdate (cjuniorfox@gmail.com)
- fixed README formatting error (cjuniorfox@gmail.com)

* Tue Jul 09 2024 Junior <cjuniorfox@gmail.com> 1.0.24-1
- chore: removal for the checkupdate requirement (cjuniorfox@gmail.com)

* Mon Jul 08 2024 Junior <cjuniorfox@gmail.com> 1.0.23-1
- chore: added the option to select the output device (cjuniorfox@gmail.com)

* Thu May 02 2024 Junior <cjuniorfox@gmail.com> 1.0.22-1
- Changed the icon.

* Thu Dec 28 2023 Junior_FOX <cjuniorfox@gmail.com> 1.0.21-1
- Updated dependencies.

* Thu Dec 28 2023 Junior_FOX <cjuniorfox@gmail.com> 1.0.20-1
- Updated dependencies.

* Thu Nov 09 2023 Junior_FOX <cjuniorfox@gmail.com> 1.0.19-1
- Changed menu icon.

* Tue Nov 07 2023 Junior_FOX <cjuniorfox@gmail.com> 1.0.18-1
- Minor updates.

* Tue Nov 07 2023 Junior_FOX <cjuniorfox@gmail.com> 1.0.17-1
- Minor updates.

* Tue Nov 07 2023 Junior_FOX <cjuniorfox@gmail.com> 1.0.16-1
- Updated taskbar.

* Tue Nov 07 2023 Junior_FOX <cjuniorfox@gmail.com> 1.0.15-1
- Updated taskbar.

* Tue Oct 17 2023 Junior_FOX <cjuniorfox@gmail.com> 1.0.14-1
- Created empty file for checkupdate when starting Waybar.

* Wed Sep 27 2023 Junior_FOX <cjuniorfox@gmail.com> 1.0.13-1
- Fixed build issues.

* Wed Sep 27 2023 Junior_FOX <cjuniorfox@gmail.com> 1.0.12-1
- Renamed files.

* Wed Sep 27 2023 Junior_FOX <cjuniorfox@gmail.com> 1.0.11-1
- Added close button.

* Mon Sep 25 2023 Junior_FOX <cjuniorfox@gmail.com> 1.0.10-1
- Updated dependencies.

* Sat Sep 16 2023 Junior_FOX <cjuniorfox@gmail.com> 1.0.9-1
- Added disk free space as default.

* Thu Sep 14 2023 Junior_FOX <cjuniorfox@gmail.com> 1.0.8-1
- Updated spacing.

* Tue Sep 12 2023 Junior_FOX <cjuniorfox@gmail.com> 1.0.7-1
- Removed quick launch styles.

* Wed Sep 06 2023 Junior_FOX <cjuniorfox@gmail.com> 1.0.6-1
- Fixed issue with keyboard change script.

* Wed Sep 06 2023 Junior_FOX <cjuniorfox@gmail.com> 1.0.5-1
- Removed modules left from main config.

* Wed Sep 06 2023 Junior_FOX <cjuniorfox@gmail.com> 1.0.4-1
- Added keyboard-changer dependency.
- Refactored custom scripts, launcher, and GUI.

* Tue Aug 29 2023 Junior_FOX <cjuniorfox@gmail.com> 1.0.3-1
- Changed dependency.

* Sat Aug 26 2023 Junior_FOX <cjuniorfox@gmail.com> 1.0.2-1
- Added dependencies.

* Sat Aug 26 2023 Junior_FOX <cjuniorfox@gmail.com> 1.0.1-1
- Added dependencies.

* Sun Aug 20 2023 Junior_FOX <cjuniorfox@gmail.com> 1.0.0-1
- Initial release.