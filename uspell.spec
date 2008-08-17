Summary:	A spelling checker/corrector for Unicode-encoded dictionaries
Summary(pl.UTF-8):	Program sprawdzający/poprawiający pisownię dla słowników w Unikodzie
Name:		uspell
Version:	1.1.1
%define		snap	20031030
Release:	0.%{snap}.3
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

%description -l pl.UTF-8
Uspell to program i biblioteka do kontroli i poprawiania pisowni dla
słowników zakodowanych w Unikodzie, głównie dla języków jidysz,
hebrajskiego oraz wschodnioeuropejskich.

%package devel
Summary:	Header files for uspell library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki uspell
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	libstdc++-devel

%description devel
Header files for uspell library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki uspell.

%package static
Summary:	Static uspell library
Summary(pl.UTF-8):	Statyczna biblioteka uspell
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static uspell library.

%description static -l pl.UTF-8
Statyczna biblioteka uspell.

%package en_US
Summary:	American English dictionary (word list) for uspell
Summary(pl.UTF-8):	Angielski słownik (lista słów) dla uspella
Group:		Applications/Text
Requires:	%{name} = %{version}-%{release}

%description en_US
American English dictionary (word list) for uspell. It's a
concatenation from scowl-5 English and American lists, with
case-insensitive words capitalized. See
<http://wordlist.sourceforge.net/>.

%description en_US -l pl.UTF-8
Ten pakiet zawiera słownik (listę słów) angielski w odmianie
amerykańskiej dla uspella. Jest to połączenie list English i American
ze scowl-5, ze słowami nie wymagającymi pisania wielką literą
przerobionymi w całości na wielkie litery. Więcej informacji na
stronie <http://wordlist.sourceforge.net/>.

%package he
Summary:	Hebrew dictionary (word list) for uspell
Summary(pl.UTF-8):	Hebrajski słownik (lista słów) dla uspella
Group:		Applications/Text
Requires:	%{name} = %{version}-%{release}

%description he
Hebrew dictionary (word list) for uspell. It comes from the hspell
source.

%description he -l pl.UTF-8
Hebrajski słownik (lista słów) dla uspella. Pochodzi ze źródeł
hspella.

%package yi
Summary:	Yiddish dictionary (word list) for uspell
Summary(pl.UTF-8):	Słownik (lista słow) języka jidysz dla uspella
Group:		Applications/Text
Requires:	%{name} = %{version}-%{release}

%description yi
Yiddish dictionary (word list) for uspell. It comes from Raphael
Finkel's personal word list.

%description yi -l pl.UTF-8
Słownik (lista słow) języka jidysz dla uspella. Pochodzi z własnej
listy słów Raphaela Finkela.

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
%attr(755,root,root) %{_bindir}/udriver
%attr(755,root,root) %{_libdir}/libuspell.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libuspell.so.1
%dir %{_datadir}/uspell

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libuspell.so
%{_libdir}/libuspell.la
%{_includedir}/uspell
%{_pkgconfigdir}/libuspell.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/libuspell.a

%files en_US
%defattr(644,root,root,755)
%{_datadir}/uspell/american.uspell.*

%files he
%defattr(644,root,root,755)
%{_datadir}/uspell/hebrew.uspell.*

%files yi
%defattr(644,root,root,755)
%{_datadir}/uspell/yiddish.uspell.*
