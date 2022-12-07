:warning: ⛔️ **Pulp2 is EOL as of November 30 2022, for more info visit this link https://pulpproject.org/2022/09/19/pulp-2-eol/.** ⛔️


# Pulp Packaging

## Adding a nightly built package

To add a new project to be built nightly, add a new entry under pulp_packages in `package_manifest.yaml`

```yaml
my-new-package:
      git: "{git url}"
```

1. Create a directory for the spec `packages/my-new-package/`
2. Download/create a spec file in the above folder 
3. run ansible-playbook nightlies.yaml -l my-new-package

Tito is configured to checkout this project and generate a source tarball to be used with the spec file under 
packages/project-name

## Updating a Dependency

To add a new dependency, start by adding an entry to `package_manifest.yml` in the appropriate section.
```yaml
my-new-package:
  files:
    - "my-new-package-{version}.tar.gz"
    - "my-new-package.spec"
    - "patch-1.patch"
```

1. Create a directory for the spec and source(s) under packages/
1. Download the spec and source(s)
1. `git annex addurl {url} -file my-new-package-{version}.tar.gz`, where `{url}` is the Source0 line 
    provided by `spectool my-package.spec` and `{version}` is the upstream version number of the dependency
1. Edit the spec setting the release to `1`
1. Scratch build your package 
    `tito release koji-pulp-server --test --scratch`
1. If your scratch build is successful, then please commit your additions and submit an MR.

TODO: ansible playbook to do this automatically.

## Comps Files

To ensure a package is created and shipped with the pulp repo, please be sure it's listed in it's corresponding 
`pulp-comps-{dist}.xml` file 

## Tito custom source strategy

There is a custom 'PulpSourceStrategy' class in rel-eng/lib/custom.py that is used to generate source tarballs from github.
 This allows us to have a spec file live outside the git repo for the nightly builds, and helps decouple release engineering
 effors from the main code repo.
