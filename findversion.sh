#!/bin/sh

# Root directory
cd `dirname "$0"`
ROOT_DIR=`pwd`

# Determine if we are using modified version
MODIFIED="0"

# If there is .git directory
if [ -d "$ROOT_DIR/.git" ] || [ -f "$ROOT_DIR/.git" ]; then
  # Refresh the index to make sure file stat info is in sync, then look for modifications
  git update-index --refresh >/dev/null

  # Modified, but uncommitted
  if [ -n "`git diff-index HEAD`" ]; then
    MODIFIED="1"
  fi
  
  # Get current commit's hash and tag
  HASH=`LC_ALL=C git rev-parse --verify HEAD 2>/dev/null`
  SHORTHASH=`echo $HASH | cut -c1-10`
  ISODATE=`LC_ALL=C git show -s --pretty='format:%ci' HEAD | awk '{ gsub("-", "", $1); print $1 }'`
  BRANCH="`git symbolic-ref -q HEAD 2>/dev/null | sed 's@.*/@@'`"
  TAG="`git name-rev --name-only --tags --no-undefined HEAD 2>/dev/null | sed 's@\^0$@@'`"

  # If the current commit has a tag, it is a release version
  if [ -n "$TAG" ]; then
    VERSION="$TAG"
  else
    VERSION="$ISODATE-$BRANCH-$SHORTHASH"
  fi

# If there is .rev file
elif [ -f "$ROOT_DIR/.rev" ]; then
  VERSION=`cat $ROOT_DIR/.rev`

# Or, we don't know
else
  VERSION=`date +"%Y%m%d"`
fi

echo "$VERSION"
