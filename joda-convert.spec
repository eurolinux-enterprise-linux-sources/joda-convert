Name:           joda-convert
Version:        1.3
Release:        4%{?dist}
Summary:        Java library for conversion to and from standard string formats
License:        ASL 2.0 
URL:            https://github.com/JodaOrg/joda-convert/
Source0:        https://github.com/JodaOrg/joda-convert/tarball/v1.3#/joda-convert-1.3.tar.gz
BuildArch:      noarch

BuildRequires:  maven-local

%description
Java library to enable conversion to and from standard string formats.

%package javadoc
Summary:        Javadocs for %{name}

%description javadoc
This package contains the API documentation for %{name}.

%prep
%setup -q -n JodaOrg-joda-convert-df6d6c9
%mvn_file : %{name}
sed -i s/// LICENSE.txt NOTICE.txt RELEASE-NOTES.txt

%build
%mvn_build

%install
%mvn_install

%files -f .mfiles
%doc LICENSE.txt NOTICE.txt RELEASE-NOTES.txt

%files javadoc -f .mfiles-javadoc
%doc LICENSE.txt NOTICE.txt

%changelog
* Tue Aug 27 2013 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.3-4
- Migrate away from mvn-rpmbuild

* Fri Jun 28 2013 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.3-3
- Rebuild to regenerate API documentation
- Resolves: CVE-2013-1571

* Tue May 28 2013 Stanislav Ochotnicky <sochotnicky@redhat.com> - 1.3-2
- Install NOTICE file with javadoc as well
- Use full URL for Source0

* Fri Feb 22 2013 Andy Grimm <agrimm@gmail.com> - 1.3-1
- Update to 1.3

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Feb 06 2013 Java SIG <java-devel@lists.fedoraproject.org> - 1.2-4
- Update for https://fedoraproject.org/wiki/Fedora_19_Maven_Rebuild
- Replace maven BuildRequires with maven-local

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Thu Nov 17 2011 Andy Grimm <agrimm@gmail.com> - 1.2-1
- update to 1.2 and pull source tarball correctly

* Tue Oct 18 2011 Andy Grimm <agrimm@gmail.com> - 1.1-1
- Initial package
