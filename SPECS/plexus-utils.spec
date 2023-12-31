%bcond_with bootstrap

Name:           plexus-utils
Version:        3.3.0
Release:        10%{?dist}
Summary:        Plexus Common Utilities
# ASL 1.1: several files in src/main/java/org/codehaus/plexus/util/ 
# xpp: src/main/java/org/codehaus/plexus/util/xml/pull directory
# ASL 2.0 and BSD:
#      src/main/java/org/codehaus/plexus/util/cli/StreamConsumer
#      src/main/java/org/codehaus/plexus/util/cli/StreamPumper
#      src/main/java/org/codehaus/plexus/util/cli/Commandline            
# Public domain: src/main/java/org/codehaus/plexus/util/TypeFormat.java
# rest is ASL 2.0
License:        ASL 1.1 and ASL 2.0 and xpp and BSD and Public Domain
URL:            https://codehaus-plexus.github.io/plexus-utils/
BuildArch:      noarch
ExclusiveArch:  %{java_arches} noarch

Source0:        https://github.com/codehaus-plexus/%{name}/archive/%{name}-%{version}.tar.gz
Source1:        http://apache.org/licenses/LICENSE-2.0.txt

%if %{with bootstrap}
BuildRequires:  javapackages-bootstrap-openjdk8
%else
BuildRequires:  maven-local-openjdk8
BuildRequires:  mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires:  mvn(org.apache.maven.plugins:maven-enforcer-plugin)
BuildRequires:  mvn(org.codehaus.plexus:plexus:pom:)
%endif

%description
The Plexus project seeks to create end-to-end developer tools for
writing applications. At the core is the container, which can be
embedded or for a full scale application server. There are many
reusable components for hibernate, form processing, jndi, i18n,
velocity, etc. Plexus also includes an application server which
is like a J2EE application server, without all the baggage.

%{?javadoc_package}

%prep
%setup -q -n %{name}-%{name}-%{version}

cp %{SOURCE1} .

%mvn_file : plexus/utils
%mvn_alias : plexus:plexus-utils

# Generate OSGI info
%pom_xpath_inject "pom:project" "<packaging>bundle</packaging>"
%pom_xpath_inject "pom:build/pom:plugins" "
        <plugin>
          <groupId>org.apache.felix</groupId>
          <artifactId>maven-bundle-plugin</artifactId>
          <extensions>true</extensions>
          <configuration>
            <instructions>
              <_nouses>true</_nouses>
              <Export-Package>org.codehaus.plexus.util.*;org.codehaus.plexus.util.cli.*;org.codehaus.plexus.util.cli.shell.*;org.codehaus.plexus.util.dag.*;org.codehaus.plexus.util.introspection.*;org.codehaus.plexus.util.io.*;org.codehaus.plexus.util.reflection.*;org.codehaus.plexus.util.xml.*;org.codehaus.plexus.util.xml.pull.*</Export-Package>
            </instructions>
          </configuration>
        </plugin>"

%build
%mvn_build -f

%install
%mvn_install

%files -f .mfiles
%license NOTICE.txt LICENSE-2.0.txt

%changelog
* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Feb 05 2022 Jiri Vanek <jvanek@redhat.com> - 3.3.0-9
- Rebuilt for java-17-openjdk as system jdk

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Mon May 17 2021 Mikolaj Izdebski <mizdebsk@redhat.com> - 3.3.0-6
- Bootstrap build
- Non-bootstrap build

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sat Jul 11 2020 Jiri Vanek <jvanek@redhat.com> - 3.3.0-3
- Rebuilt for JDK-11, see https://fedoraproject.org/wiki/Changes/Java11

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jan 25 2020 Mikolaj Izdebski <mizdebsk@redhat.com> - 3.3.0-3
- Build with OpenJDK 8

* Tue Nov 05 2019 Mikolaj Izdebski <mizdebsk@redhat.com> - 3.3.0-2
- Mass rebuild for javapackages-tools 201902

* Wed Oct 23 2019 Marian Koncek <mkoncek@redhat.com> - 3.3.0-1
- Update to upstream verssion 3.3.0

* Wed Oct 16 2019 Fabio Valentini <decathorpe@gmail.com> - 3.3.0-1
- Update to version 3.3.0.

* Fri Oct 11 2019 Fabio Valentini <decathorpe@gmail.com> - 3.2.1-1
- Update to version 3.2.1.

* Mon Jul 29 2019 Marian Koncek <mkoncek@redhat.com> - 3.2.1-1
- Update to upstream version 3.2.1

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed Jul 03 2019 Fabio Valentini <decathorpe@gmail.com> - 3.2.0-1
- Update to version 3.2.0.

* Fri May 24 2019 Mikolaj Izdebski <mizdebsk@redhat.com> - 3.2.0-2
- Mass rebuild for javapackages-tools 201901

