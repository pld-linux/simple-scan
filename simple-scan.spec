Summary:	Simple scanning utility
Name:		simple-scan
Version:	3.28.0
Release:	1
License:	GPL v3+
Group:		Applications/Multimedia
Source0:	https://download.gnome.org/sources/simple-scan/3.28/%{name}-%{version}.tar.xz
# Source0-md5:	1313de249d70d7fc844ef485603f4977
URL:		https://launchpad.net/simple-scan
BuildRequires:	PackageKit-devel
BuildRequires:	autoconf
BuildRequires:	automake >= 1:1.11
BuildRequires:	cairo-devel
BuildRequires:	colord-devel
BuildRequires:	gdk-pixbuf2-devel
BuildRequires:	gettext-tools
BuildRequires:	glib2-devel >= 1:2.38.0
BuildRequires:	gnome-common
BuildRequires:	gnome-doc-utils
BuildRequires:	gtk+3-devel >= 3.12.0
BuildRequires:	itstool
BuildRequires:	libgusb-devel >= 0.2.7
BuildRequires:	libjpeg-devel
BuildRequires:	libwebp-devel
BuildRequires:	meson >= 0.37.1
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(macros) >= 1.198
BuildRequires:	sane-backends-devel
BuildRequires:	vala >= 2:0.22.0
BuildRequires:	vala-colord
BuildRequires:	vala-libgusb
BuildRequires:	yelp-tools
BuildRequires:	zlib-devel
Requires(post,postun):	glib2 >= 1:2.26.0
Requires:	gnome-icon-theme
Suggests:	colord
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Simple Scan is an easy-to-use application, designed to let users
connect their scanner and quickly have the image/document in an
appropriate format.

%prep
%setup -q

%build
%meson build
%meson_build -C build

%install
rm -rf $RPM_BUILD_ROOT

%meson_install -C build

%find_lang %{name} --with-gnome

%clean
rm -rf $RPM_BUILD_ROOT

%post
%glib_compile_schemas

%postun
%glib_compile_schemas

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc NEWS README.md
%attr(755,root,root) %{_bindir}/simple-scan
%{_mandir}/man1/simple-scan.1*
%{_desktopdir}/simple-scan.desktop
%{_datadir}/metainfo/simple-scan.appdata.xml
%{_datadir}/glib-2.0/schemas/org.gnome.SimpleScan.gschema.xml
%{_datadir}/simple-scan
