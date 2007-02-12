
%define short_name pgf
%define	texhash	[ ! -x %{_bindir}/texhash ] || %{_bindir}/texhash 1>&2 ;

# TODO:
# Pack more files ? (documentation sources as examples)

Summary:	The TeX Portable Graphic Format
Summary(pl.UTF-8):   Przenośny format grafiki dla TeXa
Name:		tetex-pgf
Version:	1.01
Release:	1
License:	LaTeX Project Public License
Group:		Applications/Publishing/TeX
Source0:	http://dl.sourceforge.net/latex-beamer/%{short_name}-%{version}.tar.gz
# Source0-md5:	0e9261dce4aa0f4ffef34fad75ae4e32
Requires:	tetex-latex
Requires:	tetex-latex-xcolor >= 2.00
Requires(post,postun):	/usr/bin/texhash
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A macro package for creating graphics directly in TeX and LaTeX.

%description -l pl.UTF-8
Pakiet makr do tworzenia grafiki bezpośrednio z TeXa i LaTeXa.

%prep
%setup -q -n %{short_name}-%{version}

%install
rm -rf $RPM_BUILD_ROOT

for SEC in generic latex plain; do
	cd $SEC/%{short_name}
	for DIR in *; do
		install -d $RPM_BUILD_ROOT%{_datadir}/texmf/tex/$SEC/%{short_name}/$DIR
		install $DIR/* $RPM_BUILD_ROOT%{_datadir}/texmf/tex/$SEC/%{short_name}/$DIR
	done
	cd ../..
done

%clean
rm -rf $RPM_BUILD_ROOT

%post
%texhash

%postun
%texhash

%files
%defattr(644,root,root,755)
%doc doc/generic/pgf/version-for-pdftex/en/pgfmanual.pdf  doc/generic/pgf/AUTHORS doc/generic/pgf/ChangeLog doc/generic/pgf/README doc/generic/pgf/TODO
%{_datadir}/texmf/tex/generic/%{short_name}
%{_datadir}/texmf/tex/latex/%{short_name}
%{_datadir}/texmf/tex/plain/%{short_name}
