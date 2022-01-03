# Clear dist
rm -r dist/*

# Copy over all files from content
cp -r content/* dist

# Generate HTML files
find dist/ -name \*.md -type f -exec pandoc {} -o {}.html \;

# Rename .md.html files to .html
find dist/ -depth -name '*.md.html' -execdir bash -c 'mv -i "$1" "${1//md.html/html}"' bash {} \;

# Remove md files from dist
find dist/ -name "*.md" -type f -delete

# Replace hrefs to be html
find dist/ -name "*.html" -type f -exec sed -i -e 's/<a href="\([^"]*\)\.md/<a href="\1.html/g' {} \;