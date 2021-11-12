
for var in "$@"
do
  case "$var" in
    setup)
      rm -fr ./themes/learn
      git clone https://github.com/matcornic/hugo-theme-learn.git ./themes/learn
      ;;
    serve)
      hugo serve
      ;;
    *)
      ;;
  esac
done
