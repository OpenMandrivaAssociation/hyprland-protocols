Name:           hyprland-protocols
Version:        0.2
Release:        1
Summary:        Wayland protocol extensions for Hyprland
BuildArch:      noarch
Group:          HyprlandWayland
License:        BSD-3-Clause
URL:            https://github.com/hyprwm/hyprland-protocols
Source0:        https://github.com/hyprwm/hyprland-protocols/archive/v%{version}/%{name}-%{version}.tar.gz
 
BuildRequires:  meson
 
%description
%{summary}.
 
%package        devel
Summary:        Wayland protocol extensions for Hyprland
 
%description    devel
%{summary}.
 
%prep
%autosetup -p1
 
%build
%meson
%meson_build
 
%install
%meson_install
 
%files devel
%license LICENSE
%doc README.md
%{_datadir}/pkgconfig/%{name}.pc
%{_datadir}/%{name}/
