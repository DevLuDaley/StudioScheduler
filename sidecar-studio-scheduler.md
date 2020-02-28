# 1\. create and activate \(env_pizza\)

```
create github repo titled => studioScheduler
```

`git clone git@github.com:DevLuDaley/django-forms.git`

`cd studioscheduler`

`python3 -m venv env_studioscheduler`

<br>
\`\`\`
actovate environment - also either vcode will ask or just press  \`shift +cmd +P\` and select interpreter
\`\`\`

`source env_studioscheduler/bin/activate`

```
access command palette => [cmd + shift + P]
enter 'interpreter'
select python env
```

<br>
<br>
```
select ['env_studioscheduler':venv] environment
```

# 2\. setup env complete django

# 3\. git checkout 2-setup-django

clone setup env branch to create 'stup-django' branch

git checkoiut to new branch

`git checkout setup_django`

```
note:
  if you get an error pull the latest version of the master project from the remote repo.
  Now the local git knows about the new branch ('django-setup') created in remote git/GitHub
```

`git pull`

# 4\. install django + project & app

`pip install django`

```
create studio project & folder
```

`django-admin startproject studio`

```
rename project folder to projectstudio
```

`mv studio/ projectstudio`

- the tutorial says nandiasgarden-project but "name-project" produces an error in py 3.8\*\*
- rename project folder. add project to start of the name i.e folder => projectfolder or projectnandiasgarden for this project
- this helps differentiate between the project folder and the autogenerate folder (with the identaical project name) that lives in the project folder

```
open projectstudio
```

`cd projectstudio`

```
create scheduler app
```

`django-admin startapp scheduler`

update settings.py
to include new app => 'scheduler'
change Timezone to 'EST'

```
use github desktop app
commit=>push => create new_branch (clone current) => checkout new_branch
```

# 5\. git checkout 3-setup-models/relationships

# 6\. create models


![](2020-02-27-21-51-30.png)

