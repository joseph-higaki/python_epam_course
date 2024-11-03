#!/bin/bash

# load GITLAB_PRIVATE_TOKEN
source .env

# Fetch the list of projects
curl --header "PRIVATE-TOKEN: $GITLAB_PRIVATE_TOKEN" "https://gitlab.com/api/v4/users/joseph-higaki/projects" -o projects.json

# Parse the JSON and clone each project
for repo_url in $(jq -r '.[].http_url_to_repo' projects.json); do
    # Insert the token into the URL
    repo_url_with_token="${repo_url/https:\/\//https:\/\/oauth2:$GITLAB_PRIVATE_TOKEN@}"
    #echo "... Cloning.... $repo_url_with_token"
    echo $repo_url >> project_list.txt
    #git clone "$repo_url_with_token"
done

#rm projects.json