# dosbox-x has its own autogen.sh script that differs a little
%define _disable_rebuild_configure 1

Summary:	DOS Emulator
Summary(pl.UTF-8):	Emulator DOS-a
Name:		dosbox-x
Version:	2026.01.02
Release:	0.2
License:	GPL v2+
Group:		Applications/Emulators
Source0:	https://github.com/joncampbell123/dosbox-x/archive/refs/tags/%{name}-v%{version}.tar.gz
# Source0-md5:	4818bcfa9bdb349812a70a3b990d25fa
URL:		https://dosbox-x.com/
BuildRequires:	SDL2-devel
BuildRequires:	SDL2_image-devel
BuildRequires:	SDL2_net-devel
BuildRequires:	alsa-lib-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	fluidsynth-devel
BuildRequires:	freetype-devel
BuildRequires:	gmock-devel
BuildRequires:	gtest-devel
BuildRequires:	libglvnd-libGL-devel
BuildRequires:	libglvnd-libGL-devel
BuildRequires:	libpcap-devel
BuildRequires:	libpng-devel
BuildRequires:	libslirp-devel >= 4.6.1
BuildRequires:	libtool
BuildRequires:	m4
BuildRequires:	ncurses-devel
BuildRequires:	opusfile-devel
BuildRequires:	speexdsp-devel
BuildRequires:	xorg-lib-libX11-devel
BuildRequires:	xorg-lib-libxkbfile-devel
BuildRequires:	zlib-devel
Requires(post,postun):	desktop-file-utils
Requires(post,postun):	gtk-update-icon-cache
Obsoletes:	dosbox <= 0.74.3
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
DOSBox is a DOS emulator, emulating 286/386 CPUs, filesystems,
XMS/EMS, various graphics cards and sound cards.

DOSBox-x is a fork of DOSBox that tries to modernize the codebase and
add new features.

%description -l pl.UTF-8
DOSBox to emulator DOS-a, emulujący procesory 286/386, systemy plików,
XMS/EMS, różne karty graficzne i dźwiękowe.

DOSBox-x to rozwinięcie DOSBoxa, które ma na celu unowocześnienie kodu
źródłowego i dodanie nowych funkcji.

%post
%update_icon_cache hicolor
%update_desktop_database_post

%postun
%update_icon_cache hicolor
%update_desktop_database_postun

%prep
%setup -q -n %{name}-%{name}-v%{version}
./autogen.sh

%build
%configure \
	--enable-sdl2

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/dosbox-x
%{bash_compdir}/dosbox-x
%{_iconsdir}/hicolor/*/apps/dosbox-x.*
%{_desktopdir}/com.dosbox_x.DOSBox-X.desktop
%{_datadir}/metainfo/com.dosbox_x.DOSBox-X.metainfo.xml
%{_datadir}/dosbox-x
%{_mandir}/man1/dosbox-x.1*

%clean
rm -rf $RPM_BUILD_ROOT
