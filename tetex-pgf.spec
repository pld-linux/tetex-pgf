
%define short_name pgf
%define	texhash	[ ! -x %{_bindir}/texhash ] || %{_bindir}/texhash 1>&2 ;

Summary:	The TeX Portable Graphic Format
Summary(pl):	Przeno¶ny format grafiki dla TeXa
Name:		tetex-pgf
Version:	0.65
Release:	1
License:	LaTeX Project Public License
Group:		Applications/Publishing/TeX
Source0:	http://dl.sourceforge.net/latex-beamer/%{short_name}-%{version}.tar.gz
# Source0-md5:	763cab72b1a46160da5e40b6892db6a1
Requires:	tetex-latex
Requires:	tetex-latex-xcolor >= 2.00
Requires(post,postun):	/usr/bin/texhash
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A macro package for creating graphics directly in TeX and LaTeX.

%description
Pakiet makr do tworzenia grafiki bezpo¶rednio z TeXa i LaTeXa.

%prep
%setup -q -n %{short_name}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}/texmf/tex/%{short_name}

install *.sty $RPM_BUILD_ROOT%{_datadir}/texmf/tex/%{short_name}

%clean
rm -rf $RPM_BUILD_ROOT

%post
%texhash

%postun
%texhash

%files
%defattr(644,root,root,755)
%doc *.pdf
%{_datadir}/texmf/tex/%{short_name}
