%global realname	ArcMenu
%global uuid		arcmenu@arcmenu.com
%global realnamel	arcmenu

Summary:	Gnome shell extension designed to replace the standard menu
Name:		gnome-shell-extension-arcmenu
Version:	68.0
Release:	1%{dist}

License:	GPLv2
URL:		https://gitlab.com/arcmenu/ArcMenu/
Source0:	https://gitlab.com/arcmenu/ArcMenu/-/archive/v%{version}/ArcMenu-v%{version}.tar.bz2

BuildArch:	noarch

BuildRequires:	fdupes
BuildRequires:	git
BuildRequires:	glib2
BuildRequires:	gettext
BuildRequires:  make
BuildRequires:  glib2-devel

Requires:	gnome-shell-extension-common
Requires:	gnome-menus

%description
Arc Menu is a Gnome shell extension designed to replace the standard menu found
in Gnome 3 this application menu extension has some added benefits over the
standard menu found in Gnome 3, these include the long awaited search
functionality as well as quick access to files on your system and also the
current logged in user along with quick access to the software centre and
system settings and other features which can be accessed from the settings
menu.

%prep
%autosetup -n %{realname}-v%{version} -p1

%build
%make_build

%install
%make_install INSTALL=system
%fdupes -s %{buildroot}

rm -f %{buildroot}%{_datadir}/gnome-shell/extensions/%{uuid}/COPYING
rm -f %{buildroot}%{_datadir}/gnome-shell/extensions/%{uuid}/README.md
rm -rf %{buildroot}%{_datadir}/gnome-shell/extensions/arcmenu@arcmenu.com/media/.keep

# fix mod
find %{buildroot} -type f -exec chmod 644 {} \;

mkdir -p %{buildroot}%{_datadir}/pixmaps/

%find_lang %{realnamel} --with-gnome

%files -f %{realnamel}.lang
%doc README.md
%{_datadir}/glib-2.0/schemas/org.gnome.shell.extensions.arcmenu.gschema.xml
%{_datadir}/gnome-shell/extensions/%{uuid}

%changelog
* Tue Feb 24 2026 Shaun Assam <sassam@fedoraproject.org> - 68.0
- Rebuilt for EPEL 10

* Mon Dec 22 2025 Arkady L. Shane <tigro@msvsphere-os.ru> - 67.2-2
- Rebuilt for Fedora

* Fri Nov 21 2025 Arkady L. Shane <tigro@msvsphere-os.ru> - 67.2-1.inferit.2
- Set chromium and ptyxis by default

* Mon Oct 20 2025 Arkady L. Shane <tigro@msvsphere-os.ru> - 67.2-1.inferit.1
- Fix border radius

* Mon Oct 20 2025 Arkady L. Shane <tigro@msvsphere-os.ru> - 67.2-1.inferit
- Update to 67.2 version

* Tue Apr 22 2025 Ernest Ershov <ernest.ershov@softline.com> - 63-3.inferit
- Add Eugene Zamriy's patch to make icons executable and make extension compatible with Desktop Icons NG

* Tue Dec 24 2024 Arkady L. Shane <tigro@msvsphere-os.ru> - 63-3
- Added Chromium and Terminal to favorites
- Fix menu border
- Bump menus size

* Tue Dec 24 2024 Arkady L. Shane <tigro@msvsphere-os.ru> - 63-2
- Set 48 px size for Menu icon
- Disable open menu shortcut

* Mon Dec 23 2024 Arkady L. Shane <tigro@msvsphere-os.ru> - 63-1
- Update to v63

* Fri Oct 27 2023 Arkady L. Shane <tigro@msvsphere-os.ru> - 27-9
- Read system name from MSVSPHERE_PRETTY_NAME

* Thu Sep  7 2023 Arkady L. Shane <ashejn@msvsphere.ru> - 27-8
- Added MSVSphere symbolic icon
- Use main icon from sphere-logos

* Wed Sep  6 2023 Arkady L. Shane <ashejn@msvsphere.ru> - 27-7
- Added monochrome icon

* Mon Sep  4 2023 Arkady L. Shane <ashejn@msvsphere.ru> - 27-6
- Display on all monitors
- Set a hotkey (Super-X) to open ArcMenu

* Wed Aug 23 2023 Arkady L. Shane <ashejn@msvsphere.ru> - 27-5
- Update menu icon again

* Tue Aug 22 2023 Arkady L. Shane <ashejn@msvsphere.ru> - 27-4
- Update menu icon

* Mon Aug 21 2023 Arkady L. Shane <ashejn@msvsphere.ru> - 27-3
- Added menu icon

* Wed Aug  9 2023 Arkady L. Shane <ashejn@msvsphere.ru> - 27-2
- Change Menu icon

* Sun Jun 25 2023 Arkady L. Shane <ashejn@msvsphere.ru> - 27-1
- initial build for MSVSphere 9.2
