
%define		_name	qinx

Summary:	KDE theme - %{_name}
Summary(pl):	Motyw KDE - %{_name}
Name:		kde-theme-%{_name}
Version:	1.4
Release:	1
License:	X11
Group:		Themes
Source0:	http://www.kde-look.org/content/files/2306-%{_name}-%{version}.tar.bz2
# Source0-md5:	316956de0067e3560e89ac02a7e863b8
Patch0:		%{_name}-unsermake.patch
URL:		http://www.kde-look.org/content/show.php?content=2306
BuildRequires:	autoconf
BuildRequires:	unsermake
BuildRequires:	automake
BuildRequires:	kdelibs-devel >= 9:3.2.0
BuildRequires:	kdebase-desktop-libs >= 9:3.2.0
Requires:	kde-decoration-%{_name}
Requires:	kde-style-%{_name}
Requires:	kde-colorscheme-%{_name}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Qinx is a clone of the Photon theme known from the QNX operating
system. It gives the user a clean and useful look with and concave
looking widgets.

%description -l pl
Qinx to kopia motywu Photon znanego z systemu operacyjnego QNX.
Oferuje on u¿ytkownikowi przejrzysty i funkcjonalny wygl±d oraz
poczucie wklês³o¶ci elementów interfejsu graficznego.

%package -n kde-style-%{_name}
Summary:	KDE style - %{_name}
Summary(pl):	Styl do KDE - %{_name}
Group:		Themes
Requires:	kdelibs

%description -n kde-style-%{_name}
Qinx is a clone of the Photon style known from the QNX operating
system. It gives the user a clean and useful look with and concave
looking widgets.

%description -n kde-style-%{_name} -l pl
Qinx to kopia stylu Photon znanego z systemu operacyjnego QNX. Oferuje
on u¿ytkownikowi przejrzysty i funkcjonalny wygl±d oraz poczucie
wklês³o¶ci elementów interfejsu graficznego.

%package -n kde-colorscheme-%{_name}
Summary:	Color scheme for KDE style - %{_name}
Summary(pl):	Schemat kolorów do stylu KDE - %{_name}
Group:		Themes
Requires:	kdebase-core

%description -n kde-colorscheme-%{_name}
This package contains two color schemes for KDE. One of them creates a
modern, blue look and the second a combined blue and grey look with a
lesser contrast.

%description -n kde-colorscheme-%{_name} -l pl
Ten pakiet zawiera dwa schematy kolorów dla KDE. Jeden z nich tworzy
nowoczesny, niebieski wygl±d, a drugi ³±czy kolory niebieski i szary,
tworz±c wygl±d o mniejszym kontra¶cie.

%package -n kde-decoration-%{_name}
Summary:	Kwin decoration - %{_name}
Summary(pl):	Dekoracja kwin - %{_name}
Group:		Themes
Requires:	kdebase-desktop-libs >= 9:3.2.0

%description -n kde-decoration-%{_name}
Tis package contains a kwin decoration similar to the one used in
Photon from the QNX operating system. It consists of a convex space
for window titles and concave space for window buttons, which makes
the whole decoration clear and visible.

%description -n kde-decoration-%{_name} -l pl
Ten pakiet zawiera dekoracje kwin podobn± do tej u¿ywanej w Photonie,
stylu znanym z systemu operacyjnego QNX. Sk³ada siê z wypuk³ej czê¶ci
zawieraj±cej tytu³ okna oraz wklês³ej, w której znajduj± siê
przyciski, co sprawia, ¿e ca³a dekoracja jest wyra¼na i widoczna.

%prep
%setup -q -n %{_name}-%{version}
%patch0 -p1

%build
cp -f %{_datadir}/automake/config.sub admin
export UNSERMAKE=%{_datadir}/unsermake/unsermake
%{__make} -f Makefile.cvs

%configure \
	--with-qt-libraries=%{_libdir}

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	kde_htmldir="%{_kdedocdir}"

%clean
rm -rf $RPM_BUILD_ROOT

%files

%files -n kde-decoration-%{_name}
%defattr(644,root,root,755)
%{_libdir}/kde3/kwin*.la
%attr(755,root,root) %{_libdir}/kde3/kwin*.so
%{_datadir}/apps/kwin/*.desktop

%files -n kde-style-%{_name}
%defattr(644,root,root,755)
%{_libdir}/kde3/kstyle_*.la
%attr(755,root,root) %{_libdir}/kde3/kstyle_*.so
%{_libdir}/kde3/plugins/styles/*.la
%attr(755,root,root) %{_libdir}/kde3/plugins/styles/*.so
%{_datadir}/apps/kstyle/themes/*.themerc

%files -n kde-colorscheme-%{_name}
%defattr(644,root,root,755)
%{_datadir}/apps/kdisplay/color-schemes/*.kcsrc
