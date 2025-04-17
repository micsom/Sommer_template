  #!/bin/bash
  set -e

  REPO_NAME=$1
  ORG=$2
  DESCRIPTION="sommer_repo"

  echo "Creating repo $REPO_NAME under org $ORG"

  gh repo create "$ORG/$REPO_NAME" \
    --private \
    --description "$DESCRIPTION" \
    --template micsom/sommer_repo \
    --enable-issues \
    --enable-actions \
    --clone

  cd $REPO_NAME
  git remote add upstream "https://github.com/micsom/sommer_repop.git"
  echo "Repo $REPO_NAME initialized and ready."