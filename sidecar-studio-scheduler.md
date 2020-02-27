# 1\. create and activate \(env\_pizza\)

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

# 2\. install django

```
clone master branch to create 'django-setup' branch

note:
  if you get an error pull the latest version of the master project from the remote repo.

  Now the local git knows about the new branch ('django-setup') created in remote git/GitHub
```

`git pull`

`git checkout setup_django`

`pip install django`

# 3\. create nandiasgarden project & folder

`django-admin startproject nandiasgarden`

# 4\. rename project folder to projectnandiasgarden

`mv nandiasgarden/ projectnandiasgarden`

* the tutorial says nandiasgarden-project but "name-project" produces an error in py 3.8\*\*
* rename project folder. add project to start of the name i.e folder => projectfolder or projectnandiasgarden for this project
* this helps differentiate between the project folder and the autogenerate folder (with the identaical project name) that lives in the project folder

open projectnandiasgarden

`cd projectnandiasgarden`

`django-admin startapp pizza`

# 5\. create pizza app

`django-admin startapp pizza`