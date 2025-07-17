#!/bin/bash

hugo

cd public
git init
git remote add origin git@github.com:afash7/geektoria.git
git checkout -b gh-pages
git add .
git commit -m "Deploy site to GitHub Pages"
git push -f origin gh-pages