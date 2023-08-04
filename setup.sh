sudo apt install -y git stow

(
  cd ~
  git clone https://github.com/jerome3o/dotfiles
  (
    cd dotfiles/
    source ./stow_all.sh
  )
  source ./scripts/terminal.sh
)

