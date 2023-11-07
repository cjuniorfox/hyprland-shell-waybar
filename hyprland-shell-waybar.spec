%global srcname hyprland-shell-waybar
%define debug_package %{nil}

Name:           hyprland-shell-waybar
Version:        1.0.15
Release:        1%{?dist}
Summary:        Waybar config and themes made for using with hyprland
Url:            https://pagure.io/%{srcname}
# Sources can be obtained by
# git clone https://pagure.io/hyprland-shell-waybar
# cd rofi-shutdown-menu
# tito build --tgz
License:        GPLv3


BuildRequires: systemd-rpm-macros

BuildArch:      noarch
Requires:       waybar
Requires:       checkupdate
Requires:       fontawesome6-free
Requires:       rofi-shutdown-menu
Requires:       jq
Requires:       hyprland-keyboard-changer

Source0:        %{name}-%{version}.tar.gz


%description
Waybar theme for using with Hyprland made for hyprland-shell

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
* Tue Nov 07 2023 Junior_FOX <cjuniorfox@gmail.com> 1.0.15-1
- taskbar' (cjuniorfox@gmail.com)
- taskbar' (cjuniorfox@gmail.com)

* Tue Oct 17 2023 Junior_FOX <cjuniorfox@gmail.com> 1.0.14-1
- creation for empty file for checkupdate when starts waybar
  (cjuniorfox@gmail.com)

* Wed Sep 27 2023 Junior_FOX <cjuniorfox@gmail.com> 1.0.13-1
- fixes for proper build (cjuniorfox@gmail.com)

* Wed Sep 27 2023 Junior_FOX <cjuniorfox@gmail.com> 1.0.12-1
- renamed (cjuniorfox@gmail.com)

* Wed Sep 27 2023 Junior_FOX <cjuniorfox@gmail.com> 1.0.11-1
- added the close button (cjuniorfox@gmail.com)

* Mon Sep 25 2023 Junior_FOX <cjuniorfox@gmail.com> 1.0.10-1
- dependence changes (cjuniorfox@gmail.com)

* Sat Sep 16 2023 Junior_FOX <cjuniorfox@gmail.com> 1.0.9-1
- added disk free space as default (cjuniorfox@gmail.com)

* Thu Sep 14 2023 Junior_FOX <cjuniorfox@gmail.com> 1.0.8-1
- changes into spacing (cjuniorfox@gmail.com)

* Tue Sep 12 2023 Junior_FOX <cjuniorfox@gmail.com> 1.0.7-1
- removal of quick launch styles (cjuniorfox@gmail.com)

* Wed Sep 06 2023 Junior_FOX <cjuniorfox@gmail.com> 1.0.6-1
- fix issue regarding the keyboard change script (cjuniorfox@gmail.com)

* Wed Sep 06 2023 Junior_FOX <cjuniorfox@gmail.com> 1.0.5-1
- removal of modules left from main config (cjuniorfox@gmail.com)

* Wed Sep 06 2023 Junior_FOX <cjuniorfox@gmail.com> 1.0.4-1
- added keyboard-changer dependency (cjuniorfox@gmail.com)
- refactoring. custom scripts, launcher, new gui (cjuniorfox@gmail.com)

* Tue Aug 29 2023 Junior_FOX <cjuniorfox@gmail.com> 1.0.3-1
- change dependency (cjuniorfox@gmail.com)

* Sat Aug 26 2023 Junior_FOX <cjuniorfox@gmail.com> 1.0.2-1
- added dependencies (cjuniorfox@gmail.com)

* Sat Aug 26 2023 Junior_FOX <cjuniorfox@gmail.com> 1.0.1-1
- added dependencies (cjuniorfox@gmail.com)

* Sun Aug 20 2023 Junior_FOX <cjuniorfox@gmail.com> 1.0.0-1
- Initial relase
