Summary:	Simple scanning utility
Name:		simple-scan
Version:	3.14.2
Release:	1
License:	GPL v3+
Group:		Applications/Multimedia
Source0:	https://launchpad.net/simple-scan/3.14/%{version}/+download/%{name}-%{version}.tar.xz
# Source0-md5:	fa45b07aef08910d3c6435a2cb3a89ad
URL:		https://launchpad.net/simple-scan
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	cairo-devel
BuildRequires:	colord-devel
BuildRequires:	gdk-pixbuf2-devel
BuildRequires:	gettext-tools
BuildRequires:	glib2-devel >= 1:2.32.0
BuildRequires:	gnome-common
BuildRequires:	gnome-doc-utils
BuildRequires:	gtk+3-devel >= 3.0.0
BuildRequires:	intltool >= 0.40.0
BuildRequires:	libjpeg-devel
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(macros) >= 1.198
BuildRequires:	sane-backends-devel
BuildRequires:	udev-glib-devel
BuildRequires:	vala >= 2:0.22.0
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
%{__intltoolize}
%{__aclocal}
%{__autoconf}
%{__automake}
%configure \
	--disable-schemas-compile \
	--disable-silent-rules
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

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
%{_datadir}/appdata/simple-scan.appdata.xml
%{_datadir}/glib-2.0/schemas/org.gnome.SimpleScan.gschema.xml
%{_datadir}/simple-scan
