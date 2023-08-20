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
%autosetup

%build

%install
mkdir -p $RPM_BUILD_ROOT%{_sysconfdir}/xdg/waybar/scripts/
mkdir -p $RPM_BUILD_ROOT%{_sysconfdir}/xdg/waybar/styles/
install -d $RPM_BUILD_ROOT%{_sysconfdir}/xdg/waybar/
install -d $RPM_BUILD_ROOT%{_sysconfdir}/xdg/waybar/scripts/
install -d $RPM_BUILD_ROOT%{_sysconfdir}/xdg/waybar/styles/
install -d $RPM_BUILD_ROOT%{_bindir}
install -m 755 start_waybar_hyprland $RPM_BUILD_ROOT%{_bindir}
install -m 755 dunst_notify  $RPM_BUILD_ROOT%{_sysconfdir}/xdg/waybar/scripts/

%files
%{_sysconfdir}/xdg/waybar/hyprland
%{_sysconfdir}/xdg/waybar/styles/transparent.css
%{_sysconfdir}/xdg/waybar/styles/under_rainbow.css
%{_sysconfdir}/xdg/waybar/styles/transparent.css
%{_sysconfdir}/xdg/waybar/scripts/dunst_notify
%{_bindir}/start_waybar_hyprland

%changelog
