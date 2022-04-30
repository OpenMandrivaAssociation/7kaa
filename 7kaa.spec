Name:		7kaa
Version:	2.15.5
Release:	1
Summary:	Seven Kingdoms: Ancient Adversaries is a real-time strategy game
Group:		Games/Strategy
License:	GPLv2
URL:		http://7kfans.com/
Source0:	https://sourceforge.net/projects/skfans/files/7KAA%20%{version}/7kaa-%{version}.tar.xz
#source mirror: https://github.com/the3dfxdude/7kaa/releases/
Source1:	%{name}.png
Source2:	%{name}.xpm

BuildRequires:  gettext
BuildRequires:  pkgconfig(libcurl)
BuildRequires:  pkgconfig(libenet)
BuildRequires:  pkgconfig(sdl2)
BuildRequires:  pkgconfig(openal)

Requires:	%{name}-data

Recommends:	%{name}-music

%description
Seven Kingdoms made departures from the traditional real-time strategy models
of "gather resources, build a base and army, and attack". The economic model
bears more resemblance to a turn-based strategy game. It features an espionage
system that allows players to train and control spies individually, who each
have a spying skill that increases over time. The player is also responsible
for catching spies in their own kingdom. Inns built within the game allow
players to hire mercenaries of various occupations, skill levels, and races.
Skilled spies of enemy races are essential to a well-conducted espionage
program, and the player can bolster his forces by grabbing a skilled fighter
or give ones own factories, mines, and towers of science, a boost by hiring a
skilled professional.

Enlight Software decided to release the game to the Open Source community
in August 2009. At that time everything, but the music, was released under
the GPL v2. The music has a slightly different license.

%package data
Summary:        Data files for Seven Kingdoms: Ancient Adversaries
BuildArch:      noarch
Conflicts:      %{name} < 2.14.6

%description data
This package contains arch-independent data files for the Seven Kingdoms:
Ancient Adversaries game.

%prep
%autosetup -p1

%build
%ifarch %{ix86}
export CC=gcc
export CXX=g++
%define _disable_lto 1
%endif

# ARM uses unsigned chars, breaks compilation: https://github.com/the3dfxdude/7kaa/issues/81
export CXXFLAGS="%{optflags} -fsigned-char"
%configure --bindir=%{_gamesbindir} \
               --datadir=%{_gamesdatadir}
%make_build

%install
%make_install

mkdir -p %{buildroot}%{_datadir}/pixmaps
install -m 644 %{SOURCE1} %{SOURCE2} %{buildroot}%{_datadir}/pixmaps/

# menu-entry
mkdir -p  %{buildroot}%{_datadir}/applications
cat > %{buildroot}%{_datadir}/applications/%{name}.desktop << EOF
[Desktop Entry]
Version=1.0
Name=Seven Kingdoms
Comment=Seven Kingdoms: Ancient Adversaries
Type=Application
Exec=%{name}
Icon=%{name}
Categories=Game;StrategyGame;
EOF

%find_lang %{name}

%files -f %{name}.lang
%doc COPYING README
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/%{name}.*
%{_gamesbindir}/%{name}

%files data
%{_gamesdatadir}/%{name}/
