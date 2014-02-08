# revision 16238
# category Package
# catalog-ctan /macros/latex/contrib/technics
# catalog-date 2007-01-16 00:15:12 +0100
# catalog-license lppl
# catalog-version undef
Name:		texlive-technics
Version:	20070116
Release:	3
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
TeXLive technics package.

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


%changelog
* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 20070116-2
+ Revision: 756550
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 20070116-1
+ Revision: 719663
- texlive-technics
- texlive-technics
- texlive-technics

