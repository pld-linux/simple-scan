Summary:	Simple scanning utility
Summary(pl.UTF-8):	Proste narzędzie do skanowania
Name:		simple-scan
Version:	3.36.2.1
Release:	1
License:	GPL v3+
Group:		X11/Applications/Multimedia
Source0:	http://ftp.gnome.org/pub/GNOME/sources/simple-scan/3.36/%{name}-%{version}.tar.xz
# Source0-md5:	b0ec45780a685f01f243dd19e669f908
URL:		https://launchpad.net/simple-scan
BuildRequires:	PackageKit-devel >= 1.1.5
BuildRequires:	cairo-devel
BuildRequires:	colord-devel
BuildRequires:	gdk-pixbuf2-devel >= 2.0
BuildRequires:	gettext-tools
BuildRequires:	glib2-devel >= 1:2.38
BuildRequires:	gtk+3-devel >= 3.22
BuildRequires:	itstool
BuildRequires:	libgusb-devel >= 0.2.7
BuildRequires:	libjpeg-devel
BuildRequires:	libwebp-devel
BuildRequires:	meson >= 0.37.1
BuildRequires:	ninja >= 1.5
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(macros) >= 1.736
BuildRequires:	sane-backends-devel
BuildRequires:	tar >= 1:1.22
BuildRequires:	vala >= 2:0.22.0
BuildRequires:	vala-colord
BuildRequires:	vala-libgusb >= 0.2.7
BuildRequires:	yelp-tools
BuildRequires:	xz
BuildRequires:	zlib-devel
Requires(post,postun):	glib2 >= 1:2.38
Requires:	PackageKit >= 1.1.5
Requires:	glib2 >= 1:2.38
Requires:	hicolor-icon-theme
Requires:	gtk+3 >= 3.22
Requires:	libgusb >= 0.2.7
Suggests:	colord
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Simple Scan is an easy-to-use application, designed to let users
connect their scanner and quickly have the image/document in an
appropriate format.

%description -l pl.UTF-8
Simple Scan to łatwa w użyciu aplikacja, pozwalająca użytkownikom
podłączyć skaner i szybko otrzymać dokument we właściwym formacie.

%prep
%setup -q

%build
%meson build

%ninja_build -C build

%install
rm -rf $RPM_BUILD_ROOT

%ninja_install -C build

%find_lang %{name} --with-gnome

%clean
rm -rf $RPM_BUILD_ROOT

%post
%glib_compile_schemas
%update_icon_cache hicolor

%postun
%glib_compile_schemas
%update_icon_cache hicolor

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc NEWS README.md
%attr(755,root,root) %{_bindir}/simple-scan
%{_datadir}/glib-2.0/schemas/org.gnome.SimpleScan.gschema.xml
%{_datadir}/metainfo/simple-scan.appdata.xml
%{_desktopdir}/simple-scan.desktop
%{_iconsdir}/hicolor/scalable/apps/org.gnome.SimpleScan.svg
%{_iconsdir}/hicolor/symbolic/apps/org.gnome.SimpleScan-symbolic.svg
%{_mandir}/man1/simple-scan.1*
