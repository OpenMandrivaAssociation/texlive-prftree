%global tl_name prftree
%global tl_revision 77682

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.6
Release:	%{tl_revision}.1
Summary:	Macros for building proof trees
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/prftree
License:	gpl
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/prftree.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/prftree.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
A package to typeset proof trees for natural deduction calculi, sequent-
like calculi, and similar.

