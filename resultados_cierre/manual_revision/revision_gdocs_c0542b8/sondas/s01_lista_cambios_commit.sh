#!/bin/sh
# G-DOCS: lista exacta de archivos del commit c0542b83 vs base 957af65 (solo lectura, API GitHub)
gh api "repos/jluisplagos/munger-v2/compare/957af652cdc3bef3d67e8623c9572138bac685e9...c0542b83b9923f98124d3c72e48b7fc7245284d2" \
  --jq '{status, ahead_by, total_commits, files: [.files[] | {filename, status, additions, deletions}]}'
# comprobacion del padre del commit y del HEAD de la rama
gh api repos/jluisplagos/munger-v2/commits/c0542b83b9923f98124d3c72e48b7fc7245284d2 --jq '{sha: .sha, parents: [.parents[].sha]}'
gh api repos/jluisplagos/munger-v2/branches/integracion/docs-operativos-957af65 --jq '{rama_head: .commit.sha}'
