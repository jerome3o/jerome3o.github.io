---
layout: post
title: Machine Learning Rig: Metrics
---

# Converting from VSCode to nvim

## Comparison

* Python LSP
  * PyRight on VSCode
  * ruff-lsp on nvim (lsp-config, TODO: link)
* Automatic formatting
  * Black on both, hooked into lsp
* Multi-cursor
  * Built-in to VSCode
  * Multi-cursor plugin (TODO: get details)
* debugpy debugging
  * Python plugin in VSCode
  * dap-config, wasn't very good, went for ipdb
* Snippets
  * Snippet config from vscode works with nvim plugin (TODO: link plugin)
* Folder tree
  * Built-in vscode
  * Tried nerd-tree, changed to nvim-tree
* Syntax highlighting
  * Python plugin
  * nvim-treesitter
* Code navigation via ast
* Fuzzy file search
  * Built-in ctrl-p VSCode
  * fd, telescope
* Fuzzy global search
  * Built-in ctrl+shift+f
  * fzf, telescope
* Built-in terminal
  * tmux
* Python environment management
  * manual

TODO: link to dotfiles

## New in nvim

* Copilot (never used it in VSCode)

## Left behind

* Control pallette search
* Debugging

