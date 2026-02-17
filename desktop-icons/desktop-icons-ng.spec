%global extid   %{extname}@rastersoft.com
%global extname ding
%global extname_full desktop-icons-ng
%global uuid    org.gnome.shell.extensions.%{extname}

Name:           gnome-shell-extension-%{extname_full}
Version:        49.0.5
Release:        1%{?dist}
Summary:        GNOME Shell extension (next gen) for providing desktop icons

License:        GPLv3+
URL:            https://gitlab.com/rastersoft/desktop-icons-ng
Source0:        %{url}/-/archive/%{version}/desktop-icons-ng-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  gobject-introspection
BuildRequires:  intltool
BuildRequires:  meson

Requires:       gnome-shell >= 47

%description
This package provides a GNOME Shell extension for showing the contents of
~/Desktop on the desktop of the Shell. Common file management operations such as
launching, copy/paste, rename and deleting are supported.

You can use gnome-tweaks (additional package) or run in terminal:

  gnome-extensions enable %{extid}


%prep
%autosetup -n %{extname_full}-%{version}
rm -rf apparmor
sed -i '35,37d' meson.build
sed "s/print('Reloading apparmor rules...')/print('Reloading...')/" meson_post_install.py
sed "s/subprocess.call(['systemctl', 'reload', 'apparmor'])/subprocess.call(['systemctl', 'reload'])/" meson_post_install.py
sed -e "/meson_post_install/d" -i meson.build


%build
%meson --localedir=%{_datadir}/locale
%meson_build


%install
%meson_install
%find_lang %{extname}


%files -f %{extname}.lang
#%license LICENSE
%doc README.md
%{_datadir}/glib-2.0/schemas/%{uuid}.gschema.xml
%{_datadir}/gnome-shell/extensions/%{extid}/


%changelog
* Thu Jan 29 2026 Shaun Assam <sassam@fedoraproject.org> - 49.0.5
- Updated and rebuilt for EPEL 10