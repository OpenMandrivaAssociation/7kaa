Name:		7kaa
Version:	2.14.3
Release:	%mkrel 1
Summary:	Seven Kingdoms: Ancient Adversaries is a real-time strategy game
Group:		Games/Strategy
License:	GPLv2
URL:		http://7kfans.com/
Source0:	http://sourceforge.net/projects/skfans/files/7KAA%20%{version}/%{name}-source-%{version}.tar.bz2
Source1:	%{name}.png
Source2:	%{name}.xpm
Patch0:		7kaa-2.14.3-datapath.patch
BuildRequires:	SDL-devel
BuildRequires:	SDL_net-devel
BuildRequires:	pkgconfig(openal)
Requires:	%{name}-data
Suggests:	%{name}-music

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

%prep
%setup -q
%patch0 -p1

%build
%configure2_5x
%make

%install
%__rm -rf %{buildroot}
%makeinstall_std

%__mkdir_p %{buildroot}%{_datadir}/pixmaps
%__install -D -m 644 %{SOURCE1} %{buildroot}%{_datadir}/pixmaps/
%__install -D -m 644 %{SOURCE2} %{buildroot}%{_datadir}/pixmaps/

# menu-entry
%__mkdir_p  %{buildroot}%{_datadir}/applications
%__cat > %{buildroot}%{_datadir}/applications/%{name}.desktop << EOF
[Desktop Entry]
Version=1.0
Name=Seven Kingdoms
Comment=Seven Kingdoms: Ancient Adversaries
Type=Application
Exec=7kaa
Icon=7kaa
Categories=Game;StrategyGame;
EOF

%clean
%__rm -rf %{buildroot}

%files
%doc COPYING README
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/%{name}.*



%changelog
* Fri Mar 23 2012 Andrey Bondrov <abondrov@mandriva.org> 2.14.3-1mdv2011.0
+ Revision: 786258
- imported package 7kaa

