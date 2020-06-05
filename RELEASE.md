# Instructions for creating a release

- [ ] Check out the release branch. Release branches are named `release-{MAJOR}.{MINOR}`.
- [ ] Update `CLIENT_VERSION` in [`scripts/constants.py`](scripts/constants.py#L26) to reflect the new version.
- [ ] Update `KUBERNETES_CLIENT_VERSION` in [`scripts/constants.py`](scripts/constants.py#L27) to reflect an updated `kubernetes` python package, if needed.
- [ ] Run [`scripts/update_version.sh`](scripts/update_version.sh). This will update the version numbers everywhere they are referenced.
- [ ] Commit the changes made by the previous step. If you have push access, you can push the branch up directly. If not, you can open a PR and a maintainer will review and merge it.
- [ ] In the GitHub UI go to the [`releases`](https://github.com/openshift/openshift-restclient-python/releases) tab. Select [`Draft a new release`](https://github.com/openshift/openshift-restclient-python/releases/new).
- [ ] For tag version, fill in `v` followed by the value for `CLIENT_VERSION` that you added to [`constants.py`](scripts/constants.py#L26), ie, if your `CLIENT_VERSION` is `0.36.2`, your tag will be `v0.36.2`
- [ ] Ensure that the `Target` is set to the proper `release-{MAJOR}.{MINOR}`, NOT master.
- [ ] For `Release title`, just put `Release` followed by the new version you set in `CLIENT_VERSION`
- [ ] For the release notes, summarize the features and bugfixes that have been made since the last release. There is no automation for this part yet unfortunately.
- [ ] Click `Publish release`. This will kick off a travis-ci build, and once that succeeds the package will be uploaded to pypi automatically.
