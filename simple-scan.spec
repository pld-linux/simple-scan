Summary:	Simple scanning utility
Name:		simple-scan
Version:	2.31.1
Release:	1
License:	GPLv3+
Group:		Applications/Multimedia
Source0:	http://launchpad.net/simple-scan/trunk/%{version}/+download/%{name}-%{version}.tar.gz
# Source0-md5:	6e37cf889ce147e22a9130348c2e929d
URL:		https://launchpad.net/simple-scan
BuildRequires:	automake
BuildRequires:	intltool
BuildRequires:	GConf2-devel
BuildRequires:	autoconf
BuildRequires:	cairo-devel
BuildRequires:	dbus-glib-devel
BuildRequires:	glib2-devel
BuildRequires:	gnome-doc-utils
BuildRequires:	gtk+2-devel
BuildRequires:	sane-backends-devel
BuildRequires:	udev-glib-devel
Requires(post,preun):	GConf2
Requires:	gnome-icon-theme
Requires:	xdg-utils

%description
Simple Scan is an easy-to-use application, designed to let users
connect their scanner and quickly have the image/document in an
appropriate format.

%prep
%setup -q

%build
%configure \
	--disable-schemas-install
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
%{_mandir}/man1/simple-scan.1*
%{_sysconfdir}/gconf/schemas/simple-scan.schemas
%attr(755,root,root) %{_bindir}/simple-scan
%{_desktopdir}/simple-scan.desktop
%{_datadir}/simple-scan/
