# revision 29349
# category Package
# catalog-ctan /macros/latex/contrib/technics
# catalog-date 2012-08-31 01:04:09 +0200
# catalog-license lppl
# catalog-version 1.0
Name:		texlive-technics
Epoch:		1
Version:	1.0
Release:	6
Summary:	A package to format technical documents
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/technics
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/technics.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/technics.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package provides a very simple LaTeX document template, in
the hope that this use of LaTeX will become attractive to
typical word processor users. (Presentation is as if it were a
class; users are expected to start from a template document.).

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/technics/technics.sty
%doc %{_texmfdistdir}/doc/latex/technics/png2eps.sh
%doc %{_texmfdistdir}/doc/latex/technics/rf-logo.zip
%doc %{_texmfdistdir}/doc/latex/technics/technics.pdf
%doc %{_texmfdistdir}/doc/latex/technics/technics.tex
%doc %{_texmfdistdir}/doc/latex/technics/view-dvi.sh
%doc %{_texmfdistdir}/doc/latex/technics/vmlinux.eps
%doc %{_texmfdistdir}/doc/latex/technics/vmlinux.png

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
