#!/bin/bash

# load GITLAB_PRIVATE_TOKEN
source .env

# Initialize variables
page=1
per_page=100  # Maximum allowed per page
all_projects="[]"

# Fetch all pages of projects
while true; do
    response=$(curl --header "PRIVATE-TOKEN: $GITLAB_PRIVATE_TOKEN" "https://gitlab.com/api/v4/users/joseph-higaki/projects?page=$page&per_page=$per_page")
    projects=$(echo "$response" | jq '.')
    
    # Break the loop if no more projects are returned
    if [ "$(echo "$projects" | jq 'length')" -eq 0 ]; then
        break
    fi

    # Combine the current page of projects with the previous ones
    all_projects=$(echo "$all_projects" "$projects" | jq -s 'add')

    echo "Fetched page: $page"
    # Increment the page number
    page=$((page + 1))    
done

# Save all projects to a file
echo "$all_projects" > projects.json

rm project_list.txt
echo "project_name,timestamp,http_url_to_repo" > project_list.txt
# Parse the JSON and clone each project
for repo_url in $(jq -r '.[].http_url_to_repo' projects.json); do
    #get project name
    project_name=$(basename "$repo_url" .git)
    #store in csv
    echo "$project_name,$(date --utc +%FT%T.%3NZ),$repo_url" >> project_list.txt
    #include access token
    repo_url_with_token="${repo_url/https:\/\//https:\/\/oauth2:$GITLAB_PRIVATE_TOKEN@}"
    #clone repo
    git clone "$repo_url_with_token"
    # Remove the .git directory from the cloned repository
    rm -rf "$project_name/.git"
done