rem /******************** open a Anaconda PowerShell Prompt ***********************************/
conda init powershell

rem /******************** re-open a regular PowerShell Prompt ***********************************/
conda info

rem /********************create env indicating wnvironment folder ***********************************/
rem /*********************from root project folder, so it finds evironment.yml **********************************/
conda env create --prefix .\conda-envs\scrapper-student-template-env --file environment.yml 

rem /***********activate the environment ******************/
conda activate .\conda-envs\scrapper-student-template-env


rem /***********remove the environment ******************/
conda env remove -p .\conda-envs\scrapper-student-template-env 

rem /*********** GIT ******************/
rem /* Configure Local gitlab*/
git config --local user.name "Joseph Higaki" | git config --local user.email "josephhigaki@hotmail.com

rem /*********** generatre \ work loaptop key  ******************/
ssh-keygen -t ed25519 -C "joseph_higaki work laptop epam.git"

rem /*********** Add an SSH key to your GitLab account in Profile SSH keys  ******************/

rem /*********** Connect to remote GitLab  ******************/
ssh -T git@git.epam.com


rem /*********** git init  ******************/
git init
git add . 
git commit -m 'Initial Commit, project creation'

git remote add origin git@git.epam.com
git remote add origin git@git.epam.com:joseph_higaki/py101.git
git push origin main



rem /*********** adding code  ******************/
git checkout add-main-logic
git add . adedd helloworld py and changes in ntes command



rem /***********  SUBMITTING TO GITHUB ******************/

rem /*********** generatre \ work loaptop key  ******************/
ssh-keygen -t ed25519 -C "josephhigaki@hotmail EPAM work laptop for github.com" -f "$HOME/.ssh/id_ed25519_github"

rem /*********** Add an SSH key to your GitLab account in Profile SSH keys  ******************/
ssh-add $HOME/.ssh/id_ed25519_github


rem /*********** Connect to remote GitLab  ******************/
rem /*********** C:\Users\Joseph_Higaki\.ssh\config file ******************/
# github.com
Host github.com
    HostName github.com
    User git
    IdentityFile ~/.ssh/id_ed25519_github

rem /*********** Connect to remote GitLab  ******************/
ssh -T git@github.com


rem /*********** Set local (project folder) username  ******************/
git config --local user.name "Joseph Higaki" | git config --local user.email "josephhigaki@hotmail.com"

git remote add personal-origin git@github.com:joseph-higaki/py101.git


--json https://news.yahoo.com/rss
--json --limit 3 https://news.yahoo.com/rss

--limit 3 https://news.yahoo.com/rss
https://news.yahoo.com/rss

https://rss.nytimes.com/services/xml/rss/nyt/Travel.xml
--json https://rss.nytimes.com/services/xml/rss/nyt/Travel.xml