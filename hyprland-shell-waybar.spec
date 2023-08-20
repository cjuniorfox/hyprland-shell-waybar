%global srcname hyprland-shell-waybar
%define debug_package %{nil}

Name:           hyprland-shell-waybar
Version:        0.0.0
Release:        0%{?dist}
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

Source0:        %{name}-%{version}.tar.gz


%description
Waybar theme for using with Hyprland made for hyprland-shell

%prep
%define xdgWaybar        %{_sysconfdir}/xdg/waybar
%autosetup

%build

%install
mkdir -p $RPM_BUILD_ROOT%{xdgWaybar}/scripts/
mkdir -p $RPM_BUILD_ROOT%{xdgWaybar}/styles/
install -d $RPM_BUILD_ROOT%{xdgWaybar}/scripts/
install -d $RPM_BUILD_ROOT%{xdgWaybar}/styles/
install hyprland $RPM_BUILD_DIR%{xdgWaybar}
install transparent.css $RPM_BUILD_DIR%{xdgWaybar}/styles/
install under_rainbow.css $RPM_BUILD_DIR%{xdgWaybar}/styles/
install -m 755 dunst_notify  $RPM_BUILD_ROOT%{xdgWaybar}/scripts/
install -m 755 start_waybar_hyprland $RPM_BUILD_ROOT%{_bindir}


%files
%{xdgWaybar}/hyprland
%{xdgWaybar}/styles/transparent.css
%{xdgWaybar}/styles/under_rainbow.css
%{xdgWaybar}/styles/transparent.css
%{xdgWaybar}/scripts/dunst_notify
%{_bindir}/start_waybar_hyprland

%changelog
