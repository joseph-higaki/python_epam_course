rem /* Clone
git clone git@gitlab.com:joseph-higaki/data-types-final-task-2-student-template.git

rem /* Configure Local gitlab*/
git config --local user.name "Joseph Higaki" | git config --local user.email "josephhigaki@hotmail.com"

rem /* conda env
conda env create --prefix .\conda-envs\data-types-final-task-2-student-template-env --file environment.yml 
conda activate .\conda-envs\data-types-final-task-2-student-template-env

rem /*********** adding code  ******************/
git checkout -b add-main-logic
git add .
git commit -m 'Add logic and unit tests'

git checkout main
git merge add-main-logic
git push origin main 

