Summary:	A spelling checker/corrector for Unicode-encoded dictionaries
Summary(pl):	Program sprawdzaj±cy/poprawiaj±cy pisowniê dla s³owników w Unikodzie
Name:		uspell
Version:	1.1.1
%define		snap	20031030
Release:	0.%{snap}.2
License:	GPL
Group:		Libraries
# -d :pserver:anoncvs:anoncvs@anoncvs.abisource.com:/cvsroot uspell
Source0:	%{name}-%{snap}.tar.bz2
# Source0-md5:	f50edc2a6228dd3f7e03dc72b9e7fb46
Patch0:		%{name}-gcc4.patch
# not exactly uspell homepage, but contains a little information
URL:		http://www.abisource.com/enchant/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libstdc++-devel
BuildRequires:	libtool >= 2:1.4d
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Uspell is a spelling checker/corrector for Unicode-encoded
dictionaries, primarily for Yiddish, Hebrew, and Eastern European
languages.

%description -l pl
Uspell to program i biblioteka do kontroli i poprawiania pisowni dla
s³owników zakodowanych w Unikodzie, g³ównie dla jêzyków jidysz,
hebrajskiego oraz wschodnioeuropejskich.

%package devel
Summary:	Header files for uspell library
Summary(pl):	Pliki nag³ówkowe biblioteki uspell
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	libstdc++-devel

%description devel
Header files for uspell library.

%description devel -l pl
Pliki nag³ówkowe biblioteki uspell.

%package static
Summary:	Static uspell library
Summary(pl):	Statyczna biblioteka uspell
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static uspell library.

%description static -l pl
Statyczna biblioteka uspell.

%package en_US
Summary:	American English dictionary (word list) for uspell
Summary(pl):	Angielski s³ownik (lista s³ów) dla uspella
Group:		Applications/Text
Requires:	%{name} = %{version}-%{release}

%description en_US
American English dictionary (word list) for uspell. It's a
concatenation from scowl-5 English and American lists, with
case-insensitive words capitalized. See
<http://wordlist.sourceforge.net/>.

%description en_US -l pl
Ten pakiet zawiera s³ownik (listê s³ów) angielski w odmianie
amerykañskiej dla uspella. Jest to po³±czenie list English i American
ze scowl-5, ze s³owami nie wymagaj±cymi pisania wielk± liter±
przerobionymi w ca³o¶ci na wielkie litery. Wiêcej informacji na
stronie <http://wordlist.sourceforge.net/>.

%package he
Summary:	Hebrew dictionary (word list) for uspell
Summary(pl):	Hebrajski s³ownik (lista s³ów) dla uspella
Group:		Applications/Text
Requires:	%{name} = %{version}-%{release}

%description he
Hebrew dictionary (word list) for uspell. It comes from the hspell
source.

%description he -l pl
Hebrajski s³ownik (lista s³ów) dla uspella. Pochodzi ze ¼róde³
hspella.

%package yi
Summary:	Yiddish dictionary (word list) for uspell
Summary(pl):	S³ownik (lista s³ow) jêzyka jidysz dla uspella
Group:		Applications/Text
Requires:	%{name} = %{version}-%{release}

%description yi
Yiddish dictionary (word list) for uspell. It comes from Raphael
Finkel's personal word list.

%description yi -l pl
S³ownik (lista s³ow) jêzyka jidysz dla uspella. Pochodzi z w³asnej
listy s³ów Raphaela Finkela.

%prep
%setup -q -n %{name}
%patch0 -p1

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# missing from dict_DATA
install dic/american.* $RPM_BUILD_ROOT%{_datadir}/uspell

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc doc/doc.txt
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_libdir}/lib*.so.*.*.*
%dir %{_datadir}/uspell

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so
%{_libdir}/lib*.la
%{_includedir}/uspell
%{_pkgconfigdir}/*.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a

%files en_US
%defattr(644,root,root,755)
%{_datadir}/uspell/american.uspell.*

%files he
%defattr(644,root,root,755)
%{_datadir}/uspell/hebrew.uspell.*

%files yi
%defattr(644,root,root,755)
%{_datadir}/uspell/yiddish.uspell.*
