# `dannixon.user.nerdfont`

[![dannixon.user.nerdfont](https://github.com/DanNixon/ansible-user/actions/workflows/nerdfont.yml/badge.svg?branch=main)](https://github.com/DanNixon/ansible-user/actions/workflows/nerdfont.yml)

Installs a selection of [Nerd Fonts](https://www.nerdfonts.com/).

## Role Variables

The font(s) to be installed are set via the `nerdfont_fonts` variable.

## Example Playbook

```yaml
- hosts: all
  become: true

  vars:
    nerdfont_fonts:
      - DejaVuSansMono

  roles:
    - dannixon.user.nerdfont
```

## License

MIT
