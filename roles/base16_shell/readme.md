# `dannixon.user.base16_shell`

Installs [base16-shell](https://github.com/chriskempson/base16-shell/) and sets the current theme.

## Role Variables

The theme that is enabled by default can be set via `base16_shell_theme`.

## Example Playbook

```yaml
- hosts: all
  become: true

  vars:
    base16_shell_theme: material-darker

  roles:
    - dannixon.user.base16_shell
```

## License

MIT
