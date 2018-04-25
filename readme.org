* Chomper

[[../assets/chomper_example.gif?raw=true]]

*** Note: Welcome to [[https://twit.tv/shows/floss-weekly][FLOSS Weekly]] viewers! I'm looking for collaborators on Chomper - in particular with creating a GUI, adapting Chomper for OSX, and packaging Chomper with pyinstaller. Reach out to me at the [[https://gitter.im/chomperapp/Lobby][Chomper Gitter channel]] if you want to work together!

Chomper is a Python command-line program for use on Linux which can either create blacklists of blocked websites or whitelists of allowed websites for specified periods of time. The program is intended to help people with issues being productive on a computer due to Internet distractions.

Most internet blocking programs operate just by modifying [[https://en.wikipedia.org/wiki/Hosts_(file)][the hosts file]]. This approach only allows for creating blacklists. Additionally, the hosts file approach does not allow you to block particular URLs - it only allows you to block particular domains.

Chomper instead filters outgoing requests through a transparent proxy, which allows for filtering requests at the URL level. This means you can make nuanced blacklists and whitelists, so that you can block websites without sacrificing your ability to do work.

You can read more about my motivation for developing Chomper [[https://addictedto.tech/chomper/][here]].
* Docs/Installation/Usage
You can find the installation and usage information at [[https://chomper.readthedocs.io][ReadTheDocs]].
* Support
You can ask questions and join the development discussion on the [[https://gitter.im/chomperapp/Lobby][Chomper Gitter channel]].

Please post bug reports and feature requests (only) in GitHub issues.
* License
Chomper is licensed according to the GPLv3. See the COPYING file for more details.
* Contributing
Interested in contributing? Awesome! Start by reading the [[https://chomper.readthedocs.io/en/latest/development/index.html][developer's walkthrough]] to the Chomper codebase. For guidelines on making pull requests, please read the [[./CONTRIBUTING.org][CONTRIBUTING.org file]].
* About
Chomper was created and is maintained by Aniket Panjwani. For a full list of contributors, go [[https://github.com/aniketpanjwani/chomper/graphs/contributors][here]].
