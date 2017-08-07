Coding style Guidelines
=======================

Follow [PEP-8](https://www.python.org/dev/peps/pep-0008/) coding guidelines.


Commit Message Guidelines
=========================

Commit Guidelines inspired by [Gnome Commit Guidelines](https://wiki.gnome.org/Git/CommitMessages).

Those are only general-purpose recommended guidelines, depending on the context of each PR the following rules can vary. 

Remember: the commit message is mainly for the other people, so they should be able to understand the changes made at any point in time.

Example
-------

```
short explanation of the commit

Longer (optional) explanation explaining exactly what's changed and why instead of how,
whether any external or private interfaces changed, what bugs were fixed (with bug
tracker reference if applicable) and so forth. Be concise but not too brief. Avoid writing long lines, use newlines when necessary.

[Reference to the issue solved, if any]
```

Details
-------

- First line (the brief description) must only be one sentence in imperative mood. The message should be concise, less than 50 characters if possible. Do not end it with a period.
- The long explanation is optional, although it is encouraged to be written if it helps clarify the issue tackled. Explain the "why", not the "how" there and try to wrap every line at 72 characters. Also, keep a blank like between the first line and the long explanation.
- Remember to commit your code with a [username](https://help.github.com/articles/setting-your-username-in-git/) and [email](https://help.github.com/articles/setting-your-email-in-git/).
- If there is an issue created for this commit, link it at the end of the commit message, in a new line. The issue should follow the [GitHub guidelines](https://help.github.com/articles/closing-issues-via-commit-messages/#closing-an-issue-in-the-same-repository).