rem notebook to useful command lines

rem /********************activate conda base, as it is not in PATH***********************************/
rem /********************Open Terminal  (Power Shell ) RUN as ADMINSITRATOR ***********************************/
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned

rem /******************** open a Anaconda PowerShell Prompt ***********************************/
conda init powershell

rem /******************** re-open a regular PowerShell Prompt ***********************************/
conda info

rem /********************create env indicating wnvironment folder ***********************************/
rem /*********************from root project folder, so it finds evironment.yml **********************************/
conda env create --prefix .\conda-envs\oop-magic-methods-task-3-student-template-env --file environment.yml 

rem /***********activate the environment ******************/
conda activate .\conda-envs\oop-magic-methods-task-3-student-template-env


rem /*********** Set local (project folder) username  ******************/
git config --local user.name "Joseph Higaki" | git config --local user.email "josephhigaki@hotmail.com"


