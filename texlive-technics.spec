# revision 16238
# category Package
# catalog-ctan /macros/latex/contrib/technics
# catalog-date 2007-01-16 00:15:12 +0100
# catalog-license lppl
# catalog-version undef
Name:		texlive-technics
Version:	20070116
Release:	1
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
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3

%description
TeXLive technics package.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
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
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
