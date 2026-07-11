%global tl_name technics
%global tl_revision 79618

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.0
Release:	%{tl_revision}.1
Summary:	A package to format technical documents
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/technics
License:	lppl1
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/technics.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/technics.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package provides a very simple LaTeX document template, in the hope
that this use of LaTeX will become attractive to typical word processor
users. (Presentation is as if it were a class; users are expected to
start from a template document.)

