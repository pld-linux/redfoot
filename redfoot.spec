%include	/usr/lib/rpm/macros.python
Summary:	Redfoot - a program for managing and sharing information
Summary(pl):	Redfoot - program do zarz�dzania i dzielenia informacji
Name:		redfoot
Version:	1.8.0
Release:	1
License:	BSD
Vendor:		Robin Dunn <robin@alldunn.com>
Group:		Development/Languages/Python
Source0:	http://redfoot.net/2003/01/06/%{name}-%{version}.tgz
# Source0-md5:	4c707fdfd0977be9518a8932a7be86a2
URL:		http://redfoot.net/
BuildRequires:	python-devel >= 2.3
BuildRequires:	rpm-pythonprov
%pyrequires_eq	python-modules
Requires:	python-medusa
Requires:	python-rdflib = 1.2.4
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Redfoot is a program for managing and sharing information. Redfoot is
currently geared mostly to the developer, but is shifting in the
direction of the end user.

Redfoot makes extensive use of RDF and is written in Python. Redfoot's
vision has much in common with that of the Semantic Web. Eventually 
there will be a P2P network of Redfeet ;)

Redfoot utilizes RDFLib and is currently being developed by Daniel
Krech.

%description -l pl
Redfoot to program do zarz�dzania i dzielenia informacji. Jest
aktualnie dostosowany g��wnie pod k�tem programist�w, ale zmienia
kierunek na u�ytkownika ko�cowego.

Redfoot intensywnie u�ywa RDF i jest napisany w Pythonie. Wizja
Redfoota ma wiele wsp�lnego z wizj� Semantic Web. By� mo�e b�dzie sie�
P2P Redfoot�w ;)

Redfoot wykorzystuje RDFLib i jest aktualnie rozwijany przez Daniela
Krecha.

%prep
%setup -q

%build
env CFLAGS="%{rpmcflags}" python setup.py build

%install
rm -rf $RPM_BUILD_ROOT

python -- setup.py install \
	--root=$RPM_BUILD_ROOT \
	--optimize=2

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README LICENSE CHANGELOG doc index.html credits.html sample_pages.rdf
%attr(755,root,root) %{_bindir}/%{name}.py
