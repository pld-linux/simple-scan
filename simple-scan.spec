Summary:	Simple scanning utility
Name:		simple-scan
Version:	2.32.0.1
Release:	1
License:	GPL v3+
Group:		Applications/Multimedia
Source0:	http://ftp.gnome.org/pub/GNOME/sources/simple-scan/2.32/%{name}-%{version}.tar.bz2
# Source0-md5:	9c0682f1aa6b338222b973fec6162e87
URL:		https://launchpad.net/simple-scan
BuildRequires:	GConf2-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	dbus-glib-devel
BuildRequires:	gettext-devel
BuildRequires:	gnome-common
BuildRequires:	gnome-doc-utils
BuildRequires:	gtk+2-devel >= 2:2.18.0
BuildRequires:	intltool >= 0.40.0
BuildRequires:	libjpeg-devel
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(macros) >= 1.198
BuildRequires:	sane-backends-devel
BuildRequires:	udev-glib-devel
BuildRequires:	zlib-devel
Requires(post,preun):	GConf2
Requires:	gnome-icon-theme
Requires:	xdg-utils
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
	--disable-schemas-install \
	--disable-silent-rules
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name} --with-gnome

%post
%gconf_schema_install simple-scan.schemas

%preun
%gconf_schema_uninstall simple-scan.schemas

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS README ChangeLog
%attr(755,root,root) %{_bindir}/simple-scan
%{_mandir}/man1/simple-scan.1*
%{_sysconfdir}/gconf/schemas/simple-scan.schemas
%{_desktopdir}/simple-scan.desktop
%{_datadir}/simple-scan
