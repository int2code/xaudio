
Contribution
============

To contribute to the project follow below steps:

    * git clone this project repository
    * create dev branch using your initials and an descriptive name like `user/feature_name`
    * modify code as desired
    * write unittests to cover your changes
    * verify that pylint, pytest and other checkers pass
    * update `RELEASE_NOTES.rst` and `version.txt` according to `sematic versioning <https://semver.org/>`_
    * create a pull request - add at least one reviewer
    * fix any comments until review is accepted
    * merge your changes

After your changes are merged to the main branch an automatic pipeline will trigger,
verify your changes, build the package and finally upload it to artifactory server.
