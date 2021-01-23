<div>
<img src="http://drive.google.com/uc?export=view&id=1MADw5CwZYysojTdKwgfJEJpAHdO1Jxoq">
<h1 style="font-family: -apple-system, BlinkMacSystemFont, 'Space Mono', sans-serif;">Hack your Learning: Session 1 - Part 3
</h1>
</div>

The purpose of the exercises in this section is to broaden your knowledge of `git` commands that have the power to rewrite history. Specifically, you will learn about `git rebase` and how interactive rebasing can be used to Amend, Reword, Delete, Reorder, Squash and Split commits.

To learn about these abilities, you will watch 2 short YouTube videos. Then, you will practice using the git commands with branches & commits that have been pre-created for you. Exercises 1-9 are individual exercises and do not require teamwork to complete. However, we encourage you to work in teams to share knowledge and help each other. If you have time, exercise 10 should be done in a team!

### The Problem

For this exercise, you will be working with Python. You will create a simple cryptography application that allows you to encode and decode messages by entering a message to encode/decode and a secret to help encode/decode it. To do exercises 1-9, you will not be required to do much coding - most of it has already been done for you. 

This repository contains many branches which each contain definitions for different parts of the cryptographic system. As you progress through the exercise, you will gradually reassemble these branches into one working system. For most exercises, you should NOT copy, paste, or delete code, except when resolving conflicts.

At any point, you can test your code by running `python encode.py` in your command line. It should compile and run with no errors. Once you have combined the different branches, you may test your program's cryptographic abilities by editing the definitions of `encode` and `decode` to use appropriate encoding and decoding algorithms.

### Getting started

1. Fork this repository to your own GitHub repo. 
2. Clone your repo onto your local machine using `git clone`.
3. If you haven't already, download and install Python (https://www.python.org/downloads/)

## Learn - Part 1: Rebasing

To learn about rebasing and what makes it different than merging, read the following article: https://www.atlassian.com/git/tutorials/rewriting-history/git-rebase

Then, watch the following video to reinforce your learning:
https://www.youtube.com/watch?v=f1wnYdLEpgI

One important caveat to remember with rebase is that it rewrites history (deletes and recreates commits). Therefore, it can be very dangerous to use when other people may already be working with the commits you are rebasing. Rebasing and rewriting history can be a very handy tool when you are working on your local branches, but be very careful if you ever do this with branches and commits that are on a remote repository where you are collaborating with other people.

With that being said, in the following exercises you will be rebasing and rewriting history that exists on your forked remote repository for the sake of convenience and learning.

### Refresher on branches

Whenever you need to access a branch for the first time on your local repository, follow these directions:
1. Use `git branch branchNameHere` to create the branch in your local repository
2. Use `git checkout branchNameHere` to switch to it
3. Finally, use `git pull origin branchNameHere` to sync with the commits for that branch from the origin repository. 

After you have completed these steps, you may switch between branches using `git checkout`. Remember: branches from the remote repository will not exist on your local repository unless you manually follow the above steps to add them!

## Exercise 1: Rebase (Easy)

Using your knowledge from above, you will rebase the caesarfeat branch on to the caesar branch.
Here is what these branches' history currently looks like:

```
    caesarfeat->(Add decode caesar)
                /
caesar->(Create caesar)
          /
     (Create runtest)-(Print output)<- main
```

Here is what it should look like after you finish:

```
     (Create caesar)-(Add decode caesar)<-caesar
       /
    (Create runtest)-(Print output)<- main
```

## Exercise 2: Rebase (Hard)

Next, rebase the caesar branch onto main, following the methodology employed by the above video. When you are done, the commit history should look something like:

`(Create runtest)-(Print output)-(Create caesar)-(Add decode caesar)<- main`

## Learn Part 2: Interactive Rebasing and Rewriting

Now, we're going to learn about interactive rebasing and rewriting history so we can apply it to other parts of the problem. To do this, watch this video: https://www.youtube.com/watch?v=ElRzTuYln0M

The video is split into parts. Each part corresponds to an exercise below. 

An easy way of seeing your commit history is with `git log --oneline`.

## Exercise 3: Ammending

Switch to the `shuffle` branch. Notice that the encode_shuffle function isn't returning the shuffled string- instead, it's returning `""` every time! Fix this issue. What if we wanted to add your fix without creating a new commit? We could ammend it to the previous commit. Follow the instructions from the video to accomplish this.

## Exercise 4: Rewording

Notice how one of the previous commits in the shuffle branch is called "sbubby". Let's rename this commit "Add decode shuffle", using the method demonstrated in the above video.

## Exercise 5: Deleting Commits

A group of malicious magic Lennys have invaded the shuffle branch! Instead of deleting them manually, use your knowledge of rebasing to delete the commit `Invasion by Magic Lennys` to solve the problem. 

## Exercise 6: Reordering Commits

Now, switch to the `vigenere` branch and pull from origin. This branch uses the Vigenere method to encode and decode messsages. You can read about it here: https://pages.mtu.edu/~shene/NSF-4/Tutorial/VIG/Vig-Base.html  
Notice how the branch has the following structure:

`(Create Vigenere)-(Encode Part 1)-(Decode Vigenere and Add Art)-(Encode Part 2)-(Encode Part 3)`

Your task is to reorder the commits so that they have the following order:

`(Create Vigenere)-(Decode Vigenere and Add Art)-(Encode Part 1)-(Encode Part 2)-(Encode Part 3)`

## Exercise 7: Squashing Commits

Instead of having 3 separate commits for encode, why don't we combine them into one? Use the squash method illustrated by the video to squash each Encode commit into a single commit. Bonus if you rename this commit simply `Encode Vigenere`!

## Exercise 8: Splitting Commits

Split the commit `Decode Vigenere and Add Art` into 2 separate commits: `Decode Vigenere` and `Add Art`. Decode Vigenere modifies Vigenere.py, while Add art modifies `encode.py`.

## Exercise 9: Put it all together!

Using your new knowledge of rebasing and your previous knowledge of merging, adopt the strategy of your choice to combine the features of `shuffle` and `Vigenere` into one branch (preferably main). You should not copy and paste anything.

Once it's all together, you can make changes to combine different methods of encoding and decoding your message. Encode a message for your friends and see if they can decode it given the secret and your order of operations! Note: be careful encoding messages that contain spaces, as you may not notice extra whitespace in the printed result.

As a bonus, try decoding this message: `slPmuzUOvvYaijePwyYhUmsRwkGctew`. It was encoded using caesar, then shuffle, then vigenere, using the secret `hackYourLearning!`. 

## Exercise 10: Collaborate

Can you think of a new way to encode and decode a message? Pair up with a partner and decide whose repository you will work on. Create a new branch for your crypto method, and have them create a branch for a different crypto message, and when you've completed your implementations try putting them together using `git rebase` and/or `git merge`. Test out your new encryption methods to see if they work!

Congrats, you've completed all the challenges! Thanks for participating in this Hack Your Learning prep session- follow our social media to stay up to date with upcoming events!