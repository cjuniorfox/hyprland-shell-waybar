{ lib
, stdenvNoCC
, jq
, waybar
, font-awesome
, python3Packages
, socat
, dbus
, dunst
, psmisc          # killall
, weathergrabber
, rofi-shutdown-menu
, rofi-audio-output-selector
, hyprland-keyboard-changer
}:

stdenvNoCC.mkDerivation {
  pname = "hyprland-shell-waybar";
  version = "1.0.57";

  src = ./.;

  nativeBuildInputs = [ jq ];

  # Runtime dependencies wired into scripts via PATH
  propagatedBuildInputs = [
    jq
    waybar
    font-awesome
    socat
    dbus              # dbus-monitor used in dunst_notify
    dunst             # dunstctl used in dunst_notify
    psmisc            # killall used in start_waybar_hyprland
    weathergrabber
    rofi-shutdown-menu
    rofi-audio-output-selector
    hyprland-keyboard-changer
  ];

  dontConfigure = true;
  dontBuild = true;

  installPhase = ''
    runHook preInstall

    xdgWaybar="$out/etc/xdg/waybar"
    install -d "$xdgWaybar/scripts"

    install -m 644 hyprland.css  "$xdgWaybar/hyprland.css"
    install -m 644 hyprland.json "$xdgWaybar/hyprland.json"
    install -m 644 modules.json  "$xdgWaybar/modules.json"

    install -m 755 dunst_notify  "$xdgWaybar/scripts/dunst_notify"
    install -m 755 keys_blocked  "$xdgWaybar/scripts/keys_blocked"
    install -m 755 close_window  "$xdgWaybar/scripts/close_window"

    install -d "$out/bin"
    install -m 755 start_waybar_hyprland "$out/bin/start_waybar_hyprland"

    # Patch hard-coded paths in the launcher script
    substituteInPlace "$out/bin/start_waybar_hyprland" \
      --replace '/etc/xdg/waybar/' "$xdgWaybar/"

    # Systemd user service
    install -Dm 644 hyprland-shell-waybar.service \
      "$out/lib/systemd/user/hyprland-shell-waybar.service"

    # Fix the ExecStart path in the service unit
    substituteInPlace "$out/lib/systemd/user/hyprland-shell-waybar.service" \
      --replace '/usr/bin/start_waybar_hyprland' "$out/bin/start_waybar_hyprland"

    runHook postInstall
  '';

  meta = with lib; {
    description = "Waybar config and themes made for using with Hyprland";
    homepage    = "https://pagure.io/hyprland-shell-waybar";
    license     = licenses.gpl3Only;
    platforms   = platforms.linux;
    maintainers = [ ];
  };
}
