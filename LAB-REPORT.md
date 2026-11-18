# Lab Report – Assignment 4

**Name:** Sharjeel Shahzad
**Registration No:** FA23-BSE-170
**Course:** DevOps for Cloud Computing (CSC418)
**Instructor:** Dr. M. Hasanain Ch

**Repository URL:** https://github.com/Sharjeel-Shahzad1/student-task-manager
**Release URL:** https://github.com/Sharjeel-Shahzad1/student-task-manager/releases/tag/v1.0.0

---

## 1. Git vs GitHub; add, commit, push
**Git** is a version control tool that runs on my computer and tracks changes to files.
**GitHub** is a website that hosts Git repositories online so people can share code and work together.

- `git add` puts changed files in the staging area (chooses what goes in the next commit).
- `git commit` saves a snapshot of the staged changes with a message.
- `git push` sends my local commits to the remote repository on GitHub.

## 2. Branches, Pull Requests, merge conflicts
**Branches** let me work on one feature separately without breaking the main code. In this project, add, complete and delete were each built on their own branch.
**Pull Requests** let others review the changes before they are merged into `main`.
A **merge conflict** happens when two branches change the same line of the same file differently, and Git cannot decide which version to keep. In Part D, both branches changed the "Project status" line in README.md.

## 3. fetch vs pull; merge vs rebase
- `git fetch` downloads new changes from GitHub but does not change my files.
- `git pull` = fetch + merge, so it downloads and applies the changes.
- `git merge` joins two branches and creates a merge commit, keeping the full history.
- `git rebase` moves my commits on top of another branch, giving a straight, cleaner history.

## 4. GitHub Issues and Actions
**Issues** are used to track tasks, bugs and features, so the team knows what needs to be done. Each of my PRs closed an Issue.
**Actions** automatically run tests on every push or pull request, so broken code is caught before it is merged. My workflow caught a wrong test before merging.

## 5. Difficulty faced
While merging the second status branch, I got a merge conflict in README.md. At first I did not understand the
`<<<<<<<`, `=======` and `>>>>>>>` markers. I learned that the top part is the current branch (main) and the bottom
part is the incoming branch. I edited the file to keep one correct line, removed the markers, then ran
`git add` and `git commit` to finish the merge without losing any other work.

---

## Evidence
Screenshots of key steps are in the [lab-evidence](lab-evidence/) folder.
