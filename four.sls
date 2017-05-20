Clone yum-s3-iam plugin Github:
  git.latest:
    - name: https://github.com/seporaitis/yum-s3-iam
    - target: /usr/share/yum-s3-iam/

Copy yum-s3-iam plugin files to yim:
  cmd.run:
    - name: |
        cp s3iam.py /usr/lib/yum-plugins/
        cp s3iam.conf /etc/yum/pluginconf.d/
    - cwd: /usr/share/yum-s3-iam/
    - require:
      - git: Clone yum-s3-iam plugin Github