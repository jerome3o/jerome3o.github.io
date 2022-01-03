# Generate HTML files
find content/ -name \*.md -type f -exec pandoc ./dist/{} -o {} \;

