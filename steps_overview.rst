Steps
==============

1. Get existing version from setup.py
2. Update setup.py version #
    2.1 *Validate*: setup() func has a version argument (version=)
    2.2 *Validate*: Version format: (\d)+\.(\d)+.(\d)+. --> major_no, minor_no, patch_no
3. git add -up
    3.1 *Validate*: on master
    3.2 *Validate*: nothing modified in repo
    3.3 *Validate*: nothing staged in repo
    3.4 *Abstract*: --> is_clean_repo(repo_dir) combining the 3 validations
4. git commit -m "{version}"
5. git push origin master
6. git tag "{version}"
7. git push --tags
8. cd to root of virtualenv
9. Update version in requirements.txt in update_target_repo
10. get add -up
11. git commit -m "Bump {repo} to {version}"
12. git push origin master

