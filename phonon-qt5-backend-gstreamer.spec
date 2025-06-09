%define		phonon_ver	4.10.60
%define		qt_ver		5.2.0

Summary:	GStreamer backend for Qt5 Phonon
Summary(pl.UTF-8):	Wtyczka GStreamera dla Phonona opartego na Qt5
Name:		phonon-qt5-backend-gstreamer
Version:	4.10.0
Release:	1
License:	LGPL 2.1
Group:		Libraries
Source0:	https://download.kde.org/Attic/phonon/phonon-backend-gstreamer/%{version}/phonon-backend-gstreamer-%{version}.tar.xz
# Source0-md5:	60abf634e961160cd1772d486f4a7097
BuildRequires:	OpenGL-devel
BuildRequires:	Qt5Core-devel >= %{qt_ver}
BuildRequires:	Qt5Gui-devel >= %{qt_ver}
BuildRequires:	Qt5OpenGL-devel >= %{qt_ver}
BuildRequires:	Qt5Widgets-devel >= %{qt_ver}
BuildRequires:	Qt5X11Extras-devel >= %{qt_ver}
BuildRequires:	cmake >= 3.5
BuildRequires:	glib2-devel >= 2.0
BuildRequires:	gstreamer-devel >= 1.0
BuildRequires:	gstreamer-plugins-base-devel >= 1.0
BuildRequires:	kf5-extra-cmake-modules >= 5.60
BuildRequires:	libxml2-devel >= 2
BuildRequires:	pkgconfig
BuildRequires:	qt5-build >= %{qt_ver}
BuildRequires:	qt5-linguist >= %{qt_ver}
BuildRequires:	rpmbuild(macros) >= 1.605
BuildRequires:	sed >= 4.0
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
BuildRequires:	phonon-qt5-devel >= %{phonon_ver}
BuildRequires:	qt5-build >= %{qt_ver}
BuildRequires:	qt5-qmake >= %{qt_ver}
Requires:	Qt5Core >= %{qt_ver}
Requires:	Qt5Gui >= %{qt_ver}
Requires:	Qt5OpenGL >= %{qt_ver}
Requires:	Qt5Widgets >= %{qt_ver}
Requires:	Qt5X11Extras >= %{qt_ver}
Requires:	phonon-qt5 >= %{phonon_ver}
Suggests:	gstreamer-pulseaudio >= 1.0
Provides:	phonon-qt5-backend = %{version}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
GStreamer backend for Qt5 Phonon.

%description -l pl.UTF-8
Wtyczka GStreamera dla Phonona opartego na Qt5.

%prep
%setup -q -n phonon-backend-gstreamer-%{version}

%build
install -d build-qt5
cd build-qt5
%cmake .. \
	-DKDE_INSTALL_USE_QT_SYS_PATHS=ON \
	-DPHONON_BUILD_PHONON4QT5=ON

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C build-qt5 install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang phonon_gstreamer_qt --with-qm

%clean
rm -rf $RPM_BUILD_ROOT

%files -f phonon_gstreamer_qt.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/qt5/plugins/phonon4qt5_backend/phonon_gstreamer.so
%{_iconsdir}/hicolor/*x*/apps/phonon-gstreamer.png
%{_iconsdir}/hicolor/scalable/apps/phonon-gstreamer.svg
