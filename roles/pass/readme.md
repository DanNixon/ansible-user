# `dannixon.user.pass`

[![dannixon.user.pass](https://github.com/DanNixon/ansible-user/actions/workflows/pass.yml/badge.svg?branch=main)](https://github.com/DanNixon/ansible-user/actions/workflows/pass.yml)

Installs [pass](https://www.passwordstore.org/) and a [fzf](https://github.com/junegunn/fzf/) based helper script.

## Example Playbook

```yaml
- hosts: all
  become: true

  roles:
    - dannixon.user.pass
```

## License

MIT
