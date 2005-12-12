
%define short_name pgf
%define	texhash	[ ! -x %{_bindir}/texhash ] || %{_bindir}/texhash 1>&2 ;

# TODO:
# Pack more files ? (plain subdirectory)

Summary:	The TeX Portable Graphic Format
Summary(pl):	Przeno¶ny format grafiki dla TeXa
Name:		tetex-pgf
Version:	0.95
Release:	1
License:	LaTeX Project Public License
Group:		Applications/Publishing/TeX
Source0:	http://dl.sourceforge.net/latex-beamer/%{short_name}-%{version}.tar.gz
# Source0-md5:	342549f27785cc6466a02cb66774e4cf
Requires:	tetex-latex
Requires:	tetex-latex-xcolor >= 2.00
Requires(post,postun):	/usr/bin/texhash
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A macro package for creating graphics directly in TeX and LaTeX.

%description
Pakiet makr do tworzenia grafiki bezpo¶rednio z TeXa i LaTeXa.

%prep
%setup -q -n %{short_name}-%{version}

%install
rm -rf $RPM_BUILD_ROOT

for SEC in generic latex; do
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
%doc doc/pgf/en/*.pdf doc/pgf/AUTHORS doc/pgf/ChangeLog doc/pgf/README doc/pgf/TODO
%{_datadir}/texmf/tex/generic/%{short_name}
%{_datadir}/texmf/tex/latex/%{short_name}
