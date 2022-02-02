# Remind me about `Git` again .. ?

`Git` is a free, open-source _`version control`_ software. This basically means that Git is a content tracker. So `Git` can be used to store content — and it is mostly used to store code because of the other features it provides. Real life projects generally have _multiple developers working in parallel_. So they need a `version control` system like Git to make sure that there are _no code conflicts_ between them. Also, the requirements in such projects change often. So a version control system allows developers to revert and go back to an older version of their code. 

The `branch system` in Git allows developers to work individually on a task.

Last week, we could have created three branches in our personal repos - but we didn't. If we had, we might have created:
- one branch for labs
- one branch for quizzes
- one branch for 100 Days

This would be an example of `One branch -> One Topic`.

Instead, we will use the `Git` branch structure to manage our Group Projects and the individual workflows of each student member. So our group project folders will look more like this:
- one branch for Taha
- one branch for Haolin
- one branch for Mehrnaz

This would be an example of `One branch -> One Developer`. This will let us _work in parallel_ while still contributing to the _same project_. So! It is important that you feel comfortable with a basic `Git` workflow.


>
> You could even apply this to your own projects or 100 Days practice as a `One branch -> One Task` ?
> 

## What was that workflow again?

The basic Git workflow goes something like this[^1]:

1. You modify files in your working tree.
2. You selectively stage just those changes you want to be part of your next commit, which adds only those changes to the staging area.
3. You do a commit, which takes the files as they are in the staging area and stores that snapshot permanently to your Git directory.

---

## Some more `Git` refreshing

A repository (or “Repo” for short) is a project that contains multiple files. In our case a repository will contain code-based files. There are two ways you can host your repositories. One is online (on the cloud - our `remote` repos hosted in the `robots-make-art-too` organization here on `GitHub`) and the second is offline (self-installed on your server, or what we refer to as you `local` copy).

### Why so much importance on `Git`

`Git` lets us _track changes in our code across versions_

When multiple people collaborate on a project, it’s hard to keep track of revisions — who changed what, when, and where those files are stored. GitHub takes care of this problem by keeping track of all the changes that have been pushed to the repository. Much like using Microsoft Word or Google Drive, you can have a version history of your code so that previous versions are not lost with every iteration. It’s easy to come back to the previous version and contribute your work. 

For now, we will use our private repos on `robots`. So you should have already `cloned` the `remote` repo you made on GitHub and have a `local` copy on your local device. When you submitted your Quiz and Lab over the last two days you went through at least one of the following: `fetch` and `pull`[^2] 
- when we `fetch` from our `local` copy, we are asking Git to send a copy of all the changes in our `remote` repo that have occured since we last checked. If there were no remote changes, it might seem as if this step did nothing (or on GitHub desk top mentions that there is nothing to `fetch`)
- when we `pull`, Git first completes a `fetch` process _but then applies the changes_ to your local code

There are 4 steps in a commit: `status` , `add` , `commit`, and `push`. 
- when we request `status`, Git shows us a summary of what we are working on locally - what files are being `tracked`, those that aren't (GitHub desktop does this automatically and we see the changes visually)
- when we `add` we tell Git to `track` the file, folder etc.
- when we `commit` we are creating a _snapshot_ of the current state of all `tracked` files and we are essentially _committing_ to updating the remote files
- when we `push` we are applying the changes from our `commit` snapshot to the remote repo

---

## Git `merge`, `branch`, `checkout`

We will be working with these over the next few weeks in preparation for the group collaborative project development. Basic concepts:

1. Git `branch`
   - List, create, or delete branches
2. Git `checkout`
   - Switch branches or restore working tree files
3. Git `merge`
   - Join two or more development histories together

Note: When we need to be precise, we will use the word `branch` to mean a line of development, and `branch head` (or just `head`) to mean a reference to the most recent commit on a branch.

What is this?

`HEAD` is a special reference that _points to the commit you are currently working on_ (we can call this our currently checked out commit). You can think of it as a global variable that can change depending on which commit you've checked out in your working directory. It is stored in a file called .git/HEAD, which I recommend you peek at in your text editor.[^3] 

---

### UPDATED SECTIONS WILL CONTINUE TO APPEAR AS WE NEED THEM OR MORE CLARIFICATION

---

Where'd I get a lot of this summarized `Git` content? Oh yeah. From that link I posted _the first day_ of [class](https://www.freecodecamp.org/news/the-beginners-guide-to-git-github/)

[^1]: https://git-scm.com/book/en/v2/Getting-Started-What-is-Git%3F#what_is_git_section
[^2]: https://www.jetbrains.com/help/idea/sync-with-a-remote-repository.html
[^3]: https://initialcommit.com/blog/what-is-git-head
