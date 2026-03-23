{
  description = "Waybar config and themes made for using with Hyprland";

  inputs = {
    nixpkgs.url = "github:NixOS/nixpkgs/nixos-25.11";

    # Your custom packages — replace URLs once repos are available
    rofi-shutdown-menu = {
      url = "github:cjuniorfox/rofi-shutdown-menu/nix";
      inputs.nixpkgs.follows = "nixpkgs";
    };
    rofi-audio-output-selector = {
      url = "github:cjuniorfox/rofi-audio-output-selector/nix";
      inputs.nixpkgs.follows = "nixpkgs";
    };
    hyprland-keyboard-changer = {
      url = "github:cjuniorfox/hyprland-keyboard-changer/nix";
      inputs.nixpkgs.follows = "nixpkgs";
    };
  };

  outputs = { self, nixpkgs
            , rofi-shutdown-menu
            , rofi-audio-output-selector
            , hyprland-keyboard-changer
            }:
    let
      system = "x86_64-linux";
      pkgs   = nixpkgs.legacyPackages.${system};
    in
    {
      packages.${system} = rec {
        hyprland-shell-waybar = pkgs.callPackage ./default.nix {
          rofi-shutdown-menu        = rofi-shutdown-menu.packages.${system}.default;
          rofi-audio-output-selector = rofi-audio-output-selector.packages.${system}.default;
          hyprland-keyboard-changer = hyprland-keyboard-changer.packages.${system}.default;
        };
        default = hyprland-shell-waybar;
      };

      # Optional: expose as a NixOS/home-manager module consumers can import
      overlays.default = final: _prev: {
        hyprland-shell-waybar = self.packages.${final.system}.hyprland-shell-waybar;
      };
    };
}
