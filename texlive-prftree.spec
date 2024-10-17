Name:		texlive-prftree
Version:	54080
Release:	2
Summary:	Macros for building proof trees
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/prftree
License:	gpl
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/prftree.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/prftree.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
A package to typeset proof trees for natural deduction calculi,
sequent-like calculi, and similar.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/latex/prftree
%doc %{_texmfdistdir}/doc/latex/prftree

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