* Sat Apr 13 2019 Mikolaj Izdebski <mizdebsk@redhat.com> - 3.2.0-1
- Update to upstream version 3.2.0

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Jul 11 2018 Michael Simacek <msimacek@redhat.com> - 3.1.0-2
- Fix copy not following symlinks

* Mon Jun 25 2018 Michael Simacek <msimacek@redhat.com> - 3.1.0-1
- Update to upstream version 3.1.0

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.24-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.24-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.24-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Jun 15 2016 Mikolaj Izdebski <mizdebsk@redhat.com> - 3.0.24-2
- Add missing build-requires
- Update upstream URL

* Mon May  9 2016 Mikolaj Izdebski <mizdebsk@redhat.com> - 3.0.24-1
- Update to upstream version 3.0.24

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.22-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.0.22-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu Apr 09 2015 Michael Simacek <msimacek@redhat.com> - 3.0.22-1
- Update to upstream version 3.0.22

* Wed Apr  1 2015 Mikolaj Izdebski <mizdebsk@redhat.com> - 3.0.21-3
- Update upstream URL

* Mon Mar 30 2015 Michael Simacek <msimacek@redhat.com> - 3.0.21-2
- Don't use NioFiles.copy as it doesn't follow symlinks

* Tue Mar 24 2015 Michael Simacek <msimacek@redhat.com> - 3.0.21-1
- Update to upstream version 3.0.21

* Mon Sep 29 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 3.0.18-1
- Update to upstream version 3.0.18
- Update to current packaging guidelines

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.0.16-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue Mar 04 2014 Stanislav Ochotnicky <sochotnicky@redhat.com> - 3.0.16-2
- Use Requires: java-headless rebuild (#1067528)

* Mon Jan 27 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 3.0.16-1
- Update to upstream version 3.0.16

* Fri Aug  9 2013 Mikolaj Izdebski <mizdebsk@redhat.com> - 3.0.14-1
- Update to upstream version 3.0.14

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.0.9-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Tue Jul 23 2013 Mikolaj Izdebski <mizdebsk@redhat.com> - 3.0.9-6
- Generate OSGi metadata
- Resolves: rhbz#987117

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.0.9-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Feb 06 2013 Java SIG <java-devel@lists.fedoraproject.org> - 3.0.9-4
- Update for https://fedoraproject.org/wiki/Fedora_19_Maven_Rebuild
- Replace maven BuildRequires with maven-local

* Mon Nov 26 2012 Stanislav Ochotnicky <sochotnicky@redhat.com> - 3.0.9-3
- Add license from one Public Domain class 

* Fri Nov 23 2012 Stanislav Ochotnicky <sochotnicky@redhat.com> - 3.0.9-2
- Fix license tag and ASL 2.0 license text

* Wed Oct 10 2012 Alexander Kurtakov <akurtako@redhat.com> 3.0.9-1
- Update to upstream 3.0.9.

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Sep 7 2011 Alexander Kurtakov <akurtako@redhat.com> 3.0-1
- Update to upstream 3.0.

* Mon Feb 28 2011 Stanislav Ochotnicky <sochotnicky@redhat.com> - 2.0.6-1
- Update to 2.0.6
- Remove obsolete patches
- Use maven 3 to build

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Dec 16 2010 Stanislav Ochotnicky <sochotnicky@redhat.com> - 2.0.5-2
- Use versionless jars/javadocs
- Use new maven plugin names
- Add compatibility depmap

* Wed May  5 2010 Mary Ellen Foster <mefoster at gmail.com> 2.0.5-1
- Update to 2.0.5

* Fri Feb 12 2010 Mary Ellen Foster <mefoster at gmail.com> 2.0.1-1
- Update to 2.0.1
- Build with maven

* Wed Aug 19 2009 Andrew Overholt <overholt@redhat.com> 1.4.5-1.2
- Update to 1.4.5 from JPackage and Deepak Bhole
- Remove gcj bits

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0:1.2-4.2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0:1.2-3.2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Wed Jul  9 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 0:1.2-2.2
- fix license tag
- drop repotag

* Thu Aug 23 2007 Ralph Apel <r.apel@r-apel.de> - 0:1.4.5-1jpp
- Upgrade to 1.4.5
- Now build with maven2 by default

* Wed Mar 21 2007 Ralph Apel <r.apel@r-apel.de> - 0:1.2-2jpp
- Fix build classpath
- Optionally build with maven2
- Add gcj_support option

* Mon Feb 20 2007 Deepak Bhole <dbhole@redhat.com> - 0:1.2-2jpp.1.fc7
- Fix spec per Fedora guidelines

* Fri Jun 16 2006 Ralph Apel <r.apel@r-apel.de> - 0:1.2-1jpp
- Upgrade to 1.2

* Wed Jan 04 2006 Fernando Nasser <fnasser@redhat.com> - 0:1.0.4-2jpp
- First JPP 1.7 build

* Mon Nov 07 2005 Ralph Apel <r.apel at r-apel.de> - 0:1.0.4-1jpp
- First JPackage build
