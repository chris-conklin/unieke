#!/bin/bash



create_directory()
{

  if [[ ! -e $1 ]]; then
    mkdir $1
  elif [[ ! -d $1 ]]; then
    echo "$1 already exists but is not a directory" 1>&2
  fi
}

create_directory "content"
create_directory "db"
create_directory "log"
create_directory "dropoff"
create_directory "trashes"



