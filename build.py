
top = open('./templates/top.html').read()
bottom = open('./templates/bottom.html').read()
blog = open('./content/index.html').read()
projects = open('./content/projects.html').read()
about = open('./content/about.html').read()

open('docs/index.html', 'a+').write(top)
open('docs/index.html', 'a+').write(blog)
open('docs/index.html', 'a+').write(bottom)

open('docs/about.html', 'a+').write(top)
open('docs/about.html', 'a+').write(about)
open('docs/about.html', 'a+').write(bottom)

open('docs/projects.html', 'a+').write(top)
open('docs/projects.html', 'a+').write(projects)
open('docs/projects.html', 'a+').write(bottom)
