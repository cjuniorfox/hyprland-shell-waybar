%global srcname hyprland-shell-waybar
%define debug_package %{nil}

Name:           hyprland-shell-waybar
Version:        1.0.3
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
Requires:       waybar-hyprland
Requires:       checkupdate
Requires:       fontawesome6-free
Requires:       rofi-shutdown-menu
Requires:       jq

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
install -m 755 start_waybar_hyprland $RPM_BUILD_ROOT%{_bindir}


%files
%{xdgWaybar}/hyprland.json
%{xdgWaybar}/hyprland.css
%{xdgWaybar}/modules.json
%{xdgWaybar}/scripts/dunst_notify
%{xdgWaybar}/scripts/keys_blocked
%{_bindir}/start_waybar_hyprland

%changelog
* Tue Aug 29 2023 Junior_FOX <cjuniorfox@gmail.com> 1.0.3-1
- change dependency (cjuniorfox@gmail.com)

* Sat Aug 26 2023 Junior_FOX <cjuniorfox@gmail.com> 1.0.2-1
- added dependencies (cjuniorfox@gmail.com)

* Sat Aug 26 2023 Junior_FOX <cjuniorfox@gmail.com> 1.0.1-1
- added dependencies (cjuniorfox@gmail.com)

* Sun Aug 20 2023 Junior_FOX <cjuniorfox@gmail.com> 1.0.0-1
- Initial relase
