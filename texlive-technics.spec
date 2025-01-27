Name:		texlive-technics
Epoch:		1
Version:	29349
Release:	2
Summary:	A package to format technical documents
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/technics
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/technics.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/technics.doc.r%{version}.tar.xz
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
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
