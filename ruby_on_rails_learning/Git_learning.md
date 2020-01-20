# Git Version Control Systems(VCS)
1. decentralized control system
2. server is (almost) not involoved
3. can push & pull between repos

# Git Basics
1. one .git directory at the **top level**
2. (empty)**Create** or(existing) clone repo
3. add **changing** to staging area
4. commit **changes**(from staging area to local repo)
5. push **changes** from local to remote repo
commit locally
push remotely

## Git practice
the function of git
1. VCS -Version Control System
2. SCM -Source Code Management
advantage of git
1. Backups are trivial -Each local repository is a Full copy including all the codes and all the change-history
2. Internet connection is not required for common Git operations

## tips
1. mods made to the file after "git add" - need to be "get added" again - even if you did not commit yet
2. 3 repository: working repository; repository; staging area
3. to skip the staging area - just use -a (after initially adding the file) **git commit - am**(after file tracted by the repository)
4. have to add a file for tracking at least once before it can make it into the repo
5. can easily go "back in time" to a snapshot

## command to remember
1. git diff -diff between staging & working area
2. git diff --staged -changes between HEAD(last commit on current branch) & staging area
3. git diff HEAD -diff between HEAD & working area
Going back in Time
*before commit*
4. git checkout re-checkout all tracked files overwriting local changes
5. git checkout -- <file> re-checkout **just one** specific file
*after committing*
6. git revert HEAD - reverts the most recent commit

# Interacting with remote repositories; Github


