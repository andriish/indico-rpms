# indico-rpms
RPMS for Indico


To install:

```
yum install indico-mpp indico-devel python3-indico
```

After the installation, as root:

```
su  indico 
bash-5.2$ indico user create
Email: 
First name: 
Last name: 
Affiliation []: 

Enter username: 
Password: 
Repeat for confirmation: 
User info:
  ID: 1
  First name: 
  Family name: 
  Email: 
  Affiliation: 

Create the new user? [Y/n]: Y
New user created successfully with ID: 1
bash-5.2$ indico  user grant-admin 1
User info:
  ID: 1
  First name: 
  Family name: 
  Email: 
  Affiliation: 

Grant administration rights to this user? [y/N]: y
Administration rights granted successfully
bash-5.2$ 
```

To run

```
/usr/bin/indico-devel-start-indico.sh
```